import copy
from collections import namedtuple, Counter
import random
from functools import cmp_to_key

Individual = namedtuple("Individual", ["genome", "fitness"])
class EA:
    def __init__(self, problemSize, populationSize, offspringSize, generatorsSize, setOfProblem):
       self.problemsize = problemSize
       self.populationSize = populationSize
       self.offspringSize = offspringSize
       self.generatorsSize = generatorsSize
       self.listOfIndevidualsAndTheirFitness = list()
       self.rankedListOfIndevidualsAndTheirFitness = list()
       self.roulletWheelOfIndevidualsAndTheirFitness = list()
       self.creatingPopulation(setOfProblem)


    def creatingPopulation(self, setOfProblem ):
        # Individual = namedtuple("Individual", ["genome", "fitness"])
        for genome in [tuple([ random.choice(range(len(setOfProblem))) for _ in range(self.problemsize)]) for __ in range(self.populationSize) ]:
            self.listOfIndevidualsAndTheirFitness.append(Individual(genome, self.forEvaluation(genome, setOfProblem)))
        self.rankOfEachIndevidualByMeansOfRouletteWheelApproach()
        self.rankedAsRoulletWheel()

    def compare(self,pair1, pair2):
        _, fitness1 = pair1
        _, fitness2 = pair2
        digits1, total1 = fitness1
        digits2, total2 = fitness2

        if digits1 == digits2:
            if total1 < total2:
                return -1
            else:
                return 1
        if digits1 < digits2:
            return -1
        else:
            return 1

    def rankOfEachIndevidualByMeansOfRouletteWheelApproach(self):
        self.rankedListOfIndevidualsAndTheirFitness = sorted(self.listOfIndevidualsAndTheirFitness, key=cmp_to_key(self.compare),reverse = True)

    def rankedAsRoulletWheel(self):
        length = len(self.rankedListOfIndevidualsAndTheirFitness)
        for eachIndevidual in range(len(self.rankedListOfIndevidualsAndTheirFitness)):
           genome, _ = self.rankedListOfIndevidualsAndTheirFitness[eachIndevidual]
           length-=1
           self.roulletWheelOfIndevidualsAndTheirFitness.append(Individual(genome,length))



    def forEvaluation(state, genome, setOfProblem):
        localSet = set()
        for index in genome:
            localSet.add(setOfProblem[index])
        cnt = Counter()
        cnt.update(sum((e for e in localSet), start=()))
        return len(cnt), -cnt.total()

    def breeding(self):
        for g in range(self.generatorsSize):
            offspring = list()
            for i in range(self.offspringSize):
                if random.random() < 0.3:
                    p = self.tournament(self.listOfIndevidualsAndTheirFitness)
                    o = self.mutation(p.genome)
                else:
                    p1 = self.tournament(self.listOfIndevidualsAndTheirFitness)
                    p2 = self.tournament(self.listOfIndevidualsAndTheirFitness)
                    o = self.cross_over(p1.genome, p2.genome)
                f = self.forEvaluation(o)
                offspring.append(Individual(o, f))
            self.listOfIndevidualsAndTheirFitness += offspring
            self.listOfIndevidualsAndTheirFitness = sorted(self.listOfIndevidualsAndTheirFitness, key=lambda i: i.fitness, reverse=True)[:self.populationSize]

    def tournament(self, tournament_size=2):
        return max(random.choices(self.listOfIndevidualsAndTheirFitness, k=tournament_size), key=lambda i: i.fitness)

    def cross_over(self, g1, g2):
        cut = random.randint(0, self.problemsize)
        return g1[:cut] + g2[cut:]

    def mutation(self, g):
        point = random.randint(0, self.problemsize - 1)
        return g[:point] + (1 - g[point],) + g[point + 1:]