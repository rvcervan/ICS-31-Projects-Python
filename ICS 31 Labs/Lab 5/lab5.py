# Raul Cervantes 77825705 and Brandon Massaro 40863671 ICS 31 Lab sec 3, Lab asst 5.

from collections import namedtuple

Dish = namedtuple('Dish', 'name price calories')
d1 = Dish('Chicken', 3.00, 335)
d2 = Dish('Ice Cream', 2.50, 137)
d3 = Dish('Lobster', 50.00, 129)
d4 = Dish('Fish', 25.00, 129)
d5 = Dish('Cereal', 17.50, 300)
d6 = Dish('Cow', 200.00, 500)
d7 = Dish('Shrimp', 18.00, 150)
d8 = Dish('Milk', 20.00, 200)
d9 = Dish('Coke', 2.00, 200)
d10 = Dish('Beef', 13.00, 635)
d11 = Dish('Chocolate', 2.50, 300)
d12 = Dish('Onions', 14.00, 129)
d13 = Dish('Tacos', 5.00, 400)
d14 = Dish('Burritos', 7.50, 300)
d15 = Dish('Pho', 20.00, 500)
d16 = Dish('Eggs', 8.00, 150)
d17 = Dish('Beer', 6.00, 200)
d18 = Dish('Cheese', 2.00, 200)
d19 = Dish('Frys', 3.00, 335)
d20 = Dish('Wings', 2.50, 400)
d21 = Dish('Snickers', 50.00, 400)
d22 = Dish('Calzone', 25.00, 700)
d23 = Dish('Pizza', 15.00, 1000)
d24 = Dish('Rice', 20.00, 100)
d25 = Dish('Water', 18.00, 0)

print()
print('--partc2--')

def Dish_str(d: Dish) -> str:
    '''Takes a Dish and returns a string.'''
    return d.name + ' ($' + str(d.price) + '): ' + str(d.calories) + ' cal'
print(Dish_str(d1))

print()
print('--partc3--')
def Dish_same(d: Dish, f: Dish) -> bool:
    '''Takes two dishes and returns true or false if the cal is the same or different/\.'''
    return d.calories  == f.calories and d.name == f.name

assert Dish_same(d1, d2) == False
assert Dish_same(d3, d4) == False

print(Dish_same(d1, d2))

print()
print('--partc4--')

def Dish_change_price(d: Dish, n: float) -> Dish:
    '''Takes a dish and adjusts its price by a specified percentage'''
    return d._replace(price= d.price * (1 + 0.01 * n))


print(Dish_change_price(d1, 100))
print(Dish_change_price(d1, -50))

print()
print('---partc5---')

def Dish_is_cheap(d: Dish, n: float) -> bool:
    '''Takes a dish and a number n and returns true if price is less than n, and false otherwise'''
    return d.price < n

print(Dish_is_cheap(d1, 2))

print()
print('---partc6---')

DL = [d1, d2, d3, d4, d5]

DL2 = [d6, d7, d8, d9]

DL.extend(DL2)
##print(DL)

def Dishlist_display(L: list) -> str:
    '''Takes a list of Dishes and returns a string consisting of the list in every line'''
    for d in L:
        print('\n' + (Dish_str(d)))
Dishlist_display(DL)

print()
print('--partc7--')
def dish_price(d: Dish) -> float:
    '''sorts the list dishes least to greatest by price'''
    return d.price

def Dishlist_all_cheap(L: list, n: float) -> bool:
    '''Returns True is n price is less than all of the prices of dishes in the list.'''      
    return Dish_is_cheap(sorted(L, key = dish_price)[-1], n)
print(Dishlist_all_cheap(DL, 500))

print()
print('--partc8--')

def Dishlist_change_price(l: list, n: float) -> list:
    '''Takes in a list of dishes and changes the price of each dish'''
    D = []
    for d in l:
        D.append((Dish_change_price(d, n)))
    return D

print(Dishlist_change_price(DL, 100))

print()
print('--partc9--')
def Dishlist_prices(L: list) -> list:
    '''Takes in the price and puts in the prices into a list.'''
    D = []
    for d in L:
        D.append(dish_price(d))
    return D
print(Dishlist_prices(DL))

print()
print('--partc10--')
def Dishlist_average(L: list) -> float:
    '''Takes in a list of dishes and returns the average price of the dishes'''
    result = 0
    for d in L:
        result += dish_price(d)
    return result/len(L)
