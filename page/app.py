import requests
import json
import os
import re

from itertools import islice

from bs4 import BeautifulSoup
from .models.team import Team
from .models.member import Member
from .common import PATH, logger, oauth_credential, git_credential
from .database import remote_db, local_db
from collections import defaultdict
from flask import Flask, render_template, url_for, request, redirect, flash
from flask_login import LoginManager, current_user, login_required, login_user, logout_user
from oauthlib.oauth2 import WebApplicationClient


def create_app():
  app = Flask(__name__)
  app.secret_key = "page"
  login_manager = LoginManager()
  login_manager.init_app(app)

  GOOGLE_DISCOVERY_URL = "https://accounts.google.com/.well-known/openid-configuration"

  @login_manager.user_loader
  def load_user(user_id):
    return remote_db.get("member", user_id)

  @app.route("/admin/<string:team_id>", methods=["POST", "GET"])
  def admin(team_id):
    return render_template("admin.html", progress_overview_html=Team.show_progress(team_id))

  @app.route('/resume')
  def download_resume():
    return send_file("/resume.pdf", as_attachment=True)

  @app.route("/premium", methods=["POST", "GET"])
  def premium():
    if request.method == 'POST':
      current_user.team_id = request.form["team_id"]
      remote_db.add("memeber", current_user)
      return redirect(url_for("index"))
    return render_template("premium.html")

  @app.route("/", methods=["GET"])
  def index():
    return render_template("index.html")

  @app.route("/signin", methods=["POST", "GET"])
  def signin():
    logger.debug("signin()")
    client = WebApplicationClient(oauth_credential["client_id"])
    authorization_endpoint = requests.get(GOOGLE_DISCOVERY_URL).json()["authorization_endpoint"]
    request_uri = client.prepare_request_uri(authorization_endpoint, redirect_uri=request.base_url + "/callback", scope=["openid", "email", "profile"],)
    logger.debug(request_uri)
    return redirect(request_uri)

  @app.route("/login/<string:id>")
  def login(id):
    logger.debug(f"login")
    if id != "sofialee7979" or id != "channykim1030":
      return redirect(url_for("index"))

    member = remote_db.get("member", id)
    login_user(member, remember=True)
    return redirect(url_for("index"))

  @app.route("/signin/callback")
  def callback():
    logger.debug("callback()")
    code = request.args.get("code")
    client = WebApplicationClient(oauth_credential["client_id"])

    token_endpoint = requests.get(GOOGLE_DISCOVERY_URL).json()["token_endpoint"]
    token_url, headers, body = client.prepare_token_request(token_endpoint, authorization_response=request.url, redirect_url=request.base_url, code=code)
    token_response = requests.post(token_url, headers=headers, data=body, auth=(oauth_credential["client_id"], oauth_credential["client_secret"]))
    client.parse_request_body_response(json.dumps(token_response.json()))
    userinfo_endpoint = requests.get(GOOGLE_DISCOVERY_URL).json()["userinfo_endpoint"]
    uri, headers, body = client.add_token(userinfo_endpoint)
    uri = uri.replace("http:", "https:")

    userinfo_response = requests.get(uri, headers=headers, data=body).json()
    member = remote_db.get("member", userinfo_response["email"].split('@')[0])

    login_user(member, remember=True)
    return redirect(url_for("index"))

  @app.route("/signout", methods=["POST", "GET"])
  def signout():
    logger.debug("signout()")
    logout_user()
    return redirect(url_for("index"))

  return app


if __name__ == "__main__":
  app = create_app()
  app.run()
