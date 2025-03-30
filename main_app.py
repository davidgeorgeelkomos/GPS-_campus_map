import os

from flask import Flask, render_template, request

from db import DB

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        person_name = request.form.get("name")  # Get the name from the form
        return render_template("index.html", person=person_name)
    return render_template("index.html", person=None)


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
        return render_template("signup.html", message="User created successfully!")
    return render_template("signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    db = DB()  # Assuming you have a database class
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        # Example: Check against a hardcoded username and password
        if username == "admin" and password == "password123":
            return render_template("login.html", message="Login successful!")
        else:
            return render_template("login.html", message="Wrong username or password!")
    
    return render_template("login.html")

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        debug=True,
        ssl_context='adhoc',
    )
