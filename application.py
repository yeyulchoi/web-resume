from flask import Flask, abort, render_template, request, redirect, url_for, flash, send_file, jsonify
import os
from werkzeug.utils import secure_filename
from datetime import datetime
import smtplib
import secrets
from flask_wtf import FlaskForm
from flask_mail import Mail, Message


application = Flask(__name__)


# <<config for email notification>>
application.config['MAIL_SERVER']='smtp.gmail.com'
application.config['MAIL_PORT']=465
application.config['MAIL_USE_TLS']=False
application.config['MAIL_USE_SSL']=True
application.config['MAIL_USERNAME']='yeyulchoi@gmail.com'  #os.environ.get('FLASK_MAIL_USER_EMAIL')
application.config['MAIL_PASSWORD']='crlr kkkp wkbx xbpw'  #os.environ.get('FLASK_MAIL_USER_PASSWORD')
mail = Mail(application)
# app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///flaskaws.db'

application.config['SQLALCHEMY_DATABASE_URI']='mysql://root:''@localhost/flask_aws2'
application.config['SQLALCHEMY_TRACK_MODIFICATION']=False
application.config['SECRET_KEY']=secrets.token_hex(16)


class Location:
    def __init__(self, key, addr,lat, lng):
        self.key = key
        self.addr = addr
        self.lat =lat
        self.lng =lng

loc_obj = Location('house','53 Willesden Rd, Toronto, ON M2H 1V5',43.793573115460475, -79.36569236094664)






@application.route('/', methods=['GET','POST'])
def home():
    if request.method =='POST':
        msg =Message(
            "This is from flask-resume-app",
            sender='noreply@demo.com',
            recipients=['yeyulchoi@outlook.com'])
        msg.body ="Your friend visited your web resume!!"
        mail.send(msg) 
        return redirect(url_for('home'))        
    return render_template('index.html',mykey=loc_obj.key, myplace=loc_obj.addr)

@application.route('/cover')
def coverletter():  
    now= datetime.now()
    month=now.strftime('%B')
    day=now.strftime('%d')
    year = now.strftime('%Y')   
    return render_template('coverltr.html', month=month, day=day, year=year)

@application.route('/<loc_key>')
def show_place(loc_key):
    return render_template('map.html', myplace_two =loc_obj.addr,latitude=loc_obj.lat, longitude=loc_obj.lng)

@application.route('/download')
def download():
    path = 'files/resume.pdf'
    return send_file(path, as_attachment=True)

if __name__ =='__main__':
    with application.app_context():
         application.run(debug=True)