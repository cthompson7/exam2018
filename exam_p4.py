"""
What is the most interesting/funny/cool thing(s) about Python that you learned from this class or from somewhere else.

You can use code or a short paragraph to illustrate it.
"""

"""
One of the most interesting things I learned through this class was how to draw shapes and patterns using Python.
Specifically, the lesson on turtle functionality was fascinating to me, as I didn't know that coding could be used
for drawing. In particular, the draw_flower function located below was one of my favorite assignments this semester.
Using a for loop, the function creates 6 petal shapes side-by-side in a circle, ultimately forming a flower. A circle
is then created around the flower, as designated in the instructions. While we didn't get to cover complex turtle
designs and how to create them in class, this topic is an area of interest for me that I might revisit in the near
future. For people who are not typically coders and have artsy backgrounds, this might be a cool way to introduce them 
to the power of Python and showcase why learning how to code can be so beneficial for any career path. I'm hopeful that
we can also spend some time this semester covering how to create games in Python using Flask, as this is an area of
interest for me. I've really enjoyed this semester thus far!
"""

import turtle
jack =turtle.Turtle()

# 1. Write an appropriately general set of functions that can draw shapes as below. The third one shape is optional.
def draw_flower(turtle):
    for i in range(6):
        turtle.circle(100, 60)
        turtle.left(120)
        turtle.circle(100, 60)
        turtle.left(60)

    turtle.penup()
    turtle.goto(0,-100)
    turtle.pendown()
    turtle.circle(100)

draw_flower(jack)
turtle.mainloop()
