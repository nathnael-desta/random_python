import math
import random

# Problem Parameters
POINTS = [(0, 0), (1, 5), (5, 3), (3, 1), (2, 2), (3,6), (8,7), (2,6), (10,0)]

POP_SIZE = 1000  # Population size
GEN_COUNT = 5000  # Number of generations

# Generate path by randomizing order
def generate_path(points):
    # shuffle after the start because we always start from one point
    start, rest = points[0], points[1:]
    random.shuffle(rest)
    return [start] + rest

# Calculate fitness by adding up distance between adjacent points
def fitness(path):
    total_distance = sum(math.dist(path[i - 1], path[i]) for i in range(len(path))) # adds -1th index and 0 index distance to signify return trip
    return total_distance

# select the better half paths of the population
def select(population):
    middle = len(population) // 2
    # splits population in the middle and compares complementary points
    return [population[i] if fitness(population[i]) < fitness(population[i + middle]) else population[i + middle] for i in range(middle)] 

# creates a child from two parents
def createChild(parent1, parent2):
    start = random.randint(0, len(parent1) - 1)
    finish = random.randint(start, len(parent1))

    # keeps the postion of a section from parent1 
    sub_routes_from_parent1 = parent1[start:finish]
    remaining_path_from_parent2 = [path for path in parent2 if path not in sub_routes_from_parent1]

    child = []
    # while keeping the position of the section intact, adds the rest
    for i in range(len(parent1)):
        if start <= i < finish:
            child.append(sub_routes_from_parent1.pop(0))
        else:
            child.append(remaining_path_from_parent2.pop(0))
    return child

# crossover within the population
def crossover(population):
    middle = len(population) // 2
    parents = [(population[i], population[i + middle]) for i in range(middle)]
    children = []
    # creates 4 crossover children to replace population
    for parent1, parent2 in parents:
        children.append(createChild(parent1, parent2))
        children.append(createChild(parent1, parent2))
        children.append(createChild(parent2, parent1))
        children.append(createChild(parent2, parent1))
    return children

# Mutates path in a population by swapping two points based on mutation rate
def mutate(population, mutation_rate):
    mutations = []
    for path in population:
        if random.random() < mutation_rate:
            index1, index2 = random.randint(1, len(path) - 1), random.randint(1, len(path) - 1)
            path[index1], path[index2] = path[index2], path[index1]
        mutations.append(path)
    return mutations



def traveling_salesman_ga():
    # generate population
    population = [generate_path(POINTS) for _ in range(POP_SIZE)]
    mutation_rate = 0.8

    for i in range(GEN_COUNT):
        better_half = select(population)
        children = crossover(better_half)
        population = mutate(children, mutation_rate)
        # prints progress and exponentially decreases mutation_rate as the generation progresses
        if (i % 100 == 0): 
            print("generation", i, "best fit", fitness(max(population, key=fitness)))
            mutation_rate *= 0.4
    
    best_individual = max(population, key=fitness)
    best_value = fitness(best_individual)

    return best_value, best_individual

# shows the average fitness of taking a random path
def random_path_fitness():
    # generate population
    population = [generate_path(POINTS) for _ in range(POP_SIZE)]
    avg_fitness = sum(fitness(path) for path in population) / POP_SIZE  # avg fitness of a random population 
    return avg_fitness



print(random_path_fitness())
print(traveling_salesman_ga())

# shows a change of fitness from around 49.46 in the random choice to around 32.794 in the best fit