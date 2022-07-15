# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 20)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
import random
import turtle
from turtle import Turtle, Screen

timmy = Turtle()
timmy.speed("fastest")
turtle.colormode(255)
color_list = [(210, 153, 64), (240, 232, 237), (39, 86, 172), (103, 160, 209),
              (229, 199, 57), (180, 61, 100), (148, 19, 59), (199, 115, 157), (143, 181, 10), (189, 72, 39),
              (51, 110, 95),
              (65, 53, 42), (12, 66, 135), (57, 52, 67), (187, 78, 103), (60, 50, 64), (96, 107, 170)]
timmy.setheading(225)
timmy.penup()
timmy.forward(300)
timmy.setheading(0)

for dot_count in range(1, 101):
    timmy.pencolor(color_list[random.randint(0, 7)])
    timmy.dot(20)
    timmy.penup()
    timmy.forward(50)
    timmy.pendown()
    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.penup()
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)



screen = Screen()
screen.exitonclick()
