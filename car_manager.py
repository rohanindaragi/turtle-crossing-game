from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = 5

    #this function helps to create a random car and moves towards the left side of the screen

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            # to set the random colors to d car
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)
    # this function can move the cars
    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    # this function increases the speed when turtle reaches the other end
    def level_up(self):
        self.car_speed += 10

