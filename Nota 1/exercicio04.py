import numpy as np

# Homework 04: Cifragem por Substituição
alphabet_code = {'a':'Z', 'b':2, 'c':'x', 'd':'g', 'e':4, 'f':9, 'g':7, 'h':8,
                 'i':'v', 'j':'C', 'k':'l', 'l':5, 'm':1, 'n':9, 'o':'P', 'p':0,
                 'q':'C', 'r':'D', 's':3, 't':'N', 'u':'F', 'v':6, 'w':'H',
                 'x':'Q', 'y':'O', 'z':'r', 'A':'Z', 'B':2, 'C':'x', 'D':'g',
                 'E':4, 'F':9, 'G':7, 'H':8, 'I':'v', 'J':'C', 'K':'l', 'L':5,
                 'M':1, 'N':9, 'O':'P', 'P':0, 'Q':'C', 'R':'D', 'S':3, 'T':'N',
                 'U':'F', 'V':6, 'W':'H', 'X':'Q', 'Y':'O', 'Z':'r', 'ç': 'B',
                 'Ç':'B'}

def encode(word):
    result = []
    for i in word:
       result.append(alphabet_code.get(i, '-'))
    return np.array(''.join(map(str, result)))

word = list(input('Entre com a palavra a ser codificada: '))
print('Palavra codificada:', encode(word))