from bruteforce import *

ciphertext = """Ymj mtwwtwx tk Mnwtxmnrf fsi Sflfxfpn rfij ymj bmtqj btwqi fkwfni tk ymj fytrnh gtrg - jajs ymtxj bmt rnlmy qfzshm tsj. Ytifd ymfy kjfw mfx rtxyqd ufxxji tzy tk qnansl rjrtwd, fsi bnym ny bj rfd mfaj qtxy f hwzhnfq xfkjlzfwi, Ifsnjq Nrrjwbfmw, fxxthnfyj uwtkjxxtw tk mnxytwd fy Stwymbjxyjws Zsnajwxnyd, bwnyjx."""

print("Ciphertext               :")
print(ciphertext + "\n")

decipheredCiphertext = bruteforce_caesar(ciphertext)
print("Deciphered Ciphertext    :")
print(decipheredCiphertext + "\n")