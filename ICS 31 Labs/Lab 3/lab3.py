# Luis Barrantes 82971123 and Raul Cervantes 77825705 ICS Lab Sec 3. Lab asst 3.

# Part c
# c.1
print('--part c.1--')
# function
def abbreviate(n: str) -> str:
    '''Take in a string and return the first three letters of the string'''
    return n[0:3]
assert abbreviate('January') == 'Jan'
assert abbreviate('abril') == 'abr'
# example
print(abbreviate('December'))
print(abbreviate('Computer'))

# c.2
print('')
print('--part c.2--')
# function
def find_area_square(s: int) -> int:
    '''Take in an input as length of one side of square and return the area of that square'''
    return s**2
assert find_area_square(1) == 1
assert find_area_square(5) == 25
# example
print(find_area_square(14))

# c.3
print('')
print('--part c.3--')
# function
def find_area_circle(num: float) -> float:
    '''input a radius and return the area of the circle with that radius'''
    return (3.14159) * (num ** 2)
assert find_area_circle(1) == 3.14159
assert find_area_circle(5) == 78.53975
# example
print(find_area_circle(2))

# c.4
print('')
print('--part c.4--')
# function
def print_even_numbers (s: int) -> int:
    '''Take in a list of integers and return the even numbers in the list'''
    for even in s:
        if even%2 == 0:
            print(even)
# example
print_even_numbers([2, 47, 31, 99, 20, 19, 23, 105, 710, 1004])

# c.5
print('')
print('--part c.5--')
# function
def calculate_shipping(w: float) -> float:
    '''Take in the weight of the package and return the shipping price of the package'''
    if w < 2.0:
        return(2.00)
    else:
        if w < 10.0:
            return(5.00)
        else:
            return(5.0 + 1.50*(w-10.0))

assert calculate_shipping(1.5) == 2.00
assert calculate_shipping(7) == 5.00
assert calculate_shipping(15) == 12.50
# example
print(calculate_shipping(13.0))
print(calculate_shipping(1.02))
print(calculate_shipping(7.0))

# c.6
print('')
print('--part c.6--')
# function
import tkinter
def create_square(x: int, y: int, L: int):
    '''Take in the x and y coordinates of the upper left vertex and the length and creates a square'''
    
    my_window = tkinter.Tk()

    my_canvas = tkinter.Canvas(my_window, width=500, height=500)
    my_canvas.pack()  
    my_canvas.create_rectangle(x, y, x+L, y+L)
    tkinter.mainloop()
    
create_square(100, 100, 200)

# c.7
print('')
print('--part c.7--')
# function
def create_circle(x: int, y: int, D: int):
    '''Take in the x and y coordinates of the upper left vertex of a square and the diameter and creates a circle'''
    
    my_window = tkinter.Tk()    # Create the graphics window

    my_canvas = tkinter.Canvas(my_window, width=500, height=500)  # Create a 500x500 canvas to draw on
    my_canvas.pack()  
    my_canvas.create_oval(x, y, x+D, y+D)
    tkinter.mainloop()
# example
create_circle(100, 100, 200)

# Part d
# d.1
print()
print('--part d.1--')
from collections import namedtuple
Restaurant = namedtuple('Restaurant', 'name cuisine phone dish price')
RC = [
    Restaurant("Thai Dishes", "Thai", "3344433", "Mee Krob", 12.50),
    Restaurant("Nobu", "Japanese", "3354433", "Natto Temaki", 5.50),
    Restaurant("Thai Dishes", "Thai", "3344433", "Mee Krob", 12.50),
    Restaurant("Nobu", "Japanese", "3354433", "Natto Temaki", 5.50),
    Restaurant("Nonna", "Italian", "3554433", "Stracotto", 25.50),
    Restaurant("Jitlada", "Thai", "3244433", "Paht Woon Sen", 15.50),
    Restaurant("Nola", "New Orleans", "3364433", "Jambalaya", 5.50),
    Restaurant("Noma", "Modern Danish", "3374433", "Birch Sap", 35.50),
    Restaurant("Addis Ababa", "Ethiopian", "3374453", "Yesiga Tibs", 10.50) ]
# function
def restaurant_price (p: Restaurant) -> float:
    '''Take Restaurant and return price'''
    return p.price

assert restaurant_price(RC[0]) == 12.5
assert restaurant_price(RC[-1]) == 10.5
# example
print(restaurant_price(RC[1]))

# d.2
print()
print('--part d.2--')
RC.sort(key=restaurant_price)
print(RC)

# d.3
print()
print('--part d.3--')
def costliest(p: list) -> str:
    '''Takes a list of the restuarant and returns the name of the restuarant with the highest price'''
    return p[-1].name
print(costliest(RC))

#d.4
print('')
print('--part d.4--')

