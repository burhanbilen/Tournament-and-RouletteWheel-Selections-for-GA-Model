import random
from ITEM import Item

ITEMS = [Item(random.randint(0,20), random.randint(0,20)) for x in range(0,20)]

#print(ITEMS[0].value, ITEMS[0].weight)

CAPACITY = 10*len(ITEMS)

POP_SIZE = 10

ITER = 2

def fitness(target):
    total_value = 0
    total_weight = 0

    index = 0
    for i in target:
        if index >= len(ITEMS):
            break
        if i == 1:
            total_value += ITEMS[index].value
            total_weight += ITEMS[index].weight
        index += 1
    if total_weight > CAPACITY:
        return 0
    else:
        return total_value

def create_starting_population(amount):
    return [create_individuals()for x in range(0,amount)]

def create_individuals():
    return [random.randint(0,1) for x in range(0,len(ITEMS))]


def mutate(individiual):
    r=random.randint(0,len(individiual)-1)

    if individiual[r] == 0:
        individiual[r] = 1
    else:
        individiual[r] = 0


def crossover(pop):
    parent_elitism = 0.2

    parent_length = int(parent_elitism*len(pop))

    parents = pop[:parent_length]

    mutate(parents[random.randint(0,len(parents)-1)])

    children = []

    desired_lenght = len(pop)-len(parents)

    #print(desired_lenght)

    while len(children) < desired_lenght:
        p1 = pop[random.randint(0, len(parents)-1)]
        p2 = pop[random.randint(0, len(parents)-1)]
        half = int(len(p1)/2)
        child = p1[:half]+p2[:half]
        
        children.append(child)

    parents.extend(children)
    
    if ask == str(1):
        return TournamentSelection(parents, POP_SIZE)
    else:
        return RouletteWheelSelection(parents)
            

def TournamentSelection(population, tournament_size):
    best = 0
    temp = [0]
    total = list()
    for i in range(len(population)):
        temp = population[random.randint(0, tournament_size-1)]
        fit = int(fitness(temp))
        if fit > best:
            best = fit
        total.append(temp)
    return total

def RouletteWheelSelection(population):
    fit_sum = fitnessSumforRoulette(population)
    boundary = random.randint(0, fit_sum)
    partial_sum = 0
    population = sorted(population, key=lambda x:fitness(x), reverse=True)
    selected = list()
    for i in population:
        for j in range(fit_sum):
            if partial_sum < boundary:
                partial_sum += fitness(i)
            if partial_sum > boundary:
                selected.append(i)
                break
    return selected
            
def fitnessSumforRoulette(population):
    total = 0
    for i in population:
        total += fitness(i)
    return total

if __name__ == '__main__':
    ask = input("1: Tournament, 2: Roulette Wheel\n")
    population = create_starting_population(POP_SIZE)
    generation = 1
    for j in range(0, ITER):
      print("**** Generation: ****", generation)
      population = sorted(population, key=lambda x:fitness(x), reverse=True)
      for i in population:
          print("%s, fit: %s"%(str(i), fitness(i)))

      population = crossover(population)
      generation += 1

