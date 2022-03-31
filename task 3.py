def star():
    import turtle
    turtle.showturtle()
    turtle.shape("turtle")
    turtle.pencolor('red')
    for x in range(20):
        turtle.forward(100)
        if x % 2 == 0:
            turtle.left(175)
        else:
            turtle.left(225)
      
def square():
    import turtle # this line is for import for turtle module
    t = turtle.Turtle()
    s = int(input("Enter the length of the side of square: "))
    c=input("what colour do you want your square to be: ")
    for _ in range(4):
        turtle.color(c)
        t.forward(s) # This moves the turtle by the lengh the user decides.
        t.left(90) # This turns the turtle by 90 degrees

def octagon():
    import turtle
    ws = turtle.Screen()#this line is for making a workscreen
    octaTurtle = turtle.Turtle()# turtle.Turtle is defined by a variable octa.
    for i in range(8):         
        octaTurtle.forward(100) # this moves the turtle forwards by 100 which is the length 
        octaTurtle.left(45)# this is the angle which ensures the octagon is at its correct shape
    

while True:
  choices=['octagon','square','star']
  choice=input('Would you like to draw a star square or octagon:')#asks the user what shape they would like to draw. 
  if choice.lower() in choices:
    break
  else:
    print("invalid choice")#use else statement so if user chooses an option that is not in the list of choices it displays an error message. 

if choice== 'star':
    star()           # calling on the functions for the shapes depending of the users choices.
if choice=='square':
    square()
if choice=='octagon':
    octagon()
if choice=='square'+'star':
    square()
    star()
