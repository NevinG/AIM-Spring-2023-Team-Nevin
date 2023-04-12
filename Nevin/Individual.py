import random
from PIL import Image, ImageDraw

class Individual:
    # point = {
    #     "x": [0,WIDTH - 1],
    #     "y": [0, HEIGHT - 1],
    #     "color": [0,255],
    #     "radius": [# of pixels]
    # }

    def __init__(self):
        self.NUMBER_OF_POINTS = random.randint(0,0)
        self.WIDTH = 100
        self.HEIGHT = 100
        self.movement_mutate_multiplier = 2
        self.radius_mutate_multiplier = 1
        self.color_mutate_multiplier = 2
        self.points = [] #each point in self.points is defined on line 5-10
        self.create_initial_values()

    #add a random chance based on our mtuate_multiplier attriubutes to:
    #add a new point
    #remove an existing point
    #change the x value of an existing point
    #change the y value of an existing point
    #change the color of an existing point
    #change the radius of an existing point
    def mutate(self):
        #chance to add a new point
        point = {
            "x": random.randint(0, self.WIDTH - 1),
            "y": random.randint(0, self.HEIGHT - 1),
            "color": random.randint(0, 255),
            "radius": random.randint(1,7)
        }
        self.points.append(point)

    #this is defined for you, i used PIL to create images based on self.points
    # and its attributes
    def generate_image(self):
        image = Image.new('RGB', (self.WIDTH, self.HEIGHT), color="white")
        draw = ImageDraw.Draw(image)
        for point in self.points:
            draw.ellipse([(point["x"] - point["radius"],point["y"] - point["radius"]),
                          (point["x"] + point["radius"], point["y"] + point["radius"])],
                            fill = (point["color"], point["color"], point["color"]))
        return image

    #fill in self.points with self.NUMBER_OF_POINTS points with 
    # random initial values and add each point to self.points
    def create_initial_values(self):
        for i in range(self.NUMBER_OF_POINTS):
            point = {
                "x": random.randint(0, self.WIDTH - 1),
                "y": random.randint(0, self.HEIGHT - 1),
                "color": random.randint(0, 255),
                "radius": random.randint(1,7)
            }
            self.points.append(point)
