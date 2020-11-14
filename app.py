import os 
from flask import (
    Flask, flash, render_template, redirect,
    request, session, url_for) 
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

