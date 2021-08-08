# Raul Cervantes 77825705 Alexis Padilla 36931764. ICS Lab sec 3. Lab asst 6.


print()
print('--part c1--')
def contains(x: str, y: str) -> bool:
    '''Checks if the second string is inside of the first string'''
    return y in x

print(contains('speed', 'pee'))
print(contains('car', 'no'))

assert contains('banana', 'ana')
assert not contains('racecar', 'ck')

print()
print('--part c2--')
def sentence_stats(x: str):
    '''Takes in a string and analyzes the string'''
    print ('Characters: ', len(x))
    print ('Words: ', len(x.split()))
    letters = 0
    for w in x.split():
        letters += len(w)
    print ('Average word length: ', letters / len(x.split()))

sentence_stats('I love UCI')

print()
print('--part c3--')
def initials(name: str) -> str:
    '''Takes in a full name and returns the initials of the name in
    a string in capital letters'''
    x = ''
    for w in name.split():
        x += w[0]
    return x.upper()

assert initials('Bill Cody') == 'BC'
assert initials('Guido van Rossum') == 'GVR'
assert initials('alan turing') == 'AT'

print(initials('Forrest Gump'))

print()
print('--part d1--')
from random import randrange
for x in range(51):
    print(randrange(11))

for x in range(51):
    print(randrange(1,7))

print()
print('--part d2--')
def roll2dice() -> int:
    '''takes to random numbers and returns the sum of the numbers'''
    d1 = randrange(1, 7)
    d2 = randrange(1, 7)
    return d1 + d2
for x in range(51):
    print(roll2dice())

print()
print('--part d3--')
def distribution_of_rolls(n: int):
    '''Takes in a number and prints out the distribution values of the rolls'''
    number = [2,3,4,5,6,7,8,9,10,11,12]
    total = 0
    odds = 0
    star = ''
    results =[]
    for y in range(n):
        results.append(roll2dice())
    for x in number:
        total = results.count(x)
        odds = total / n * 100
        star = '*' * total
        print('{:2}:    {:3} ({:4.1f})%  {}'.format(x, total, odds, star))
    print('-------------------------')
    print('     ',n ,'rolls     ')

distribution_of_rolls(200)

print()
print('--part e1--')
ALPHABET = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOWER = 'abcdefghijklmnopqrstuvwxyz'
UPPER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def rotate(n: int) -> str:
    return LOWER[n%26:] + LOWER[:n%26]+ UPPER[n%26:] + UPPER[:n%26]

def Caesar_encrypt(m: str, n: int) -> str:
    '''Takes in a string containing a message and an int for the key and returns
    the ciphertext'''
    table = str.maketrans(ALPHABET, rotate(n))
    return m.translate(table)

print(Caesar_encrypt('hello', 3))

def Caesar_decrypt(m: str, n: int) -> str:
    '''Takes in a string containing a message and an int for the key and returns
    the plaintext'''
    table = str.maketrans(rotate(n), ALPHABET)
    return m.translate(table)
            
print(Caesar_decrypt('khoor',3))

print()
print('--part e2--')

print(Caesar_encrypt('im gonna be a pokemon master', 7))
'pt nvuuh il h wvrltvu thzaly'

print(Caesar_decrypt('spwwz, szh lcp jzf?', 11))
'hello, how are you?'


print()
print('--part e3--')

print(Caesar_encrypt('cat', 3))

print()
print('--part f1--')
Text = [ "Four score and seven years ago, our fathers brought forth on",
         "this continent a new nation, conceived in liberty and dedicated",
         "to the proposition that all men are created equal.  Now we are",
         "   engaged in a great 		civil war, testing whether that nation, or any",
         "nation so conceived and so dedicated, can long endure.        " ]

def print_line_numbers(L: 'list of strings') -> str:
    '''Takes in a list of strings and prints each string preceded by a line numbe''' 
    for s in range(len(L)):
        print('{:5}: {}'.format(s+1, L[s]))
print_line_numbers(Text)

print()
print('--part f2--')
def stats(L: 'list of strings'):
    '''takes a list of strings and prints the stats of the string'''
    print('{:5}    lines in the list'.format(len(L)))
    empty = 0
    for i in L:
        if i == '':
            empty += 1
    print('{:5}    empty lines'.format(empty))
    characters = 0
    for i in L:
        characters += len(i)
    print('{:7.1f}  average characters per line'.format(characters/len(L)))
    non_empty = []
    for i in L:
        if i != '':
            non_empty.append(i)
    x = 0
    for i in non_empty:
        x += len(i)
    print('{:7.1f}  average characters per non-empty line'.format(x/len(non_empty)))
stats(Text)

print()
print('--part f3--')
def list_of_words(L: 'list of strings') -> list:
    words = []
    punc = ',.?"!'
    for i in L:
        for w in i.split():
            w = w.strip(',.?! ')
            words.append(w)
    return words
print(list_of_words(Text))

print()
print('--part g1--')

    

       
       
            
            
    
     

        
