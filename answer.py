import math
import random

# Problem Parameters
POINTS = [(0, 0), (1, 5), (5, 3), (3, 1), (2, 2)]

POP_SIZE = 2000  # Population size
MUTATION_RATE = 0.1  # Probability of mutation
GEN_COUNT = 100  # Number of generations

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

# Select best path out of random grouping
def select(population):
    tournament = random.sample(population, 5)
    return max(tournament, key=fitness)

def crossover(parent1, parent2):
    start = random.randint(0, len(parent1) - 1)
    finish = random.randint(start, len(parent1))
    sub_routes_from_parent1 = parent1[start:finish]
    remaining_path_from_parent2 = list([path for path in parent2 if path not in sub_routes_from_parent1]) 
    child = [sub_routes_from_parent1.pop(0) if start <= i < finish else remaining_path_from_parent2.pop(0) for i in range(len(parent1))]
    return child

# def crossover(parent1, parent2):
#     start = random.randint(0, len(parent1) - 1)
#     finish = random.randint(start, len(parent1))
#     sub_routes_from_parent1 = parent1[start:finish]
#     remaining_path_from_parent2 = list([path for path in parent2 if path not in sub_routes_from_parent1]) 
#     child = [sub_routes_from_parent1.pop(0) if start <= i < finish else remaining_path_from_parent2.pop(0) for i in range(len(parent1))]
#     return child


# # Mutates path by swapping two points based on mutation rate
# def mutate(path):
#     for i in range(len(path)):
#         if (random.random() < MUTATION_RATE):
#             rand_point = random.randint(1, len(POINTS) - 1)
#             path[i], path[rand_point] = path[rand_point], path[i]
#     return path

# Mutates path by swapping two points based on mutation rate
def mutate(path):
    if random.randint(0, 1000) < 9:
        index1, index2 = random.randint(1, len(path) - 1), random.randint(1, len(path) - 1)
        path[index1], path[index2] = path[index2], path[index1]
    return path



def traveling_salesman_ga():
    # generate population
    population = [generate_path(POINTS) for _ in range(POP_SIZE)]

    for _ in range(GEN_COUNT):
        new_population = []

        # take select best parents, crossover them an return their mutated children
        for _ in range(POP_SIZE):
            parent1, parent2 = select(population), select(population)
            child = crossover(parent1, parent2)
            new_population.extend([mutate(child)])
        population = new_population
    
    best_individual = max(population, key=fitness)
    best_value = fitness(best_individual)

    return best_value, best_individual


def random_path_fitness():
    # generate population
    population = [generate_path(POINTS) for _ in range(POP_SIZE)]
    print("population", len(population), POP_SIZE)
    avg_fitness = sum(fitness(path) for path in population) / POP_SIZE
    return avg_fitness



print(random_path_fitness())
print(traveling_salesman_ga())
# best result i got 
# [(0, 0), (1, 5), (5, 3), (3, 1), (2, 2)] -> [(0, 0), (5, 3), (2, 2), (3, 1), (1, 5)], 19.97859858597914

# print([(0, 0), (1, 5), (5, 3), (3, 1), (2, 2)])
# print(mutate([(0, 0), (1, 5), (5, 3), (3, 1), (2, 2)]))