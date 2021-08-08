# Raul Cervantes 77825705 and  Miguel Olvera 26187521. ICS 31 Lab sec 7. Lab asst 7.

print()
print('--part c1--')
import random
from random import randrange
def random_surnames(n: int) -> list:
    '''Takes and integer and returns a list of that many strings,
    with each string a randomly generated name as described above'''
    names = []
    new = []
    infile = open('surnames.txt', 'r')
    x = infile.readlines()
    for line in x:
        names.append(line.split()[0])
    for i in range(n):
        new.append(random.choice(names))
    return new

##print(random_names(5))

def random_firstname(n: int) -> list:
    names = []
    new = []
    infile = open('malenames.txt', 'r')
    x = infile.readlines()
    for lines in x:
        names.append(lines.split()[0])
        infile = open('femalenames.txt', 'r')
    x = infile.readlines()
    for line in x:
        names.append(line.split()[0])
    for i in range(n):
        new.append(random.choice(names))
    return new
##print(random_firstname(5))


def random_names(n: int) -> str:
    for i in range(n):
        print ('{}, {}'.format(random_surnames(n)[0],random_firstname(n)[0]))

random_names(2)

print()
print('--part c2 and c3--')
        
def random_names(n: int) -> str:
    for i in range(n):
        print ('{}, {}'.format(random_surnames(n)[0].capitalize(),random_firstname(n)[0].capitalize()))
random_names(2)

print()
print('--part d1--')
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
##print(Caesar_encrypt('Power Tower Shower in the Universe', 8))

def Caesar_break(s: str) -> str:
    '''Takes in an encrypted string and returns the plaintext string without
        the key'''
    infile = open('wordlist.txt', 'r')
    temp = []
    for line in infile:
        temp.extend(line.split())
    for i in range(26):
        table = str.maketrans(ALPHABET, rotate(i))
        stuff = s.translate(table)
        nuff = stuff.split()
        for word in nuff:
            if word in temp:
                return stuff
##print(Caesar_break('Xwemz Bwemz Apwemz qv bpm Cvqdmzam'))

print()
print('--part e1--')

def copy_file():
    infile_name = input("Please enter the name of the file to copy: ")
    infile = open(infile_name, 'r', encoding='utf8')
    outfile_name = input("Please enter the name of the new copy:  ")
    outfile = open(outfile_name, 'w', encoding='utf8')
    for line in infile:
        outfile.write(line)
    infile.close()
    outfile.close()
    
##copy_file()

print()
print('--part e2--')

def copy_file(s: str):
    result = 0
    infile_name = input("Please enter the name of the file to copy: ")
    infile = open(infile_name, 'r', encoding='utf8')
    outfile_name = input("Please enter the name of the new copy:  ")
    outfile = open(outfile_name, 'w', encoding='utf8')
    if s == 'line numbers':
        for line in infile:
            result += 1
            outfile.write('{:5}: {}'.format(result, line))
    infile.close()
    outfile.close()

    
##copy_file('line numbers')

print()
print('--part e3--')

def copy_file(s: str):    
    infile_name = input("Please enter the name of the file to copy: ")
    infileMain = (open(infile_name, 'r', encoding='utf8'))
    infile=list(infileMain)
    outfile_name = input("Please enter the name of the new copy:  ")
    outfile = open(outfile_name, 'w', encoding='utf8')
    if s == 'line numbers':
        for line in infile:
            result += 1
            outfile.write('{:5}: {}'.format(result, line))
    elif s == 'Gutenberg trim':
        start=-1
        end=-1
        for i in range(len(infile)):
            if infile[i][0:3]=="***":
                if start==-1:
                    start=i
                else:
                    end=i
                    break
    
        outfile.write("\n".join(infile[start:end]))
    infileMain.close()
    outfile.close()


##copy_file('Gutenberg trim')

print()
print('--part e4--')
 
def copy_file(s: str):
    infile_name = input("Please enter the name of the file to copy: ")
    infile = open(infile_name, 'r', encoding='utf8')
    outfile_name = input("Please enter the name of the new copy:  ")
    outfile = open(outfile_name, 'a', encoding='utf8')
    x = infile.readlines()
    lines = 0
    empty = 0
    char = 0
    avg_empty = 0
    result = 0
    if s == 'line numbers':
        for line in x:
            result += 1
            outfile.write('{:5}: {}'.format(result, line))
    elif s == 'Gutenberg trim':
        start=-1
        end=-1
        for i in range(len(x)):
            if x[i][0:3]=="***":
                if start==-1:
                    start=i
                else:
                    end=i
                    break
    
        outfile.write("\n".join(x[start:end]))
    elif s == 'statistics':
        for line in x:
        
            if line == '\n':
                empty += 1
            if line != '\n':
                lines += 1
            outfile.write(line)            

        for num in x:
            char += len(num)
        avg_char = char/len(x)
        non_empty = char/(len(x)- empty)
     
        outfile.write('\n')       
        outfile.write('{:5} lines in the file'.format(lines))
        outfile.write('\n')
        outfile.write('{:5} empty lines'.format(empty))
        outfile.write('\n')
        outfile.write('{:5.1f} average characters per line'.format(avg_char))
        outfile.write('\n')
        outfile.write('{:5.1f} average characters per non-empty line'.format(non_empty))
    
    infile.close()
    outfile.close()
    
    
copy_file('statistics')
copy_file('Gutenberg trim')
copy_file('line numbers')


        



##infile = open('example.txt', 'r,w,a,r+,t,b')
##r = reading mode(default)
##w = writing mode; if the file already exists, its content is wiped out
##a = append mode; writes are appended to the end of the file
##r+ = reading and writing mode(beyond the scope of this book)
##t = text mode(default)
##b = binary mode

##infile.read(n) = Read n characters from the file infile or until the end
##                 of the file is reached, and return characters read as a string
##
##infile .read() = Read characters from file infile until the end of
##                 the file and return characters read as a string
##
##infile.readline() = Read file infile until (and including) the new line character or until
##        end of file, whichever is first, and return characters read as a string
##
##infile.readlines() = Read file inf ile until the end of the file and return the characters
##                    read as a list lines
##
##outfile.write(s) = Write strings to file outfile
##
##file.close() = Close the file
