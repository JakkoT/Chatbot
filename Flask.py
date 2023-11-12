from flask import Flask, render_template, request
import Chatbot



app = Flask(__name__)

vastus = ""


@app.route("/", methods =["GET", "POST"])
def html():
    vastus = ""
    if request.method == "POST":
       küs = request.form.get("küs")
       vastus = Chatbot.vastus(küs)
    return render_template("index.html", data=vastus)