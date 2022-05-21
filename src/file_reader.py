import os

def get_file(): 
    dict_file = open("C:/Lenovo Temp/IF Files/Sem4/Stima/Makalah/CaesarBruteforce/src/assets/dictionary.txt", 'r') # change file name if necessary
    return dict_file

def sanitize_sentence(sentence):
    return sentence.upper().replace('\'', '')

def get_dict():
    dict_file = get_file()
    words = []
    for line in dict_file:
        words.append(sanitize_sentence(line.strip()))
    return words