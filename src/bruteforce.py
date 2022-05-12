from typing import List
from caesar import *
from file_reader import *
import re
import time

def get_occurence(dict: List[str], text: str) -> int:
    occurence = 0
    for word in dict:
        exp = "\\b" + word + "\\b"
        occurence += len(re.findall(exp, text))
    return occurence

def bruteforce_caesar(ciphertext):
    dict = get_dict()
    occurence_list = []
    
    start_time = time.time()
    for shift in range(26):
        occurence_list.append(get_occurence(arr_do_caesar(dict, shift), sanitize_sentence(ciphertext)))

    mostLikelyShift = occurence_list.index(max(occurence_list))
    mostLikelyKey = (26 - mostLikelyShift) % 26
    mostLikelyDecipheredText = do_caesar(ciphertext , mostLikelyKey)
    print("Time taken               : " + str(int((time.time() - start_time) * 1000)) + "ms")
    print("Most likely key          : " + str(mostLikelyKey))

    return mostLikelyDecipheredText