from flask import Flask, render_template, make_response
import os
import time
import pyrebase

app = Flask(__name__)
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
#db=firebase.database()
auth=firebase.auth()
auth.create_user_with_email_and_password("rbtmd1010@gmail.com", "rbtmd1")
auth.sign_in_with_email_and_password("rbtmd1010@gmail.com", "rbtmd1")

@app.route('/')
def index():
    context = { 'server_time': time.strftime("%I:%M:%S %p", time.localtime()) }
    template = render_template('index.html', context=context)
    response = make_response(template)
    response.headers['Cache-Control'] = 'public, max-age=300, s-maxage=600'
    return response

def signin():
    template = render_template('machine_learning.html')
    return template

if __name__ == '__main__':
    pass
    #app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))