print(Dishlist_average(DL))

print()
print('--partc11--')
def Dishlist_keep_cheap(L: list, n: float) -> list:
    '''Takes in a list of Dishes and a float and returns a list of dishes
    whose prices are less than the number.'''
    result = []
    for d in L:
        if Dish_is_cheap(d, n):
            result.append(d)
    return result
print(Dishlist_keep_cheap(DL, 4))

print()
print('--partc12--')
All = [d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13, d14, d15, d16, d17,
       d18, d19, d20, d21, d22, d23, d24, d25]
def before_and_after():
    response = float(input('Enter the percentage you would like to change the prices: '))
    Dishlist_display(All)
    result = []
    for d in All:
        result.append(Dish_change_price(d, response))
    Dishlist_display(result)
before_and_after()
    
print()
print('--parte1--')

Restaurant = namedtuple('Restaurant', 'name cuisine phone menu')
r1 = Restaurant('Thai Dishes', 'Thai', '334-4433', [Dish('Mee Krob', 12.50, 500),
                                                    Dish('Larb Gai', 11.00, 450)])
r2 = Restaurant('Taillevent', 'French', '01-44-95-15-01', 
				[Dish('Homard Bleu', 45.00, 750),
				 Dish('Tournedos Rossini', 65.00, 950),
				 Dish("Selle d'Agneau", 60.00, 850)])	

r3 = Restaurant(' Pascal', 'French', '940-752-0107', [Dish('Escargot', 12.95, 250),
                                                      Dish('Poached Salmon', 18.50, 550),
                                                      Dish('Rack of lamb', 24.00, 850),
                                                      Dish('Marjolaine cake', 8.50, 950)])

T = [r1, r2, r3]

print()
print('--parte2--')
def Restaurant_first_dish_name(R: Restaurant) -> str:
    '''Takes in a Restaurant and returns the name of the first dish of the
    restaurant'''
    return R.menu[0].name
print(Restaurant_first_dish_name(r3))

print()
print('--parte3--')
def Restaurant_is_cheap(R: Restaurant, n: float) -> bool:
    '''Takes in a restaurant and a number and returns true if the price is less
    than the number'''
    return Dishlist_average(R.menu) <= n
print(Restaurant_is_cheap(r2, 100))

print()
print('--parte4--')
def Restaurant_raise_price(R: Restaurant) -> Restaurant:
    '''Raises the price of the cuisine in the menu by 2.5'''
    menu2 = []
    for d in R.menu:
        d = d._replace(price = d.price + 2.50)
        menu2.append(d)
    R = R._replace(menu = menu2)
    return R

def Restaurant_change_price(R: Restaurant, n: float) -> Restaurant:
    '''Raises the price of the cuisine in the menu by percent'''
    menu3 = []
    for d in R.menu:
        d = d._replace(price = d.price * (1 + 0.01 * n))
        menu3.append(d)
    R = R._replace(menu = menu3)
    return R
    
##print(Restaurant_raise_price(r1))


def Collection_raise_price(L: list) -> list:
    '''Raises the price of the collection of Restaurants by 2.5'''
    C = []
    for R in L:
        R = Restaurant_raise_price(R)
        C.append(R)
    
    return C
            
##print(Collection_raise_price(T))

def Collection_change_price(L: list, n: float) -> list:
    C = []
    for R in L:
        R = Restaurant_change_price(R, n)
        C.append(R)
    return C

print(Collection_change_price(T, 100))                       

print()
print('--parte5--') 
def Collection_select_cheap(L: list, n: float) -> list:
    '''Takes in a list of Restaurants and a number n and returns a list with restuarants
    that have price less than n'''
    D =[]
    for R in L:
        if Dishlist_average(R.menu) <= n:
            D.append(R)
    return D
print(Collection_select_cheap(T, 12.5))

print()
print('--partf--')

print()
print('--partg--')
Count = namedtuple('Count', 'letter number')

def letter_count(s: str, t:str) -> Count:
    '''returns the number of occurances or each letter specified in a given string'''
    b = []
    a = []
    for i in range(len(t)):
        for j in range(len(s)):
            if s[j] == t[i]:
                a.append(1)
            else: a.append(0)
        b.append((Count(t[i], sum(a))))
        a = []
    return b    

print(letter_count('aeiou', 'bdye'))


    
        






    
