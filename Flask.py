from flask import Flask, render_template, request, redirect, url_for
import Chatbot
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user


app = Flask(__name__)
app.config['SECRET_KEY'] = 'jakko.kristjan.key'


login_manager = LoginManager(app)
login_manager.login_view = 'login'


users = {
    'jakko': {'password': 'jakko', 'dashboard_content': 'Dashboard for jakko'},
    'kristjan': {'password': 'kristjan', 'dashboard_content': 'Dashboard for kristjan'}
}

# User class for Flask-Login
class User(UserMixin):
    pass

@login_manager.user_loader
def load_user(user_id):
    if user_id in users:
        user = User()
        user.id = user_id
        return user
    return None

vastus = ["Chat History:", "  "]


@app.route('/del', methods =["GET", "POST"])
def kustuta():
   f = open(f"history{username}.txt", "w")
   f.write("History: ")
   return render_template('index.html')

@app.route('/', methods=['POST', 'GET'])
def sisene():
   return render_template("sisene.html")



# Default route - Login Page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username in users and users[username]['password'] == password:
            user = User()
            user.id = username
            login_user(user)
            return redirect(url_for('html', username=username))
    
    return render_template('sisene.html')

# Dashboard route - Only accessible after login
@app.route('/dashboard/<username>', methods=['POST', 'GET'])
@login_required
def html(username):
    if username == current_user.id:
      
      user_data = users[username]

      kustuta = False
      f = open(f"history{username}.txt", "a")
      f.close()
      f = open(f"history{username}.txt", "r")
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
      f = open(f"history{username}.txt","a")
      if request.method == "POST":
         if "kustuta" in request.form:
            print("kustuta")
            küs = []
      else:
         f.write(str(küs) + "\n")
         f.write(str(Cvastus) + "\n")
      f.close()

      return render_template("index.html", username=username, data=vastus, content=user_data['dashboard_content'])

    else:
        return redirect(url_for('login'))

# Logout route
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))