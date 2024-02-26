from flask import Flask, render_template, redirect, url_for, request
from markupsafe import Markup
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
Bootstrap5(app)

@app.route("/")
def base():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/get-a-quote")
def quote():
    return render_template("get-a-quote.html")

if __name__ == "__main__":
    app.run(debug=True)