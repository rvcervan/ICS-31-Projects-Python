# Shiyu Ji 16024014 and Raul Cervantes 77825705  ICS 31 Lab sec 2.  Lab Asst 2.


#(c.1)
print('How many hours?')
hours = float(input())
print('This many hours:', hours)
print('How many dollars per hour?')
rate = float(input())
print('This many dollars per hour:  ', rate)
print('Weekly salary:  ', hours * rate)

hours = int(input('How many hours?'))
print('This many hours:', hours)
rate = float(input('How many dollars per hour?'))
print('This many dollars per hour:  ', rate)
print('Weekly salary:  ', hours * rate)
#modified
print('How many hours?')
hours = float(input())
print('This many hours:', hours)
print('How many dollars per hour?')
rate = float(input())
print('This many dollars per hour:  $', rate)
print('Weekly salary:  $', hours * rate)

hours = int(input('How many hours?'))
print('This many hours:', hours)
rate = float(input('How many dollars per hour?'))
print('This many dollars per hour:  $', rate)
print('Weekly salary:  $', hours * rate)

#(c.2)
name = input('Hello. What is your name?')
print("Hello, ", name)
print("It's nice to meet you.")
age = int(input('how old are you?'))
print("Next year you will be", age+1,"years old.")
print("Good-bye!")

#(d)
print('Please provide this information:')
name = input("Business name:")
num_euro = float(input('Number of euros:'))
num_pound = float(input('Number of pounds:'))
num_dollar = float(input('Number of dollar:'))
print('Copenhagen Chamber of Commerce')
print('Business name: ', name)
print(num_euro, 'euros is', num_euro * 7.46, 'krone')
print(num_pound, 'pounds is', num_pound * 8.60, 'krone')
print(num_dollar, 'dollars is', num_dollar * 6.62, 'krone')
print('Total krone: ',num_euro * 7.46 + num_pound * 8.60 + num_dollar * 6.62)


#(e)
from collections import namedtuple
Book = namedtuple('Book', 'title author year price')
favorite = Book('Adventures of Sherlock Holmes',
                'Arthur Conan Doyle', 1892, 21.50)
another = Book('Memoirs of Sherlock Holmes',
               'Arthur Conan Doyle', 1894, 23.50)
still_another = Book('Return of Sherlock Holmes',
                     'Arthur Conan Doyle', 1905, 25.00)
print(still_another[0])
print(another[3])
print((favorite[3]+another[3]+still_another[3])/3)    
print(favorite[2] <= 1900)
still_another = Book('Return of Sherlock Holmes',
                     'Arthur Conan Doyle', 1905, 26.00)
still_another = Book('Return of Sherlock Holmes',
                     'Arthur Conan Doyle', 1905, still_another[3] *1.2)
print(still_another[3])


#(f)
from collections import namedtuple
animal = namedtuple('animal', 'name species age weight food')
i = animal('Jumbo','elephant', 50, 1000, 'peanuts')
ii = animal('Perry','platypus', 7, 1.7, 'shrimp')
print( i[3] <= ii[3])

#(g)
booklist = [favorite, another, still_another]
print((booklist[0])[3] <= (booklist[1])[3])
print((booklist[0])[2] <= (booklist[-1])[2])


#(h)
from collections import namedtuple     # If this line is in your file already, you don't need it again
Restaurant = namedtuple('Restaurant', 'name cuisine phone dish price')# Restaurant attributes: name, kind of food served, phone number, best dish, price of that dish
RC = [    Restaurant("Thai Dishes", "Thai", "334-4433", "Mee Krob", 12.50),    Restaurant("Nobu", "Japanese", "335-4433", "Natto Temaki", 5.50),    Restaurant("Nonna", "Italian", "355-4433", "Stracotto", 25.50),    Restaurant("Jitlada", "Thai", "324-4433", "Paht Woon Sen", 15.50),    Restaurant("Nola", "New Orleans", "336-4433", "Jambalaya", 5.50),    Restaurant("Noma", "Modern Danish", "337-4433", "Birch Sap", 35.50),    Restaurant("Addis Ababa", "Ethiopian", "337-4453", "Yesiga Tibs", 10.50) ]
print((RC[2])[0])
print((RC[0])[1] == (RC[3])[1])
print((RC[-1])[4])
RC.sort()
print(RC)
RC.sort()
print(RC[-1].dish)
RC.sort()
NRC = (RC[0],RC[1],RC[-2],RC[-1])
print(NRC)



#(i)
#i.1
import tkinter              # Load the library; do this just once per program
my_window = tkinter.Tk()    # Create the graphics window
my_canvas = tkinter.Canvas(my_window, width=500, height=500)  # Create a 500x500 canvas to draw on
my_canvas.pack()            # Put the canvas into the window
my_canvas.create_line(100, 100, 300, 100, fill='orange') 
my_canvas.create_line(300, 300, 300, 100, fill='blue')
my_canvas.create_line(100, 300, 100, 100, fill='red')
my_canvas.create_line(100, 300, 300, 300, fill='green')
tkinter.mainloop()
#i.2
import tkinter              # Load the library; do this just once per program
my_window = tkinter.Tk()    # Create the graphics window
my_canvas = tkinter.Canvas(my_window, width=500, height=500)  # Create a 500x500 canvas to draw on
my_canvas.pack()            # Put the canvas into the window
my_canvas.create_line(200, 100, 300, 200)
my_canvas.create_line(300, 200, 200, 300)
my_canvas.create_line(200, 300, 100, 200)
my_canvas.create_line(100, 200, 200, 100)

tkinter.mainloop()

#i.3
import tkinter              # Load the library; do this just once per program
my_window = tkinter.Tk()    # Create the graphics window
my_canvas = tkinter.Canvas(my_window, width=500, height=500)  # Create a 500x500 canvas to draw on
my_canvas.pack()            # Put the canvas into the window
my_canvas.create_line(100, 100, 300, 100, fill='orange') 
my_canvas.create_line(300, 300, 300, 100, fill='blue')
my_canvas.create_line(100, 300, 100, 100, fill='red')
my_canvas.create_line(100, 300, 300, 300, fill='green')
my_canvas.create_line(100, 100, 200, 50)
my_canvas.create_line(200, 50, 300, 100)
my_canvas.create_line(150, 200, 200, 200)
my_canvas.create_line(200, 200, 200, 300)
my_canvas.create_line(200, 300, 150, 300)
my_canvas.create_line(150, 300, 150, 200)

my_canvas.create_line(225, 175, 250, 175)
my_canvas.create_line(250, 175, 250, 200)
my_canvas.create_line(250, 200, 225, 200)
my_canvas.create_line(225, 200, 225, 175)
tkinter.mainloop()

#i.4
import tkinter              # Load the library; do this just once per program
my_window = tkinter.Tk()    # Create the graphics window
my_canvas = tkinter.Canvas(my_window, width=500, height=500)  # Create a 500x500 canvas to draw on
my_canvas.pack()            # Put the canvas into the window
my_canvas.create_oval(100,200,300,300)
my_canvas.create_oval(175,225,225,275)
my_canvas.create_oval(195,227,205,273)

tkinter.mainloop()












