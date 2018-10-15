import re, os
from collections import Counter


from tkinter import Image
import text_to_image

"""
random text from 
http://www.randomtextgenerator.com/

Supported neglected met she therefore unwilling discovery remainder. Way sentiments two indulgence uncommonly own. Diminution to frequently sentiments he connection continuing indulgence. An my exquisite conveying up defective. Shameless see the tolerably how continued. She enable men twenty elinor points appear. Whose merry ten yet was men seven ought balls. 
Difficulty on insensible reasonable in. From as went he they. Preference themselves me as thoroughly partiality considered on in estimating. Middletons acceptance discovered projecting so is so or. In or attachment inquietude remarkably comparison at an. Is surrounded prosperous stimulated am me discretion expression. But truth being state can she china widow. Occasional preference fat remarkably now projecting uncommonly dissimilar. Sentiments projection particular companions interested do at my delightful. Listening newspaper in advantage frankness to concluded unwilling. 

"""


abc = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
       'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

ABC = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
       'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')


''' use true for encode and false for decode in method  encode_decode'''


def encode_decode(string, shift, boolean):
    ecoded_list = []
    for letter in list(string):
        if letter not in abc and letter not in ABC:
            ecoded_list.append(letter)
        else:
           if letter in abc:
               ecoded_list.append(abc[__get_index(abc.index(letter), shift, boolean)])
           else:
               ecoded_list.append(ABC[__get_index(ABC.index(letter), shift, boolean)])

    return ''.join(ecoded_list)


"""
 4 - E; A - 0; R - 17 
"""


def hack_caesar(string_from_front):
    standard_letters_index = (4, 0, 17)

    list_of_index = __get_list_of_popular(string_from_front)

    list_index_for_checking = []

    for index in list_of_index:
        for etalon_index in standard_letters_index:
            if index > etalon_index:
                list_index_for_checking.append(index - etalon_index)
            else:
                list_index_for_checking.append(len(abc) - (index - etalon_index))

    list_of_string_for_checking = []

    for index in list_index_for_checking:
        list_of_string_for_checking.append(encode_decode(string_from_front, index, False))

    return __get_the_best_variant(list_of_string_for_checking)


def __get_index(number, shift, boolean):
    if boolean:
        return (number + int(shift)) % len(abc)
    return number - (int(shift) % len(abc)) % len(abc)


def __get_the_best_variant(list_of_string_for_checking):
    etalon_words = [i.lower() for i in __get_list_of_string()]
    etalon_words = set(etalon_words)

    lower_case = [i.lower() for i in list_of_string_for_checking]

    list_of_max = []
    for string in lower_case:
        set_words = set(string.split())
        list_of_max.append(len(etalon_words.intersection(set_words)))

    if len(list_of_max) == 0:
        return "Sorry we could not decode that string"
    return list_of_string_for_checking[list_of_max.index(max(list_of_max))]


def __get_list_of_popular(string_from_front):
    regex = re.compile('[^a-zA-Z]')
    list_of_letters_without_space = regex.sub('', string_from_front)
    list_of_the_most_popular = [Counter(list_of_letters_without_space).most_common()[0][0],
                                Counter(list_of_letters_without_space).most_common()[1][0]]
    list_of_index = []

    for letter in list_of_the_most_popular:
        if letter in ABC:
            list_of_index.append(ABC.index(letter))
        elif letter in abc:
            list_of_index.append(abc.index(letter))
    return list_of_index


def __get_list_of_string():
    list = []
    try:
        with open('./static/words') as fp:
            line = fp.readline()
            while line:
                list.append(line.strip())
                line = fp.readline()
    finally:
        fp.close()
    return list


def append_filename(filename):
    return "{0}_{2}.{1}".format(*filename.rsplit('.', 1) + ["for_decode"])


def encode_text_to_picture(file, text):
    encoded = file.copy()
    width, height = file.size
    length = len(text)
    index = 0
    for row in range(height):
        for col in range(width):
            r, g, b = file.getpixel((col, row))
            # first value is length of msg
            if row == 0 and col == 0 and index < length:
                asc = length
            elif index <= length:
                c = text[index - 1]
                asc = ord(c)
            else:
                asc = r
            encoded.putpixel((col, row), (asc, g, b))
            index += 1
    return encoded



def decode_text_to_picture(file):
    width, height = file.size
    msg = ""
    index = 0
    for row in range(height):
        for col in range(width):
            try:
                r, g, b = file.getpixel((col, row))
            except ValueError:
                # need to add transparency a for some .png files
                r, g, b, a = file.getpixel((col, row))
            # first pixel r value is length of message
            if row == 0 and col == 0:
                length = r
            elif index <= length:
                msg += chr(r)
            index += 1
    return msg