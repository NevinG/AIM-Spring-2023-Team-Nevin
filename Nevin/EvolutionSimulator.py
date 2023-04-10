import numpy
from Individual import Individual
from IPython.display import display # to display images
from tensorflow import keras
import tensorflow as tf
import copy
import imagehash

class EvolutionSimulator:
    def __init__(self, pop_size):
        self.model = keras.models.load_model("my_model")
        self.POPULATION_SIZE = pop_size
        self.population = [] #population of individuals
        self.create_population()
        self.evaluate_fitness()

    #should remove the second half of self.population [a,b,c,d] 
    # after kill_population = [a,b]
    def kill_population(self):
        self.population = self.population[:len(self.population) // 2]

    #doubles the population. For each indivuals in self.population 
    # make an identical copy of them, and then call the .mutate method 
    # on that individual
    def reproduce(self):
        n = len(self.population)
        while(n < self.POPULATION_SIZE):
            for i in range(n):
                newIndivual = copy.deepcopy(self.population[i])
                newIndivual.mutate()
                self.population.append(newIndivual)
            n = len(self.population)
        self.evaluate_fitness()

    def advance_generation(self):
        while True:
            newIndivual = copy.deepcopy(self.population[0])
            newIndivual.mutate()
            self.fitness2(newIndivual)
            if newIndivual.fitness > self.population[0].fitness:
                self.population[0] = newIndivual
                return

    #create self.POPULATION_SIZE individuals add add them to self.population
    def create_population(self):
        for i in range(self.POPULATION_SIZE):
            self.population.append(Individual())

    #call the generate_image method on each individual
    def show_images(self):
        for person in self.population:
            display(person.generate_image())
            
    #display the first and last image only
    def show_first_and_last_image(self):
        display(self.population[0].generate_image())
        print(self.population[0].fitness)
        display(self.population[self.POPULATION_SIZE - 1].generate_image())
        print(self.population[self.POPULATION_SIZE - 1].fitness)
    
    #display the first image only
    def show_first_image(self):
        display(self.population[0].generate_image())
        print(self.population[0].fitness)
    
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
         image = individual.generate_image()
         img_array = tf.keras.utils.img_to_array(image)
         img_array = tf.expand_dims(img_array, 0) # Create a batch
         fitness = self.model.predict(img_array, verbose = 0)
         individual.fitness = fitness[0][0]

    #uses a target image to deduce fitness
    def fitness2(self, individual):
        hash0 = imagehash.average_hash(individual.generate_image())
        hash1 = imagehash.average_hash(self.target_image) 
        individual.fitness = -1 * abs(hash0 - hash1)

    
    def set_fitness_target_image(self, image):
        self.target_image = image
        self.fitness2(self.population[0])

        