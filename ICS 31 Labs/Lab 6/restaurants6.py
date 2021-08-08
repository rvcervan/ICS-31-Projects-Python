# RESTAURANT COLLECTION PROGRAM
# ICS 31, UCI, David G. Kay, Fall 2015

# Implement Restaurant as a namedtuple, collection as a list

##### MAIN PROGRAM (CONTROLLER)

def restaurants():  # nothing -> interaction
    """ Main program
    """
    print("Welcome to the restaurants program!")
    our_rests = Collection_new()
    our_rests = handle_commands(our_rests)
    print("\nThank you.  Good-bye.")

MENU = """
Restaurant Collection Program --- Choose one
 n:  Add a new restaurant to the collection
 r:  Remove a restaurant from the collection
 s:  Search the collection for selected restaurants
 p:  Print all the restaurants
 e:  Erase all the restaurants form the collection
 c:  Change prices for the dishes served
 f:  Find restaurants that serve a specified cuisine along with the avg price of that cuisine
 d:  Find restaurants that serve the dish with similar name
 q:  Quit
"""

def handle_commands(C: list) -> list:
    """ Display menu, accept and process commands.
    """
    while True:
        response = input(MENU)
        if response=="q":
            return C
        elif response=='n':
            r = Restaurant_get_info()
##            Dish_display(Menu_enter())
            C = Collection_add(C, r)
        elif response=='r':
            n = input("Please enter the name of the restaurant to remove:  ")
            C = Collection_remove_by_name(C, n)
        elif response=='p':
            print(Collection_str(C))
        elif response=='s':
            n = input("Please enter the name of the restaurant to search for:  ")
            for r in Collection_search_by_name(C, n):
                print(Restaurant_str(r))
        elif response=='e':
            C.clear()
        elif response=='c':
            n = float(input('Please enter the percent amount to change the dish price:  '))
            C = collection_change_price(C,n)
##        elif response=='m':
##            print(Dish_display(Menu_enter(C)))
        elif response=='f':
            n = input("Please enter the name of the cuisine:  ")
            for r in Collection_search_by_cuisine(C,n):
                print(Restaurant_str(r))
        elif response == 'd':
            n = input("Please enter the name of the dish:  ")
            for r in Collection_search_by_dish(C, n):
                print(Restaurant_str(r))
            
        else:
            invalid_command(response)

def invalid_command(response):  # string -> interaction
    """ Print message for invalid menu command.
    """
    print("Sorry; '" + response + "' isn't a valid command.  Please try again.")


##### Dishes
from collections import namedtuple

Dish = namedtuple('Dish', 'name price cal')
def Dish_str(d: Dish) -> str:
    '''Takes a Dish and returns a string.'''
    return d.name + ' ($' + str(d.price) + '): ' + str(d.cal) + ' cal\n          '

def Dish_get_info() -> Dish:
    return Dish(
        input('\nPlease enter the name of the Dish: '),
        float(input('Please enter the price of the Dish: ')),
        input('Please enter the amount of calories of the Dish: '))

##### Menus
dishes_input = '\nWould you like to add a Dish?'
def Menu_enter() -> list:
    cuisine = []
    while True:
        response = input(dishes_input)
        if response == 'yes':
            cuisine.append(
                Dish_get_info())
        elif response == 'no':
            return cuisine
        
def Dish_display(result: list) -> str:
    s = ''
    for d in result:
        s = s + Dish_str(d)
    return s
    
def Rest_avg_price(M: list) -> float:
    x = 0
    for dishes in M:
        x += dishes.price
    return x / len(M)

def Rest_avg_calories(M: list) -> float:
    x = 0
    for dishes in M:
        x += int(dishes.cal)
    return x / len(M)

def Collection_search_by_dish(C: list, d: str) -> list:
    result = [ ]
    for r in C:
        for dish in r.menu:
            if d in dish.name:
                result.append(r)
                break
    return result

##### Restaurant
Restaurant = namedtuple('Restaurant', 'name cuisine phone menu')
##Restaurant = namedtuple('Restaurant', 'name cuisine phone dish price')
# Constructor:   r1 = Restaurant('Taillevent', 'French', '01-11-22-33-44', 'Escargots', 23.50)

def Restaurant_str(self: Restaurant) -> str:
        return (
        "Name:     " + self.name + "\n" +
        "Cuisine:  " + self.cuisine + "\n" +
        "Phone:    " + self.phone + "\n" +
        "Menu:     " + Dish_display(self.menu) + "\n" +
        "Average price: $" + str(Rest_avg_price(self.menu)) + ".  Average calories:  " + str(Rest_avg_calories(self.menu)))

##    return (
##        "Name:     " + self.name + "\n" +
##        "Cuisine:  " + self.cuisine + "\n" +
##        "Phone:    " + self.phone + "\n" +
##        "Dish:     " + self.dish + "\n" +
##        "Price:    ${:2.2f}".format(self.price) + "\n\n")

def Restaurant_get_info() -> Restaurant:
    """ Prompt user for fields of Restaurant; create and return.
    """
    return Restaurant(
    input("Please enter the restaurant's name:  "),
    input("Please enter the kind of food served:  "),
    input("Please enter the phone number:  "),
    Menu_enter())
##    return Restaurant(
##        input("Please enter the restaurant's name:  "),
##        input("Please enter the kind of food served:  "),
##        input("Please enter the phone number:  "),
##        input("Please enter the name of the best dish:  "),
##        float(input("Please enter the price of that dish:  ")))


#### COLLECTION
# A collection is a list of restaurants

def Collection_new() -> list:
    ''' Return a new, empty collection
    '''
    return [ ]

def Collection_str(C: list) -> str:
    ''' Return a string representing the collection
    '''
    s = ""
    for r in C:
        s = s + Restaurant_str(r)
    return s

def Collection_search_by_name(C: list, name: str) -> list:
    """ Return list of Restaurants in input list whose name matches input string.
    """
    result = [ ]
    for r in C:
        if r.name == name:
            result.append(r)
    return result

def Collection_search_by_cuisine(C: list, cuisine: str) -> list:
    result = [ ]
    for r in C:
        if r.cuisine == cuisine:
            result.append(r)
    return result

def Collection_add(C: list, R: Restaurant) -> list:
    """ Return list of Restaurants with input Restaurant added at end.
    """
    C.append(R)
    return C

def Collection_remove_by_name(C: list, name: str) -> list:
    """ Given name, remove all Restaurants with that name from collection.
    """
    result = [ ]
    for r in C:
        if r.name != name:
            result.append(r)
    return result

def Dish_price_change(D: Dish, n: int) -> Dish:
    return D._replace(price = D.price * (1 + 0.01 * n))
        
def Menu_price_change(M: list, n: int) -> list:
    result = []
    for dish in M:
        result.append(Dish_price_change(dish, n))
    return result
     
def Restaurant_price_change(R: Restaurant, n: int) -> float:
    result  = Menu_price_change(R.menu, n)
    R = R._replace(menu = result)
    return R
        
def collection_change_price(C:list, n: int)->list:
    result = []
    for rest in C:
        result.append(Restaurant_price_change(rest, n))
    return result

def Dishprice_change(R: Restaurant, n: float) -> Restaurant:
    new_menu = []
    new_menu = R.menu._replace(price = float(R.price) * (1 + 0.01 * n))
    return new_menu
restaurants()


    
