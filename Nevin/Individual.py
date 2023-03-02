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
        self.NUMBER_OF_POINTS = random.randint(1,100)
        self.WIDTH = 100
        self.HEIGHT = 100
        self.movement_mutate_multiplier = 2
        self.radius_mutate_multiplier = 1
        self.color_mutate_multiplier = 10
        self.points = []
        self.create_initial_values()

    def mutate(self):
        #chance to add a new point
        if random.randint(0,1) == 1:
            point = {
                "x": random.randint(0, self.WIDTH - 1),
                "y": random.randint(0, self.HEIGHT - 1),
                "color": random.randint(0, 255),
                "radius": random.randint(1,5)
            }
            self.points.append(point)

        #chance to remove an existsing point
        if random.randint(0,1) == 1:
            self.points.pop(random.randrange(len(self.points)))

        for point in self.points:
            point["x"] += random.randint(-self.movement_mutate_multiplier, self.movement_mutate_multiplier)
            if point["x"] > self.WIDTH - 1:
                point["x"] = self.WIDTH - 1
            if point["x"] < 0:
                point["x"] = 0

            point["y"] += random.randint(-self.movement_mutate_multiplier, self.movement_mutate_multiplier)
            if point["y"] > self.WIDTH - 1:
                point["y"] = self.WIDTH - 1
            if point["y"] < 0:
                point["y"] = 0

            point["radius"] += random.randint(-self.radius_mutate_multiplier, self.radius_mutate_multiplier)
            if point["radius"] > self.WIDTH / 2:
                point["radius"] = self.WIDTH / 2
            if point["radius"] < 1:
                point["radius"] = 1

            point["color"] += random.randint(-self.color_mutate_multiplier, self.color_mutate_multiplier)
            if point["color"] > 255:
                point["color"] = 255
            if point["color"] < 0:
                point["color"] = 0

    def generate_image(self):
        image = Image.new('RGB', (self.WIDTH, self.HEIGHT), color="white")
        draw = ImageDraw.Draw(image)
        for point in self.points:
            draw.ellipse([(point["x"] - point["radius"],point["y"] - point["radius"]),(point["x"] + point["radius"], point["y"] + point["radius"])], fill = (point["color"], point["color"], point["color"]))
        return image

    def create_initial_values(self):
        for i in range(self.NUMBER_OF_POINTS):
            point = {
                "x": random.randint(0, self.WIDTH - 1),
                "y": random.randint(0, self.HEIGHT - 1),
                "color": random.randint(0, 255),
                "radius": random.randint(1,5)
            }
            self.points.append(point)
