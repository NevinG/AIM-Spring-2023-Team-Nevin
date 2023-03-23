from Individual import Individual
from IPython.display import display # to display images
import random
import copy

class EvolutionSimulator:
    def __init__(self):
        self.POPULATION_SIZE = 500
        self.population = [] #population of individuals
        self.create_population()

    def kill_population(self):
        self.population = self.population[:len(self.population) // 2]

    def reproduce(self):
        n = len(self.population)
        for i in range(n):
            newIndivual = copy.deepcopy(self.population[i])
            newIndivual.mutate()
            self.population.append(newIndivual)

    def create_population(self):
        for i in range(self.POPULATION_SIZE):
            self.population.append(Individual())

    def show_images(self):
        for person in self.population:
            display(person.generate_image())
    
    def get_images(self):
        images = []
        for person in self.population:
            images.append(person.generate_image())
        return images

    def evaluate_fitness(self):
        for individual in self.population:
            self.fitness(individual)

        self.population = sorted(self.population, key= lambda d: d.fitness, reverse=True)

    def fitness(self, individual):
         individual.fitness = len(individual.points)