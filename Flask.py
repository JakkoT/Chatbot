from flask import Flask, render_template, request
import Chatbot



app = Flask(__name__)

vastus = ["Chat History:", "  "]

@app.route("/", methods =["GET", "POST"])
def html():
   f = open("history.txt", "r")
   küs = "Hi"
   vastus = ["Sinu, Ajalugu"]
   if request.method == "POST":
      küs = request.form.get("küs")
   for i in f:
      vastus.append(i.strip())
   Cvastus = Chatbot.vastus(küs)
   vastus.append(küs)
   vastus.append(Cvastus)
   f.close()
   f = open("history.txt","a")
   f.write(str(küs) + "\n")
   f.write(str(Cvastus) + "\n")
   f.close()


       
   return render_template("index.html", data=vastus)