print('Stage I')

def NB(bedroom: list, newroom: str):
    bedroom.append(newroom.strip())
    return bedroom

def LB(bedroom: list):
    print('Number of bedrooms in service:  ',len(bedroom))
    print('--------------------------------------')
    for b in bedroom:
        print(b)

def PL(line: str):
    if line[0:2] == 'PL':
        print(line[2:].strip())

##def BandB():
##    s = input('Open the text file: ')
##    infile = open(s, 'r')
##    lines = infile.readlines()
##    bedroom = []
##    for line in lines:
##        line = line.strip()
##        if line[0:2].upper() == 'PL':
##            PL(line)
##        if line[0:2].upper() == 'NB':
##            NB(bedroom, line[2:])
##            
##        if line[0:2].upper() == 'LB':
##            LB(bedroom)
##BandB()

print()
print('Stage II')

def DB(bedroom: list, roomnum: int):
    if roomnum.strip() in bedroom:
        bedroom.remove(roomnum.strip())
        return bedroom
    elif roomnum not in bedroom:
        print("Sorry, can't delete room {}; it is not in service now".format(roomnum))
        return bedroom

##def BandB():
##    s = input('Open the text file: ')
##    infile = open(s, 'r')
##    lines = infile.readlines()
##    bedroom = []
##    for line in lines:
##        line = line.strip()
##        if line[0:2].upper() == 'PL':
##            PL(line)
##        if line[0:2].upper() == 'NB':
##            NB(bedroom, line[2:])
##        if line[0:2].upper() == 'LB':
##            LB(bedroom)
##        if line[0:2].upper() == 'DB':
##            DB(bedroom, line[2:])
##
##BandB()

print()
print('Stage III')

from collections import namedtuple
Customer = namedtuple('Customer', 'roomnumber arrive depart name confirmation')
c = 0
def RR(bedroom: list, line: str, res: list):
    global c
    c+=1
    newline = line[2:].split()
    withoutname = newline[:3]
    name = []
    name.append(' '.join(newline[3:]))
    withoutname.extend(name)
    roomnumber = withoutname[0]
    arrive = withoutname[1]
    depart = withoutname[2]
    name = withoutname[3]
    confirmation = c
    Customers = Customer(roomnumber, arrive, depart, name, confirmation)
    if Customers.roomnumber in bedroom:
        res.append(Customers)
        print("Reserving room {} for {} -- Confirmation #{} \n\t(arriving {}, departing {})".format(Customers.roomnumber, Customers.name, Customers.confirmation, Customers.arrive, Customers.depart))
    elif Customers.roomnumber not in bedroom:
        print("Sorry; can't reserve room {}; room not in service".format(Customers.roomnumber))
    return res

def LR(reserves: list):
    print('Number of reservations:  ', len(reserves))
    print('No. Rm. Arrive       Depart    Guest')
    print('-----------------------------------------------')
    for i in reserves:
        print(' {} {} {} {} {}'.format(i.confirmation, i.roomnumber, i.arrive, i.depart, i.name))

def DR(reserves: list, line: str):
    newline = line[2:].strip()
    for i in reserves:
        if newline == str(i.confirmation):
            reserves.remove(i)
    else:
        if newline != str(i.confirmation):
            print("Sorry, can't cancel reservation; no confirmation number {}".format(newline))

##def BandB():
##    s = input('Open the text file: ')
##    infile = open(s, 'r')
##    lines = infile.readlines()
##    bedroom = []
##    reserves = []
##    for line in lines:
##        line = line.strip()
##        if line[0:2].upper() == 'PL':
##            PL(line)
##        elif line[0:2].upper() == 'NB':
##            NB(bedroom, line[2:])
##        elif line[0:2].upper() == 'LB':
##            LB(bedroom)
##        elif line[0:2].upper() == 'DB':
##            DB(bedroom, line[2:])
##        elif line[0:2].upper() == 'RR':
##            RR(bedroom, line, reserves)
##        elif line[0:2].upper() == 'LR':
##            LR(reserves)
##        elif line[0:2].upper() == 'DR':
##            DR(reserves, line)
##        elif line[0:2].upper() == '**':
##            pass
##        else:
##            print("Sorry, invalid command")
##    return

    
print()
print('Stage IV')

from datetime import datetime

from collections import namedtuple
Customer = namedtuple('Customer', 'roomnumber arrive depart name confirmation')
c = 0

def RR(bedroom: list, line: str, res: list):
    global c
    c+=1
    newline = line[2:].split()
    withoutname = newline[:3]
    name = []
    name.append(' '.join(newline[3:]))
    withoutname.extend(name)
    roomnumber = withoutname[0]
    arrive = withoutname[1]
    depart = withoutname[2]
    name = withoutname[3]
    confirmation = c
    Customers = Customer(roomnumber, arrive, depart, name, confirmation)

    arrival = arrive.split('/')
    departure = depart.split('/')
    arrival_d = datetime(int(arrival[2]), int(arrival[0]), int(arrival[1]))
    departure_d = datetime(int(departure[2]), int(departure[0]), int(departure[1]))
    
    if Customers.roomnumber in bedroom:
        if arrival_d > departure_d:
            print('Sorry, can\'t reserve room {} ({} to {}); \n\tcan\'t leave before you arrive.'.format(roomnumber, arrive, depart))
        elif arrival_d == departure_d:
            print('Sorry, can\'t reserve room {} ({} to {}); \n\tcan\'t arrive and leave on the same day.'.format(roomnumber, arrive, depart))
        else:
            res.append(Customers)
            print("Reserving room {} for {} -- Confirmation #{} \n\t(arriving {}, departing {})".format(Customers.roomnumber, Customers.name, Customers.confirmation, Customers.arrive, Customers.depart))
    elif Customers.roomnumber not in bedroom:
        print("Sorry; can't reserve room {}; room not in service".format(Customers.roomnumber))   
    return res

def BandB():
##    s = input('Open the text file: ')
    infile = open('BBcommands.txt', 'r')
    lines = infile.readlines()
    outfile = open('BBresults.txt', 'w')
    bedroom = []
    reserves = []
    for line in lines:
        line = line.strip()
        if line[0:2].upper() == 'PL':
            PL(line)
        elif line[0:2].upper() == 'NB':
            NB(bedroom, line[2:])
        elif line[0:2].upper() == 'LB':
            LB(bedroom)
        elif line[0:2].upper() == 'DB':
            DB(bedroom, line[2:])
        elif line[0:2].upper() == 'RR':
            RR(bedroom, line, reserves)
        elif line[0:2].upper() == 'LR':
            LR(reserves)
        elif line[0:2].upper() == 'DR':
            DR(reserves, line)
        elif line[0:2].upper() == '**':
            pass
        else:
            print("Sorry, invalid command")
BandB()
            
#Couldn't figure out how to write the results of this function into a file
    


                                                                                                 
