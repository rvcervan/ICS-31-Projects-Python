
# Caroline Alvarado 24855257 and Raul Cervantes 77825705. ICS 31 Lab sec 3. Lab asst 4.

#1
print()
print('--part c.1--')
def test_number(n:int, s:str) -> bool:
    ''' Takes in an input a number and string and returns True if the number
    has the property indicated by the string, and False if it doesn't.'''
    if s=='even':
        return n%2==0
    if s== 'odd':
        return n%2==1
    if s=='positive':
        return n>=0
    if s=='negative':
        return n<0
assert test_number(14, 'even')
assert not test_number(100, 'odd')
assert test_number(33, 'positive')
assert not test_number(100, 'negative')

print (test_number(6,'even'))
print (test_number(-2,'odd'))
print (test_number(6,'positive'))
print (test_number(6,'negative'))

#2
print()
print('--part c.2--')
##def display():
##    ''' Enter any word or phrase and then prints out every character in that phrase, one per line.'''
##    x=input('Enter a word:')
##    for letter in x:
##        print(letter)
##
##display()


#3
print()
print('--part c.3--')
def square_list(l:int)->int:
    '''Takes in a list of integers and prints out each integer squared.'''
    for number in l:
        print(number**2)

square_list([2, 3, 4, 10])

#4
print()
print('--part c.4--')
def match_first_letter(s:str, l:list)-> str:
    ''' Take in a one-character string and a list of strings and prints all the strings in the list that start with the specified character'''
    for names in l:
        if s==names[0]:
            print(names)

match_first_letter('I', ['Iron Man', 'Iron Man 2', 'The Avengers', 'Superman', 'I am Legend'])

#5
print()
print('--part c.5--')
def match_area_code(list_area:list,list_phone:list)->str:
    '''Takes in a list of phone area codes and a list of phone numbers in the form shown below.'''
    for area in list_phone:
        for numbers in list_area:
            if numbers==area[1:4]:
                print (area)

match_area_code(['949', '714'], ['(714)824-1234', '(419)312-8732', '(949)555-1234'])               

#6
print()
print('--part c.6--')
def matching_area_codes(list_area:list,list_phone:list)->str:
    '''Returns a list of the matching numbers.'''
    n=[]
    for area in list_phone:
        for numbers in list_area:
            if numbers==area[1:4]:
                n.append(area)
    return n
print(matching_area_codes(['949', '714'], ['(714)824-1234', '(419)312-8732', '(949)555-1234']))

#d.1
print()
print('--part d1--')
def is_vowel(s:str)->bool:
    '''Takes in a one-character-long string and returns True if that character is a vowel and False otherwise.'''
    v='aeiouAEIOU'
    return s in v
print( is_vowel('v'))
assert is_vowel('a') 
assert is_vowel('U')
assert not is_vowel('X')
assert not is_vowel('?')

#d.2
print()
print('--part d.2--')
def print_nonvowels(s:str)-> str:
    '''Takes in a string and prints out all the characters in the string that are not vowels.'''
    v='aeiouAEIOU'
    for letter in s:
        if letter not in v:
            print(letter)
print_nonvowels('anteater')

#d.3
print()
print('--part d.3--')
def nonvowels(s:str)-> str:
    '''Takes in a string and returns a string containing all the characters in the parameter string that are not vowels.'''
    v='aeiouAEIOU'
    result=''
    for letter in s:
        if letter not in v:
            result += letter
    return result
print(nonvowels('Anteater'))

#d.4
print()
print('--part d.4--')
def consanants(s:str)->str:
    '''Takes in a string and returns a string containing all the letters in the parameter string that are not vowels'''
    c='bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    result=''
    for letter in s:
        if letter in c:
            result += letter
    return result
    
print(consanants('anteater!'))

#d.5
print()
print('--part d.5--')
def select_letters(s1:str,s2:str)->str:
    '''Takes two strings and returns a string'''
    v='aeiouAEIOU'
    result=''
    for letter in s2:
        if s1=='v' and letter in v:
           result+= letter
        if s1=='c' and letter not in v:
            result+=letter
    return result

print(select_letters('c','my name is caro'))


#d.6
print()
print('--part d.6--')
def hide_vowels(s:str)->str:
    '''Takes a string and returns a string in which every vowel in the parameter is replaced with a hyphen.'''
    v='aeiouAEIOU'
    result = s
    for letter in s:
        if letter in v:
            result = result.replace(letter,'-')
    return result
    
print(hide_vowels('anteater'))
        

#e
print()
print('--part e--')
from collections import namedtuple
Restaurant = namedtuple('Restaurant', 'name cuisine phone dish price')
r = Restaurant('Cool', 'yum', 1234567, 'food', 4.20)
def Restaurant_change_price(obj: Restaurant, n: float) -> Restaurant:
    '''Returns a object with the sme contents as the parameter except that the price has been
    increased by the specified number.'''
    return obj._replace(price = obj.price + n)
print(Restaurant_change_price(r, .80))


#f

Restaurant = namedtuple('Restaurant', 'name cuisine phone dish price')
# Restaurant attributes: name, kind of food served, phone number,
#	best dish, price of that dish

