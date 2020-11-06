import requests
import json
import pyrebase
import sys, os
import ssl
import os
import time
from flask import Flask, render_template, url_for, request, session, redirect
from oauthlib.oauth2 import WebApplicationClient
from api import get_students, get_problems, hide_unsolved
from user import User
from flask_login import (
    LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user,
)

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY") or os.urandom(24)

# User session management setup
# https://flask-login.readthedocs.io/en/latest
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

firebaseConfig = {
  "apiKey": "AIzaSyAIu3NQa8hdg_STYi65vGSIHkd3g-nkxp0",
  "authDomain": "seansdevnote-d14de.firebaseapp.com",
  "databaseURL": "https://seansdevnote-d14de.firebaseio.com",
  "projectId": "seansdevnote",
  "storageBucket": "seansdevnote.appspot.com",
  "messagingSenderId": "576471339248",
  "appId": "1:576471339248:web:9e28d0cc8815522a693235"
}
firebase = pyrebase.initialize_app(firebaseConfig)
auth=firebase.auth()


GOOGLE_CLIENT_ID = "576471339248-pjaq07ir9esv1ql5hiaci66qoivgcm6r.apps.googleusercontent.com"
GOOGLE_CLIENT_SECRET ="mTMTs9KRoAvSQ55Eqe636Irz"
GOOGLE_DISCOVERY_URL = (
    "https://accounts.google.com/.well-known/openid-configuration"
)
client = WebApplicationClient(GOOGLE_CLIENT_ID)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", posts={})
    
@app.route("/admin", methods=["POST", "GET"])
def admin():
    if request.method == 'POST':
        return render_template("admin.html", students=get_students(to_html=True, name=request.form["nm"]))
    else:
        return render_template("admin.html")

@app.route("/premium", methods=["GET"])
def premium():
    return render_template("premium.html")

@app.route("/python", methods=["GET"])
def python():
    with open("data/python.json", "r") as read_file:
        data = json.load(read_file)
        subpage = request.args.get('subpage', "")
        if subpage:
            posts = data["posts"][subpage]
            if subpage in ["Algorithm", "Syntax"]:
                posts = hide_unsolved(posts, session.get("solved", []))
        else:
            posts = data["posts"]
    return render_template("index.html", posts=posts)

@app.route("/terminal", methods=["GET"])
def terminal():
    with open("data/terminal.json", "r") as read_file:
        data = json.load(read_file)
        posts = data["posts"]
    return render_template("index.html", posts=posts)

@app.route("/signin", methods=["POST", "GET"])
def signin():
    authorization_endpoint = requests.get(GOOGLE_DISCOVERY_URL).json()["authorization_endpoint"]

    request_uri = client.prepare_request_uri(
        authorization_endpoint,
        redirect_uri=request.base_url + "/callback",
        scope=["openid", "email", "profile"],
    )

    return redirect(request_uri)

@app.route("/signin/callback")
def callback():
    code = request.args.get("code")

    token_endpoint = requests.get(GOOGLE_DISCOVERY_URL).json()["token_endpoint"]
    token_url, headers, body = client.prepare_token_request(
        token_endpoint,
        authorization_response=request.url,
        redirect_url=request.base_url,
        code=code
    )
    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET),
    )
    client.parse_request_body_response(json.dumps(token_response.json()))
    userinfo_endpoint = requests.get(GOOGLE_DISCOVERY_URL).json()["userinfo_endpoint"]
    uri, headers, body = client.add_token(userinfo_endpoint)
    userinfo_response = requests.get(uri, headers=headers, data=body).json()

    user = User(userinfo_response["sub"], name = userinfo_response["name"])
    login_user(user)
    if not user.solved:
        session["id"] = user["id"]
        return redirect(url_for("singup.html"))
    session['name'] = user.name
    session['solved'] = user.solved
    return redirect(url_for("index"))


@app.route("/signout", methods=["POST", "GET"])
def signout():
    logout_user()
    return redirect(url_for("index"))

if __name__ == "__main__":
    #fb_auth.create_user_with_email_and_password("rbtmd1010@gmail.com", "Ghkdrb12@s")
    #fb_auth.sign_in_with_email_and_password("rbtmd1010@gmail.com", "Ghkdrb12@s")
    app.run(debug=True, port=8100, ssl_context=('server.crt', 'server.key'))
    #ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS)
    #ssl_context.load_cert_chain(certfile='newcert.pem', keyfile='newkey.pem', password='secret')
    #app.run(host="0.0.0.0", port=4443, ssl_context=ssl_context)

