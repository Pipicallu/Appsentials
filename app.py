import os 
from flask import (
    Flask, flash, render_template, redirect,
    request, session, url_for) 
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

@app.route("/")
def hello():
    return "We are Halto we are awesome this is our app"

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            # debug must be set to False before deployment
            debug=True)