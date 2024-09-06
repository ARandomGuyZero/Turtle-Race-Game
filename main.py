"""
Turtle Race Game

Author: Alan
Date: September 6th 2024

This script generates a basic turtle race.
The user can bet, and they can predict which turtle will win
"""
import random
from turtle import Turtle, Screen

def turtle(turtle_color, turtle_initial_position):
    """
    Creates a new turtle
    :param turtle_color: String with the name of the color
    :param turtle_initial_position: Integer with the X coordinates of the turtle
    """
    new_turtle = Turtle(shape="turtle") # Creates new color
    new_turtle.color(turtle_color) # Adds a new color
    new_turtle.penup() # Disables drawing
    new_turtle.goto(x=-230, y=turtle_initial_position) # Moves the turtle to the starting position
    all_turtles.append(new_turtle) # Appends the turtle to the list

screen = Screen()
screen.setup(width=500, height=400)

# String with predictions of the race
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ").lower()

# List of String colors
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
is_race_on = False

# Starting position
position = -90

# The race does not start until the user types a prediction
if user_bet:
    is_race_on = True

# Creates a new turtle per color
for color in colors:
    turtle(color, position)
    position += 30

# Simple loop to start the race
while is_race_on:

    # For each turtle in the all_turtle list, they will move a random number of steps and check if they got to the goal
    for turtle in all_turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        # If they get to the coordinates goal, the game explains who won
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won! The {turtle.pencolor()} turtle has reached the goal")
            else:
                print(f"You lost! The {turtle.pencolor()} turtle has reached the goal")
            is_race_on = False

screen.exitonclick()
