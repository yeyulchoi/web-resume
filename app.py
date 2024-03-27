from flask import Flask, abort, render_template, request, redirect, url_for, flash
import smtplib
from flask_mail import Mail, Message  
import os
import secrets


app = Flask(__name__)
# <<config for email notification>>
# app.config['MAIL_SERVER']='smtp.gmail.com'
# app.config['MAIL_PORT']=465
# app.config['MAIL_USE_TLS']=False
# app.config['MAIL_USE_SSL']=True
# app.config['MAIL_USERNAME']='yeyulchoi@gmail.com'  #os.environ.get('FLASK_MAIL_USER_EMAIL')
# app.config['MAIL_PASSWORD']='crlr kkkp wkbx xbpw'  #os.environ.get('FLASK_MAIL_USER_PASSWORD')
# mail = Mail(app)
# app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///flaskaws.db'
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:''@localhost/flask_aws2'
app.config['SQLALCHEMY_TRACK_MODIFICATION']=False
app.config['SECRET_KEY']=secrets.token_hex(16)


class Location:
    def __init__(self, key, addr,lat, lng):
        self.key = key
        self.addr = addr
        self.lat =lat
        self.lng =lng

loc_obj = Location('house','53 Wilresden',43.793573115460475, -79.36569236094664)


@app.route('/', methods=['GET','POST'])
def home():
    # if request.method =='POST':
    #     msg =Message(
    #         "This is from flask-resume-app",
    #         sender='noreply@demo.com',
    #         recipients=['yeyulchoi@gmail.com','yeyulchoi@outlook.com'])
    #     msg.body =" Hey, How are you. I just clicked your email on the resume!!"
    #     mail.send(msg)
    #     redirect('index.html')
    return render_template('index.html',mykey=loc_obj.key, myplace=loc_obj.addr)

@app.route('/cover')
def cover_ltr():
    return render_template('coverltr.html')

@app.route('/<loc_key>')
def show_place(loc_key):
    return render_template('map.html', myplace_two =loc_obj.addr,latitude=loc_obj.lat, longitude=loc_obj.lng)


if __name__ =='__main__':
    with app.app_context():
         app.run(debug=True)