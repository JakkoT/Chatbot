from flask import Flask, render_template, request, request, redirect, url_for
import Chatbot



app = Flask(__name__)

vastus = ["Chat History:", "  "]

@app.route("/dashboard", methods =["GET", "POST"])
def html():
   kustuta = False
   f = open("history.txt", "r")
   küs = "Hi"
   vastus = []
   if request.method == "POST":
      if "küs" in request.form:
         küs = request.form.get("küs")

      
   
   for i in f:
      vastus.append(i.strip())
   print(küs)
   Cvastus = Chatbot.vastus(küs)
   vastus.append(küs)
   vastus.append(Cvastus)
   f.close()
   f = open("history.txt","a")
   if request.method == "POST":
      if "kustuta" in request.form:
         print("kustuta")
         küs = []
   else:
      f.write(str(küs) + "\n")
      f.write(str(Cvastus) + "\n")
   f.close()



       
   return render_template("index.html", data=vastus)


@app.route('/del', methods =["GET", "POST"])
def kustuta():
   f = open("history.txt", "w")
   f.write("History: ")
   return render_template('index.html')

@app.route('/', methods=['POST', 'GET'])
def sisene():
   return render_template("sisene.html")

@app.route('/login', methods=['POST'])
def login():
    users = {"jakko" : "kristjan"}
    global username
    username = request.form['username']
    
    password = request.form['password']

    if username in users and users[username] == password:
        # Successful login, redirect to a dashboard or home page
        return redirect(url_for('html'))
    else:
        # Failed login, redirect back to the login page
        return redirect(url_for('sisene'))