R1 = Restaurant("Taillevent", "French", "343-3434", "Escargots", 24.50)
R2 = Restaurant("La Tour D'Argent", "French", "343-3344", "Ris de Veau", 48.50)
R3 = Restaurant("Pascal", "French", "333-4444", "Bouillabaisse", 32.00)
R4 = Restaurant("Thai Touch", "Thai", "444-3333", "Mee Krob", 10.95)
R5 = Restaurant("Thai Dishes", "Thai", "333-4433", "Paht Woon Sen",  8.50)
R6 = Restaurant("Thai Spoon", "Thai", "334-3344", "Mussamun", 9.00)
R7 = Restaurant("McDonald's", "Burgers", "333-4443", "Big Mac", 3.95)
R8 = Restaurant("Burger King", "Burgers", "444-3344", "Whopper", 3.75)
R9 = Restaurant("Wahoo's", "Fish Tacos", "443-4443", "Mahi Mahi Burrito", 7.50)
R10 = Restaurant("In-N-Out Burger", "Burgers", "434-3344", "Cheeseburger", 2.50)
R11 = Restaurant("The Shack", "Burgers", "333-3334", "Hot Link Burger", 4.50)
R12 = Restaurant("Gina's", "Pizza", "334-4433", "Combo Pizza", 12.95)
R13 = Restaurant("Peacock, Room", "Indian", "333-4443", "Rogan Josh", 12.50)
R14 = Restaurant("Gaylord", "Indian", "333-3433", "Tandoori Chicken", 13.50)
R15 = Restaurant("Mr. Chow", "Chinese", "222-3333", "Peking Duck", 24.50)
R16 = Restaurant("Chez Panisse", "California", "222-3322", "Grilled Duck Breast", 25.00)
R17 = Restaurant("Spago", "California", "333-2222", "Striped Bass", 24.50)
R18 = Restaurant("Sriped Bass", "Seafood", "333-2233", "Cedar Plank Salmon", 21.50)
R19 = Restaurant("Golden Pagoda", "Chinese", "232-3232", "Egg Foo Young", 8.50)
R20 = Restaurant("Langer's", "Delicatessen", "333-2223", "Pastrami Sandwich", 11.50)
R21 = Restaurant("Nobu", "Japanese", "335-4433", "Natto Temaki", 5.50)
R22 = Restaurant("Nonna", "Italian", "355-4433", "Stracotto", 25.50)
R23 = Restaurant("Jitlada", "Thai", "324-4433", "Paht Woon Sen", 15.50)
R24 = Restaurant("Nola", "New Orleans", "336-4433", "Jambalaya", 5.50)
R25 = Restaurant("Noma", "Modern Danish", "337-4433", "Birch Sap", 35.50)
R26 = Restaurant("Addis Ababa", "Ethiopian", "337-4453", "Yesiga Tibs", 10.50) 


RL = [R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, R14, R15, R16,
	R17, R18, R19, R20, R21, R22, R23, R24, R25, R26]

#f.1
print()
print('--part f.1--')
def alphabetical(L: list) -> list:
    '''Takes a list of restaurants and returns that list in alphabetical order by name.'''
    L.sort()
    return L
print(alphabetical(RL))
print()
#f.2
print()
print('--part f.2--')
def alphabetical_names(L: list) -> list:
    '''Takes a list of restaurants and returns that list in alphabetical order by name.'''
    result = []
    Rest = sorted(L)
    for names in Rest:
        result.append(names.name)
    return result
print(alphabetical_names(RL))

#f.3
print()
print('--part f.3--')
def all_Thai(L: list) -> list:
    '''Takes a list of resaurants and returns a list of all the Thai restaurants.'''
    Food = []
    T = 'Thai'
    for species in L:
        if T in species:
            Food.append(species)
    return Food
print(all_Thai(RL))

#f.4
print()
print('--part f.4--')
def select_cuisine(l:list,s:str)->list:
    '''Takes a list of restaurants and a string representing a cuisine. Returns a list of all the
    restaurants that serve the specified cuisine.'''
    result=[]
    for rest in l:
        if s==rest.cuisine:
            result.append(rest)
    return result

print(select_cuisine(RL,'French'))

#f.5
print()
print('--part f.5--')
def select_cheaper(l:list,n:float)->list:
    '''Takes a list of restaurants and a number and returns a list of all the restaurants whose price is less than the specified number.'''
    result=[]
    for rest in l:
        if rest.price<n:
            result.append(rest)
    return result

print(select_cheaper(RL,8.60))


#f.6
print()
print('--part f.6--')
def average_price(l:list)->float:
    '''Takes a list of restaurants and returns the average price of the restaurants.'''
    n=0
    for rest in l:
        n+=rest.price
    return n/len(l)

print(average_price(RL))

#f.7
print()
print('--part f.7--')
print(average_price(select_cuisine(RL,'Indian')))

#f.8
print()
print('--part f.8--')
chinese = select_cuisine(RL, "Chinese")
thai = select_cuisine(RL, "Thai")

combine =  []
combine.extend(chinese)
combine.extend(thai)
print(average_price(combine))
               

#f.9
print()
print('--part f.9--')
print (alphabetical_names(select_cheaper(RL,15.00)))


#g
print()
print('--part g--')
##import tkinter              # Load the library; do this just once per program
##
##my_window = tkinter.Tk()    # Create the graphics window
##
##my_canvas = tkinter.Canvas(my_window, width=500, height=500)  # Create a 500x500 canvas to draw on
##my_canvas.pack()            # Put the canvas into the window
##
##def create_rectangle_from_center(x:int,y:int,h:int,w:int):
##    '''Takes in four arguments, the x and y of the point at the center and the width and hieght.'''
##    x1=x-w/2
##    x2=x+w/2
##    y1=y-h/2
##    y2=y+h/2
##    my_canvas.create_rectangle(x1,y1,x2,y2)
##
##create_rectangle_from_center(200,200,100,200)
##
##tkinter.mainloop()          # Combine all the elements and display the window
##






    


        
