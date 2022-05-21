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
    for i in range(25):
        occurence_list.append(get_occurence(dict, sanitize_sentence(ciphertext)))
        dict = arr_do_caesar(dict, 1)

    mostLikelyShift = occurence_list.index(max(occurence_list))
    mostLikelyDecryptionKey = (26 - mostLikelyShift) % 26
    mostLikelyDecipheredText = do_caesar(ciphertext , mostLikelyDecryptionKey)
    print("Time taken                   : " + str(int((time.time() - start_time) * 1000)) + "ms")
    print("Most likely encryption key   : " + str(mostLikelyShift))

    return mostLikelyDecipheredText