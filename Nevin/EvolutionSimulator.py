from Individual import Individual
from IPython.display import display # to display images
import random
import copy

class EvolutionSimulator:
    def __init__(self):
        self.POPULATION_SIZE = 500
        self.population = [] #population of individuals
        self.create_population()

    #should remove the second half of self.population [a,b,c,d] 
    # after kill_population = [a,b]
    def kill_population(self):
        self.population = self.population[:len(self.population) // 2]

    #doubles the population. For each indivuals in self.population 
    # make an identical copy of them, and then call the .mutate method 
    # on that individual
    def reproduce(self):
        n = len(self.population)
        for i in range(n):
            newIndivual = copy.deepcopy(self.population[i])
            newIndivual.mutate()
            self.population.append(newIndivual)

    #create self.POPULATION_SIZE individuals add add them to self.population
    def create_population(self):
        for i in range(self.POPULATION_SIZE):
            self.population.append(Individual())

    #call the generate_image method on each individual
    def show_images(self):
        for person in self.population:
            display(person.generate_image())
    
    def get_images(self):
        images = []
        for person in self.population:
            images.append(person.generate_image())
        return images

    #should sort self.population in order of each individuals fitness 
    # (high to low) (this must be called after fitness() otherwise there 
    # is no fitness attribute to sort by)
    def evaluate_fitness(self):
        for individual in self.population:
            self.fitness(individual)

        self.population = sorted(self.population, key= lambda d: d.fitness, reverse=True)

    #gives each indiviudal in the population a fitness score. We are 
    # going to create a machine learning model to do this for us later. 
    # For now set the fitness equal to the number of points
    def fitness(self, individual):
         individual.fitness = len(individual.points)