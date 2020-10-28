Selection functions are given below:

**Tournament Selection:
```
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
```

**Roulette Wheel Selection:
```
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
```
