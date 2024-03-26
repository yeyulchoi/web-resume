from flask import Flask, render_template, request, redirect, url_for, flash
import smtplib
from flask_mail import Mail, Message
import os
import secrets


app = Flask(__name__)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True
app.config['MAIL_USERNAME']='yeyulchoi@gmail.com'  #os.environ.get('FLASK_MAIL_USER_EMAIL')
app.config['MAIL_PASSWORD']='crlr kkkp wkbx xbpw'  #os.environ.get('FLASK_MAIL_USER_PASSWORD')
mail = Mail(app)


app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:''@localhost/flask_aws2'
app.config['SQLALCHEMY_TRACK_MODIFICATION']=False
app.config['SECRET_KEY']=secrets.token_hex(16)


@app.route('/', methods=['GET','POST'])
def home():
    if request.method =='POST':
        msg =Message(
            "This is from flask-resume-app",
            sender='noreply@demo.com',
            recipients=['yeyulchoi@gmail.com','yeyulchoi@outlook.com'])
        msg.body =" Hey, How are you. I just clicked your email on the resume!!"
        mail.send(msg)
        redirect('index.html')
    return render_template('index.html')




if __name__ =='__main__':
    with app.app_context():
         app.run(debug=True)