# from PIL import Image

import PIL.Image



# from tkinter import Image

from werkzeug.utils import secure_filename

from app import app
from .caesar import *
from flask import render_template, request, flash, redirect

UPLOAD_FOLDER = "./static/upload"

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


@app.route('/second_encode', methods=['POST'])
def second_page_encode_post():
    if request.form['form'] == 'Encode file':
        upload_file = request.files['file']

        if upload_file.filename == '':
            result = "File not has been chosen"
            return render_template('secondLab.html', first_page="/index", second_page="",
                                   shift_encode=1, shift_decode=1, not_active="btn btn-primary my-2",
                                   active="btn btn-secondary my-2", result=result)

        if not request.form['text_encode']:
            result = "No text entered"
            return render_template('secondLab.html', first_page="/index", second_page="",
                                   shift_encode=1, shift_decode=1, not_active="btn btn-primary my-2",
                                   active="btn btn-secondary my-2", result=result)

        text_encode = request.form['text_encode']

        if len(text_encode) > 255:
            result = "text too long! (don't exceed 255 characters)"
            return render_template('secondLab.html', first_page="/index", second_page="",
                                   shift_encode=1, shift_decode=1, not_active="btn btn-primary my-2",
                                   active="btn btn-secondary my-2", result=result)

        filename = secure_filename(upload_file.filename)
        # path_to_new_file = os.path.join(UPLOAD_FOLDER, append_filename(filename))
        path_to_new_file = os.path.join(UPLOAD_FOLDER, filename)
        upload_file.save(path_to_new_file)

        image = PIL.Image.open(path_to_new_file)
        image = image.convert('RGB')

        if image.mode != 'RGB':
            result = "image mode needs to be RGB"
            return render_template('secondLab.html', first_page="/index", second_page="",
                                   shift_encode=1, shift_decode=1, not_active="btn btn-primary my-2",
                                   active="btn btn-secondary my-2", result=result)

        img_encoded = encode_text_to_picture(image, text_encode)
        os.remove(path_to_new_file)
        img_encoded.save(path_to_new_file)

        result = "operation decode text to image was executed successfully"

    return render_template('secondLab.html', first_page="/index", second_page="",
                           shift_encode=1, shift_decode=1, not_active="btn btn-primary my-2",
                           active="btn btn-secondary my-2", result=result)


@app.route('/second_decode', methods=['POST'])
def second_page_decode_post():

    if request.form['form'] == 'Decode file':
        file = request.files['file']

        if file.filename == '':
            result = "File not has been chosen"
            return render_template('secondLab.html', first_page="/index", second_page="",
                                   shift_encode=1, shift_decode=1, not_active="btn btn-primary my-2",
                                   active="btn btn-secondary my-2", result=result)

        filename = secure_filename(file.filename)
        path_to_file = os.path.join(UPLOAD_FOLDER, filename)
        image = PIL.Image.open(path_to_file)
        image = image.convert('RGB')
        decoded_text = decode_text_to_picture(image)
        result = "operation decode text to image was executed successfully"

    return render_template('secondLab_decode.html', first_page="/index", second_page="",
                           shift_encode=1, shift_decode=1, not_active="btn btn-primary my-2",
                           active="btn btn-secondary my-2", text_decode=decoded_text, result=result)
