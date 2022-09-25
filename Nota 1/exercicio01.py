# Homework 01: Criptografia de Fluxo
def encode(word, key):
    result = []
    for i in word:
        letter = ord(i)
        temp = (letter+key)
        if (temp<=90 or temp<=122):
            result.append(chr(letter + key))
        else:
            result.append(chr((letter-26) + key))
                        
    return (''.join(map(str, result)))

key = int(input('Entre com a chave entre 1 e 26: '))
word = list(input('Entre com a palavra a ser codificada: '))

print('Palavra codificada: ', encode(word, key))