Restaurant1 = namedtuple('Restaurant', 'name cuisine phone dish price')
RC1 = [
    Restaurant1("Thai Dishes", "Thai", "3344433", "Mee Krob", 12.50),
    Restaurant1("Nobu", "Japanese", "3354433", "Natto Temaki", 5.50),
    Restaurant1("Thai Dishes", "Thai", "3344433", "Mee Krob", 12.50),
    Restaurant1("Nobu", "Japanese", "3354433", "Natto Temaki", 5.50),
    Restaurant1("Nonna", "Italian", "3554433", "Stracotto", 25.50),
    Restaurant1("Jitlada", "Thai", "3244433", "Paht Woon Sen", 15.50),
    Restaurant1("Nola", "New Orleans", "3364433", "Jambalaya", 5.50),
    Restaurant1("Noma", "Modern Danish", "3374433", "Birch Sap", 35.50),
    Restaurant1("Addis Ababa", "Ethiopian", "3374453", "Yesiga Tibs", 10.50) ]

def costliest2(p: list) -> str:
    '''Takes a list of the restuarant and returns the name of the restuarant with the highest price'''
    RC1_0 = sorted(p, key=restaurant_price)
    return RC1_0[-1].name
print(costliest2(RC1))
print(RC1)
    
#e.1
print('')
print('--part e.1--')

Book = namedtuple('Book', 'author title genre year price instock')
BSI = [
    Book('Raul Cervantes', 'This Sucks', 'Supernatural', 1950, 9000.0, 69),
    Book('John Snow', "I'm still alive", 'Fiction', 1898, 2.0, 40),
    Book('Spiderman', "I'm in Marvel now", 'Technology', 2016, 20.0, 50),
    Book('Luis Barrantes', 'Why is this long?', 'Mystery', 1969, 100.0, 90),
    Book('Tony Stark', 'I am Iron Man', 'Technology', 2008, 420.0, 150),
    Book('Luar Setnavrec', 'Suck This', 'Fantasy', 1969, 4.20, 420) ]
for d in BSI:
    print(d.title)

#e.2
print('')
print('--part e.2--')

def book_title(t: Book) -> str:
    '''Takes Book and returns title'''
    return t.title
d = sorted(BSI, key=book_title)
for b in d:
    print(b.title)

#e.3
print('')
print('--part e.3--')
for p in BSI:
    n = p.price * 1.10
    p = p._replace(price = n)
    print(p)

# e.4
print()
print('--part e.4--')
for tech in BSI:
    if tech.genre == 'Technology':
        print(tech.title)

# e.5
print()
print('--part e.5--')
c20 = []
c21 = []
for a in BSI:
    if a.year < 2000:
        c20.append(a)
print()
for b in BSI:
    if b.year >= 2000:
        c21.append(b)
print('More titles before 2000 ('+str(len(c20))+' vs. '+str(len(c21))+')')

# e.6
print()
print('--part e.6--')
def Inventory_value(n: Book) -> float:
    '''Takes in the Book and returns the value of inventory of the the Book'''
    return n.price * n.instock

def top_value(p: list) -> Book:
    '''Takes a list of the restuarant and returns the name of the restuarant with the highest price'''
    val = sorted(p, key = Inventory_value)
    return val[-1]        
#print(top_value(BSI).title)
print('The highest-value book is', top_value(BSI).title, 'by', top_value(BSI).author, 'at a value of $', Inventory_value(top_value(BSI)))

# Part f
print()
print('--Part f--')
my_window = tkinter.Tk()

my_canvas = tkinter.Canvas(my_window, width=500, height=500)
my_canvas.pack()
def create_eye(x: int, y: int, L: int):
    '''Take in the x and y coordinates of the upper left vertex and the length and creates a square'''  
    my_canvas.create_oval(x, y, x+L, y+(L/2), fill='white')
    my_canvas.create_oval(x+(L/4), y, x+(3*L/4), y+(L/2), fill='saddle brown')
    my_canvas.create_oval(x+(3*L/8), y+(L/8), x+(5*L/8), y+(3*L/8), fill='black')

#create_eye(50, 50, 100)
#create_eye(250, 50, 100)

def create_nose(x: int, y: int, D: int):
    '''Take in the x and y coordinates of the upper left vertex of a square and the diameter and creates a circle'''
    my_canvas.create_oval(x, y, x+D, y+D)

def create_mouth(x: int, y: int, R: int):
    '''Take in the x and y coordinates of the upper left vertex of a square and the diameter and creates a circle'''
    my_canvas.create_line(x, y, x+R, y)

#create_mouth(100, 100, 100)
def draw_face(x: int, y: int, z: int):
    '''Take in the x and y coordinates of the upper left vertex of a square and the distance and creates a face'''
    my_canvas.create_oval(x, y, x+z, y+z, fill='white')
    create_eye(x+(z/8), y+(z/4), z/4)
    create_eye(x+(5*z/8), y+(z/4), z/4)
    create_nose(x+(z/2), y+(z/2), z/12)
    create_mouth(x+(z/4), y+(3*z/4), z/2)

draw_face(0, 0, 500)

tkinter.mainloop()
my_window = tkinter.Tk()

my_canvas = tkinter.Canvas(my_window, width=500, height=500)
my_canvas.pack()
draw_face(100, 100, 250)
tkinter.mainloop()
