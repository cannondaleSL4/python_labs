from app import app
from .caesar import *
from flask import render_template, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField



@app.route('/')
@app.route('/index')
def index_page():
    return render_template('index.html')

# class ReusableForm(Form):
#     name = TextField('Name:', validators=[validators.required()])


@app.route('/', methods=['POST'])
@app.route('/index', methods=['POST'])
def index_post():
    shift_encode = request.form['shift_encode']
    # encode_text = request.form['encode_text']
    # print(shift_encode + " " + encode_text)
    return render_template("index.html")
