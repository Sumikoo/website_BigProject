from application import app
from application import *
from flask import render_template, request, redirect, url_for, session, jsonify
import datetime

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")
