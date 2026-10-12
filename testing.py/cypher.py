import numpy as np

def make_table():
    vi_table = np.zeros((26, 26), dtype=str)   # 26 rows × 26 columns of zeros

    alphabet = []
    for i in range(26):
        alphabet.append( chr( i + ord("A") ) )

    for i in range(26):
        # i represents the index of the row starting at 0 - 25
        start = i
        for j in range(26): # repeat 26 times
            vi_table[i][j] = alphabet[start]
            start += 1
            if start >= 26:
                start = 0

    return vi_table

def find_keyword_letter( text, key, index ):
    text = text.replace(" ","")

    key_index = index%len(key)

    return key[key_index]


def find_cypher_letter( text, key, index ):
    table = make_table()

    plain_text_letter = text[index]
    keyword_letter = find_keyword_letter( text, key, index )

    return table[ord(keyword_letter) - ord("A")][ord(plain_text_letter) - ord("A")]


def vigenere_cypher( text, key ):
    cypher = ""
    key = key.upper().replace(" ","")
    text = text.upper().replace(" ","")

    for i in range(len(text)):
        cypher += find_cypher_letter( text, key, i )

    return cypher
