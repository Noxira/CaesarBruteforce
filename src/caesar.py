from typing import List

def do_caesar(text: str, shift: int) -> str:
    if(shift == 0):
        return text

    result = ""
    for char in text:
        newAscii = ord(char) + shift
        if (newAscii > 90 and ord(char) < 91): # capital letter loopback
            newAscii -= 26
        elif (newAscii > 122 and ord(char) < 123): # noncapital letter loopback
            newAscii -= 26
        if ((ord(char) < 65) or (ord(char) > 90 and ord(char) < 97) or (ord(char) > 122)): # nonletter ignore
            newAscii = ord(char)
        result += chr(newAscii)
    return result

def arr_do_caesar(texts: List[str], shift: int) -> List[str]:    
    result = []
    for text in texts:
        result.append(do_caesar(text, shift))
    return result

# print(arr_do_caesar(["THE", "TEH"], 5))