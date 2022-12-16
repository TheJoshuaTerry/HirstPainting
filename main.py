from turtle import Turtle as t, Screen as s
import random

color_list = [(197, 161, 113), (139, 167, 187), (227, 210, 114), (143, 84, 60), (55, 104, 134), (193, 145, 162), (16, 33, 54), (139, 71, 90), (146, 177, 157), (166, 153, 62), (54, 31, 20), (72, 114, 92), (16, 35, 27), (189, 99, 83), (180, 96, 121), (217, 175, 188), (118, 39, 32), (61, 24, 37), (115, 38, 50), (222, 177, 170), (37, 59, 101), (66, 153, 170), (182, 189, 207), (96, 150, 109), (23, 90, 71), (174, 203, 185)]
tim = t()
tim.speed("fastest")
tim.hideturtle()
screen = s()
tim.up()
tim.goto(-240, -230)
screen.colormode(255)

for __ in range(10):
    for _ in range(10):
        tim.dot(20, random.choice(color_list))
        tim.fd(50)
    tim.goto(-240, tim.pos()[1] + 50)

screen.exitonclick()