import random
import numpy as np
import operator


class Population:
    def __init__(self, size, number):
        self.population = []
        self.number = number
        self.size = size
        self.solution = 0

    def sorted_selection(self):
        costs = list(map(lambda x: invert(cost_collision(x)), self.population))
        sum_costs = sum(costs)
        sort = random.uniform(0, sum_costs)
        choice_position = -1
        while sort > 0:
            choice_position += 1
            sort -= costs[choice_position]
        return [self.population[choice_position], self.population[choice_position - 1]]

    def crossing(self, individual_one, individual_two):  # consertar repetição linha
        index = random.randint(0, self.size)
        son_one = Individual(self.size, individual_one.chromosome[:index] + individual_two.chromosome[index:])
        son_two = Individual(self.size, individual_two.chromosome[:index] + individual_one.chromosome[index:])
        reproduction = test([son_one, son_two])
        if not reproduction:
            return "break"
        
        if random.randint(0, 2) > 1:
            population.population[0].mutation()
            population.population[1].mutation()
        
        return [son_one, son_two]

    def reproduction(self):
        print("Reproducing")
        new_individuals = []
        for i in range(int(self.size/2)):
            individuals = self.sorted_selection()
            crossed = self.crossing(individuals[0], individuals[1])
            if type(crossed) == type("str"):
                return 1
            new_individuals.extend(crossed)
        must_die = random.randint(0, self.number)  # reproduction ineffective
        self.kill(new_individuals, must_die)
        return 0

    def kill(self, population, sacrifice):
        costs = list(map(lambda x: (cost_collision(x), x), self.population))
        costs.sort(key=operator.itemgetter(0))
        for i in range(sacrifice):
            self.population.remove(costs[i][1])
        self.population.extend(population)  # no kills to new population


class Individual:
    def __init__(self, size, chromosome):
        self.chromosome = chromosome
        self.size = size

    def print_chromosome(self):
        print(self.chromosome)

    def mutation(self):
        pieces = tuple(random.sample(range(0, self.size), 2))
        piece = self.chromosome[pieces[0]]
        self.chromosome[pieces[0]] = self.chromosome[pieces[1]]
        self.chromosome[pieces[1]] = piece


def test(population):
    test = 1
    if cost_collision(population[0]) == 0:
        print("Solução 1")
        solution(population[0].chromosome, population[0])
        test = 0
    elif cost_collision(population[1]) == 0:
        print("Solução 2")
        solution(population[1].chromosome, population[1])
        test = 0
    return test


def solution(chromosome, individual):
    solution = []
    for i in range(len(chromosome)):
        solution.append([0] * len(chromosome))
    for j in range(len(chromosome)):
        solution[chromosome[j]][j] = 1
    for k in range(len(chromosome)):
        print(solution[k])
    individual.print_chromosome()
    print(cost_collision(individual))


def invert(number):
    if number > 0:
        return 1/number
    else:
        return 1


def cost_collision(individual):
    collision = 0
    dimension = individual.size
    for i in range(dimension):
        for j in range(i + 1, dimension):
            ind_i = np.array([i, individual.chromosome[i]])
            ind_j = np.array([j, individual.chromosome[j]])
            difference = abs(ind_i - ind_j)
            if difference[0] == difference[1] or ind_i[0] == ind_j[0] or ind_i[1] == ind_j[1]:
                collision += 1
    return collision


def sort_chromosome(size):
    return random.sample(range(0, size), size)


def queens_generate(number, population):
    for i in range(population.size):
        population.population.append(Individual(population.size, sort_chromosome(population.size)))


def explore(number, size, iterations):
    population = Population(size, number)
    queens_generate(number, population)
    reproduction = population.reproduction()  # variable to test solution
    print("Aqui")
    if not reproduction:
        for i in range(iterations):
            print("interando")
            continuation = population.reproduction()
            if continuation:
                break
        lasts = list(map(lambda individual: (cost_collision(individual), individual), population.population))
        lasts.sort(key=operator.itemgetter(0))
        print("Melhor solução")
        solution(lasts[len(lasts)-1][1].chromosome, lasts[len(lasts)-1][1])

def main():
    number = 4
    size = 4
    iterations = 100
    explore(number, size, iterations)


main()

