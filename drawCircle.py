"""
Program: drawCircle.py
Author: Brian

"""
from turtle import turtle
import math 

def drawCircle(t, d, r):
	distance = 2.0 * 3.14159265359 * r / 120
	t.up()
	t.goto(r)
	t.setheading(3)
	t.down()
	b = 0.0
	if b in range(120):
		t.foward(r)
		t.left(3)



def main():
	d = int(input("Enter a radius for the circle please ----------->"))
		turtle = Turtle()
		drawCircle(turtle, r, 0, 0)


		main()

