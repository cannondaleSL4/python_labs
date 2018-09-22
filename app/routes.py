from app import app
from .caesar import *
from flask import render_template, request



@app.route('/')
@app.route('/index')
def index_page():
    return render_template('index.html', first_page="", second_page="/second_encode",
                           shift_encode=1, shift_decode=1, active="btn btn-primary my-2", not_active="btn btn-secondary my-2")


@app.route('/second_encode')
def second_page_encode():
    return render_template('secondLab.html', first_page="/index", second_page="",
                           shift_encode=1, shift_decode=1, not_active="btn btn-primary my-2",
                           active="btn btn-secondary my-2")


@app.route('/second_decode')
def second_page_decode():
    return render_template('secondLab_decode.html', first_page="/index", second_page="",
                           shift_encode=1, shift_decode=1, not_active="btn btn-primary my-2",
                           active="btn btn-secondary my-2")


@app.route('/', methods=['POST'])
@app.route('/index', methods=['POST'])
def index_post():
    if request.form['form'] == 'Encode':
        shift_encode = request.form['shift_encode']
        text_encode = request.form['text_encode']

        if not shift_encode or not text_encode:
            result = "you should set text for encode also is shift letters in ABC"
            return render_template("index.html", result=result)
        text_encoded = encode_decode(text_encode, shift_encode, True)
        result = "has been executed operation encode with shift {}".format(shift_encode)
        return render_template("index.html", result=result, text_decode=text_encoded, shift_decode=shift_encode)
    elif request.form['form'] == 'Decode':
        shift_decode = request.form['shift_decode']
        text_decode = request.form['text_decode']

        if not shift_decode or not text_decode:
            result = "you should set text for decode also is shift letters in ABC"
            return render_template("index.html", result=result)
        text_decoded = encode_decode(text_decode, shift_decode, False)
        result = "has been executed operation decode with shift {}".format(shift_decode)
        return render_template("index.html", result=result, text_encode=text_decoded, shift_encode=shift_decode)
    elif request.form['form'] == 'Hack':
        text_decode = request.form['text_decode']

        if not text_decode:
            result = "you should set text for decode "
            return render_template("index.html", result=result)

        text_decoded = hack_caesar(text_decode)
        result = "has been executed operation hacking "
        return render_template("index.html", result=result, text_encode=text_decoded)
