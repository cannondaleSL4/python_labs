from app import app
from .caesar import *
from flask import render_template, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField



@app.route('/')
@app.route('/index')
def index_page():
    encode_shift = 1
    decode_shift = 1
    return render_template('index.html', encode_shift=encode_shift, decode_shift=decode_shift)


@app.route('/', methods=['POST'])
@app.route('/index', methods=['POST'])
def index_post():
    shift_encode = request.form['shift_encode']
    encode_text = request.form['encode_text']

    if not shift_encode or not encode_text:
        result = "you should set text for encode also is shift letters in ABC"
        return render_template("index.html", result=result)
    text_encoded = encode_decode(encode_text, shift_encode, True)
    result = "has been executed operation encode with shift {}".format(shift_encode)
    return render_template("index.html", result=result, decode_text=text_encoded, decode_shift=shift_encode)
