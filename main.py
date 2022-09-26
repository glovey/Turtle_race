from turtle import Turtle,Screen
from random import randint


screen = Screen()
screen.setup(width= 500,height= 400)

user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Pick a color")
colors = ["red", "orange","yellow","green","blue","purple"]
turtles = []

y_pos = -50


game_on = False

def go():

  tim.forward(460)

for x in colors:
  
  tim = Turtle(shape = "turtle",)
  tim.color(x)
  tim.up()
  tim.goto(x=-230,y = y_pos)
  turtles.append(tim)
  
  y_pos +=25

if user_bet:
    game_on = True

while game_on:
  num = randint(10,50)
  turt = randint(0,5)
  turtles[turt].forward(num)
  
  for x in turtles:
    if x.xcor() >= 230:
      print (f"the {x.pencolor()} turtle won!")
      
      if x.pencolor() == user_bet:
        print  ("you win!")
      else:
        print ("you lose!")
      game_on = False










screen.exitonclick()

