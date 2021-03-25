from flask import Flask, render_template, request, flash
import json
# from flask_mail import Mail
import smtplib

with open("config.json", "r")as c:
    params=json.load(c)["params"]

def sendEmail(content):
    server=smtplib.SMTP('smtp.gmail.com', '587')
    server.ehlo()
    server.starttls()
    server.login(params['username'], params['password'])
    server.sendmail(params['username'], params['receiver_email'], content)
    server.close()
    
    

app=Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html", params=params)

    
@app.route("/about")
def about():
    return render_template("about.html", params=params)
@app.route("/contact")
def contact():
    return render_template("contact.html",params=params)

@app.route("/resume")
def resume():
    return render_template("resume.html", params=params)

@app.route("/services")
def services():
    return render_template("services.html", params=params)

@app.route("/portfolio_details")
def portfolio_details():
    return render_template("portfolio-details.html", params=params)
@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html", params=params)

@app.route("/msgsent", methods=['GET', 'POST'])
def msgsent():
    name=request.form.get('name')
    email=request.form.get('email')
    subject=request.form.get('subject')
    message=request.form.get('message')
    msg=f'Subject: {subject}\n\nName:{name}\n\nEmail: {email}\n\nMessage: {message}'
    sendEmail(msg)
    # flash(u'Invalid password provided', 'error')
    return render_template("index.html",params=params)


    
if __name__ == '__main__':
    app.run(debug=True)