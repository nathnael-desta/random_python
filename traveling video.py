import math
import random

POINTS = [(0, 0), (1, 5), (5, 3), (3, 1), (2, 2)]

POP_SIZE = 10  # Population size
MUTATION_RATE = 0.1  # Probability of mutation
GEN_COUNT = 50  # Number of generations

def generate_random_paths(total_destinations):
    random_paths = []
    for _ in range(2000):
        random_path = list(range(1, total_destinations))
        random.shuffle(random_path)
        random_path = [0] + random_path
        random_paths.append(random_path)
    return random_paths


def total_distance(points, path):
    return sum(math.dist(points[path[i - 1]], points[path[i]]) for i in range(len(path)))


def choose_survivors(points, old_generation):
    survivors = []
    random.shuffle(old_generation)
    midway = len(old_generation) // 2
    for i in range(midway):
        if total_distance(points, old_generation[i]) < total_distance(points, old_generation[i + midway]):
            survivors.append(old_generation[i])
        else:
            survivors.append(old_generation[i + midway])
    return survivors


def create_offspring(parent_a, parent_b):
    offspring = []
    start = random.randint(0, len(parent_a) - 1)
    finish = random.randint(start, len(parent_a))
    sub_path_from_a = parent_a[start:finish]
    remaining_path_from_b = list([item for item in parent_b if item not in sub_path_from_a])
    for i in range(0, len(parent_a)):
        if start <= i < finish:
            offspring.append(sub_path_from_a.pop(0))
        else:
            offspring.append(remaining_path_from_b.pop(0))
    return offspring


def apply_crossovers(survivors):
    offsprings = []
    midway = len(survivors) // 2
    for i in range(midway):
        parent_a, parent_b = survivors[i], survivors[i + midway]
        for _ in range(2):
            offsprings.append(create_offspring(parent_a, parent_b))
            offsprings.append(create_offspring(parent_b, parent_a))
    return offsprings


def apply_mutations(generation):
    gen_wt_mutations = []
    for path in generation:
        if random.randint(0, 1000) < 9:
            index1, index2 = random.randint(1, len(path) - 1), random.randint(1, len(path) - 1)
            path[index1], path[index2] = path[index2], path[index1]
        gen_wt_mutations.append(path)
    return gen_wt_mutations


def generate_new_population(points, old_generation):
    survivors = choose_survivors(points, old_generation)
    crossovers = apply_crossovers(survivors)
    print("populatoin length", len(crossovers))
    new_population = apply_mutations(crossovers)
    return new_population


def choose_best(points, paths, count):
    return sorted(paths, key=lambda path: total_distance(points, path))[:count]


def choose_worst(points, paths, count):
    return sorted(paths, reverse=True, key=lambda path: total_distance(points, path))[:count]


def choose_random(paths, count):
    return [random.choice(paths) for _ in range(count)]




def generate_path(points):
    # shuffle after the start because we always start from one point
    start, rest = points[0], points[1:]
    random.shuffle(rest)
    return [start] + rest

def fitness(path):
    total_distance = sum(math.dist(path[i - 1], path[i]) for i in range(len(path))) # adds -1th index and 0 index distance to signify return trip
    return total_distance

def random_path_fitness():
    # generate population
    population = [generate_path(POINTS) for _ in range(POP_SIZE)]
    avg_fitness = sum(fitness(path) for path in population) / POP_SIZE
    return avg_fitness

points = [(0, 0), (1, 5), (5, 3), (3, 1), (2, 2), (3,6), (8,7), (2,6), (10,0)]

def run():
    initial_population = generate_random_paths(len(POINTS))
    generations = 100  # Adjust for better results
    population = initial_population

    for _ in range(generations):
        population = generate_new_population(POINTS, population)
    
    best_path = choose_best(POINTS, population, 1)[0]
    best_distance = total_distance(POINTS, best_path)
    print("Best Path:", best_path)
    print("Total Distance:", best_distance)



print(random_path_fitness())
print(random_path_fitness())

print(run())

