import os

from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, login_user, UserMixin, login_required, logout_user, current_user

from db import DB

app = Flask(__name__)
app.secret_key = "mysecretkey"

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


class User(UserMixin):
    pass


@login_manager.user_loader
def load_user(user_id):
    user = User()
    user.id = user_id
    return user


@app.route("/", methods=["GET", "POST"])
@login_required
def index():
    if request.method == "POST":
        person_name = request.form.get("name")  # Get the name from the form
        return render_template("index.html", person=person_name)
    return render_template("index.html", user=current_user)


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        db = DB()
        if db.get_user(username):
            return render_template("signup.html", message="User already exists!")
        # Create a new user
        user_id = db.create_user(username, password)
        user_login(user_id)
        return redirect(url_for("index"))
    return render_template("signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    db = DB()  # Assuming you have a database class
    message = None  # Initialize the message variable
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        # Fetch user details from the database
        user = db.get_user(username)
        if user is None:
            message = "User not found"
        elif user[2] != password: 
            message = "Incorrect password"
        else:
            user_login(user[0])
            return redirect(url_for("index"))
        
    return render_template("login.html", message=message, user=current_user)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))
            
def user_login(user_id):  
    user_obj = User()
    user_obj.id = user_id
    login_user(user_obj)

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        debug=True,
        ssl_context='adhoc',
    )
