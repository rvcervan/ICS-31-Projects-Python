
def NB(bedroom: list, newroom: str):
    bedroom.append(newroom.strip())
    #print(bedroom)

def LB(bedroom: list):
    print('Number of bedrooms in service:  ',len(bedroom))
    for b in bedroom:
        print(b)

def PL(line: str):
    if line[0:2] == 'PL':
        print(line[2:])

def BandB():
    s = input('Open the text file: ')
    infile = open(s, 'r')
    lines = infile.readlines()
    bedroom = []
    for line in lines:
        line = line.strip()
        if line[0:2].upper() == 'PL':
            PL(line)
        if line[0:2].upper() == 'NB':
            NB(bedroom, line[2:])
            
        if line[0:2].upper() == 'LB':
            LB(bedroom)
            
    
    
BandB()





    
    
    
    
        


    
