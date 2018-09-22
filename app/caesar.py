
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


def __get_index(number, shift, boolean):
    if boolean:
        return (number + int(shift)) % len(abc)
    return number - (shift % len(abc)) % len(abc)
