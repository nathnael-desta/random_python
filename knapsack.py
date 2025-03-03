import random

# Problem Parameters
MAX_WEIGHT = 50
ITEMS = [
    {"weight": 10, "value": 60},
    {"weight": 20, "value": 100},
    {"weight": 30, "value": 120},
    {"weight": 40, "value": 200},
    {"weight": 5, "value": 50},
]

POP_SIZE = 10  # Population size
MUTATION_RATE = 0.1  # Probability of mutation
GEN_COUNT = 50  # Number of generations

# Generate random individual
def generate_individual():
    return [random.randint(0, 1) for _ in range(len(ITEMS))]

# Calculate fitness
def fitness(individual):
    total_weight = sum(ind * item["weight"] for ind, item in zip(individual, ITEMS))
    total_value = sum(ind * item["value"] for ind, item in zip(individual, ITEMS))
    return total_value if total_weight <= MAX_WEIGHT else 0  # Penalize overweight

# Select parents (Tournament Selection)
def select(population):
    tournament = random.sample(population, 3)
    return max(tournament, key=fitness)

# Crossover (Single Point)
def crossover(parent1, parent2):
    point = random.randint(1, len(ITEMS) - 1)
    return parent1[:point] + parent2[point:], parent2[:point] + parent1[point:]

# Mutation (Flip Bits)
def mutate(individual):
    return [bit if random.random() > MUTATION_RATE else 1 - bit for bit in individual]

# Genetic Algorithm
def knapsack_ga():
    # Initialize population
    population = [generate_individual() for _ in range(POP_SIZE)]

    for _ in range(GEN_COUNT):
        # Create next generation
        new_population = []
        for _ in range(POP_SIZE // 2):
            parent1, parent2 = select(population), select(population)
            child1, child2 = crossover(parent1, parent2)
            new_population.extend([mutate(child1), mutate(child2)])
        population = new_population

    # Get best solution
    best_individual = max(population, key=fitness)
    best_value = fitness(best_individual)

    # Output results
    selected_items = [
        ITEMS[i] for i, selected in enumerate(best_individual) if selected == 1
    ]

    return best_value, selected_items

# Run the Genetic Algorithm
best_value, selected_items = knapsack_ga()
print(f"Best value: {best_value}")
print("Selected items:", selected_items)
