# sprite.py
from browser import *
from sprite import *
from e2ga import *

# Discard the old canvas if it exists. 
canvas = document.getElementById("canvas")
if (canvas):
    canvas.parentNode.removeChild(canvas)

# Create a new canvas, setting the attributes in three ways! 
canvas = document.createElement("canvas", {"id": "canvas"})
canvas.width = 400
canvas.height = 300
canvas.setAttribute("height", "300")

# Append the canvas to the provided container (the content of the widget).
container = document.getElementById("canvas-container")
container.appendChild(canvas)

# The turtle code will be happy now that it now has a canvas element!

screen = Screen()
screen.bgcolor("black")

a = Sprite({"color": "orange", "shape": "turtle"})

a.up()
for size in range(5,60,2):
    a.stamp()
    a.forward(size)
    a.left(24)
    # heading() is currently degrees, we want a vector.
    # It's also a method and we want a mutable property.
    #print a.heading()
    # position() looks like a tuple, we want a vector.
    #print a.position()
    #print a.location.x

screen.exitonclick()