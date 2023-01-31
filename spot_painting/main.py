#import colorgram
import turtle
import random

screen = turtle.Screen()
turtle.colormode(255)
tim = turtle.Turtle()
tim.speed("fastest")
tim.hideturtle()
tim.penup()
posx = -300
posy = -300

# colors = colorgram.extract('image.jpeg', 30)
# rgb_colors = []
# for color in colors:
#     #print("in loop", color.rgb)
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)


def draw_row():
    for _ in range(10):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)


color_list = [(213, 151, 106), (248, 247, 74), (87, 244, 200), (41, 12, 179), (224, 115, 161), (160, 10, 76), (17, 181, 76), (31, 6, 90), (223, 49, 138), (151, 88, 43), (118, 98, 228), (84, 34, 13), (9, 97, 45), (85, 6, 38), (183, 182, 241), (71, 216, 90), (178, 45, 104), (47, 16, 249), (34, 142, 47), (155, 134, 215), (173, 9, 7), (75, 244, 249), (228, 166, 205), (234, 47, 43), (87, 74, 148), (6, 96, 100)]

for _ in range(10):
    tim.goto(posx, posy)
    draw_row()
    posy += 50

screen.exitonclick()