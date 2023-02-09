from flask import Flask, render_template,request
from twilio.rest import Client

account_sid = "AC34f33fdcfc43f629aa4060df13917bbb"
auth_token = "16e1eedfbd31e31e0b83315bc57ab5aa"

client = Client(account_sid, auth_token)

app=Flask(__name__,template_folder="docs")
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/skills")
def skills():
    return render_template("skills.html")

@app.route("/contact",methods=["POST","GET"])
def contact():
    if request.method=="POST":
        name=request.form['fname']
        email=request.form['femail']
        message=request.form['fmessage']
        print(f"{request.form['fname']}\n"
              f"{request.form['femail']}\n"  # == Html de /name/
              f"{request.form['fmessage']}\n")
        message = client.messages.create(body=f"Sender:{name}\n"
                                              f"Email:{email}\n"
                                              f"Message:{message}\n", from_="+18176703523", to="+905454699907")
    return render_template("contact.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

if __name__ == "__main__":
    app.run(debug=True)
