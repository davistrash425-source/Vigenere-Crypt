from cypher import vigenere_cypher

plain_text = input( "Enter text to be cyphered: " )
key = input( "Enter key: " )

print ( vigenere_cypher(plain_text, key) )