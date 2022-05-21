from bruteforce import *

# 3 
# ciphertext = """Kdyh qr grxew wkdw wkhvh srolflhv zrxog kdyh d surirxqg lpsdfw rq fklog khdowk. Dgyhuwlvlqj uhvwulfwlrqv zrun. D uhfhqw shhu-uhylhzhg vwxgb eb wkh Orqgrq Vfkrro ri Kbjlhqh & Wurslfdo Phglflqh vkrzhg wkdw wkdqnv wr wkh pdbru ri Orqgrq'v mxqn irrg dgyhuwlvlqj uhvwulfwlrqv rq wkh fdslwdo'v exvhv dqg wxeh wudlqv, idplolhv duh qrz exblqj 1,000 ihzhu fdorulhv d zhhn iurp irrg wkdw lv kljk lq idw, vdow dqg vxjdu."""

# 5
# ciphertext = """Ymj mtwwtwx tk Mnwtxmnrf fsi Sflfxfpn rfij ymj bmtqj btwqi fkwfni tk ymj fytrnh gtrg - jajs ymtxj bmt rnlmy qfzshm tsj. Ytifd ymfy kjfw mfx rtxyqd ufxxji tzy tk qnansl rjrtwd, fsi bnym ny bj rfd mfaj qtxy f hwzhnfq xfkjlzfwi, Ifsnjq Nrrjwbfmw, fxxthnfyj uwtkjxxtw tk mnxytwd fy Stwymbjxyjws Zsnajwxnyd, bwnyjx."""

# 13
# ciphertext = """Fgbaruratr vf gubhtug gb unir orra ohvyg nebhaq 2,500OP, jvgu rivqrapr fhttrfgvat gur ohvyqref jrer ubhfrq ng n frggyrzrag xabja nf Qheevatgba Jnyyf, nobhg 2 zvyrf njnl. Gur fvgr jnf cerqbzvanagyl bpphcvrq va gur jvagre zbaguf, naq nccrnef gb unir orra hfrq sbe orgjrra 10 gb 50 lrnef."""

# 16
# ciphertext = """Jxu hyiydw sqiubeqt qdt q bqsa ev cutysqb huiekhsui qdt lqssydui xqi but jxu KD xkcqd hywxji qwudso je mqhd ev “tulqijqjydw” sediugkudsui veh Dehjx Aehuq'i 25 cybbyed fuefbu, qdt Mehbt Xuqbjx Ehwqdypqjyed evvysyqbi mehho qd kdsxusaut ifhuqt sekbt wylu hyiu je tuqtbyuh dum lqhyqdji."""

# 23
# ciphertext = """Qeb fjmloqxkzb lc qlrze zxjb fkql clzrp qtl vbxop xdl xp qeb tloia zlmba tfqe qeb fplixqflk fjmlpba yv ZLSFA-19. Jlkqep pmbkq xslfafkd exkapexhbp xka erdp clo cbxo lc xk fkcbzqflrp afpbxpb lkiv obfkclozba elt bppbkqfxi qebpb zlkkbzqflkp xob clo lro lsboxii ebxiqe. """

# 26
# ciphertext = """We humans rely on a suite of cues to recognize our friends, such as their smiles, their voices, or the way they walk. Biologists have known for several decades that dolphins form close friendships, and that the cetaceans identify pals by their unique whistles. Now new surprising research suggests bottlenose dolphins use their sense of taste to discern their friends' urine from unrelated dolphins."""

# 2
# ciphertext = """Ogumk vkfcm ngdkj fctk ugdwcj cnktcp mgekn, Twdkeqp ogoknkmk ctvk rgpvkpipac dcik Tqocyk. Uwpick kpk ogpcpfck rgtdcvcucp tguok cpvctc Kvcnkc fcp Ekucnrkpg Icwn, ykncacj ugncvcp Rgiwpwpicp Cnrgp acpi fkrgtkpvcj qngj Ecguct.""" 

# 24
# ciphertext = """Npyhspgrlwy kclhybg qyiqg zyeygkyly Aycqyp kcleyqyf icrcpykngjyllwy qczyeyg yfjg qrpyrceg kgjgrcp byl nmjgrgi, qcpry kclyijsiiyl Eysj. Aycqyp kckncpjsyq zyryq Pcnszjgi Pmkyug qchysf Pfglc byl qcnylhyle uyirs kclmnyle ncleypsflwy ickzyjg bg Pmkyug."""

ciphertext = input("Enter your ciphertext: ")
print()

print("Ciphertext                   :")
print(ciphertext + "\n")

decipheredCiphertext = bruteforce_caesar(ciphertext)
print("Deciphered Ciphertext        :")
print(decipheredCiphertext + "\n")