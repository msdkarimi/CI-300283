import problem
import myEA
import numpy
N = 10
seed = 42
populationSize = 6
offspringSize = 2
generatorsSize = 1000
myProblem = problem.Problem(N, seed)
print(myProblem.setOfProblem)
ea = myEA.EA(N, populationSize, offspringSize, generatorsSize, myProblem.setOfProblem)
print(ea.listOfIndevidualsAndTheirFitness)
print(ea.rankedListOfIndevidualsAndTheirFitness)
print(ea.roulletWheelOfIndevidualsAndTheirFitness)
ea.breeding()
print(ea.rankedListOfIndevidualsAndTheirFitness)
result = ea.rankedListOfIndevidualsAndTheirFitness
indexOfsolution = list(result[1].genome)
index2 = [27,26,29,3,41,41,6,3,25,21]
NParrayOfSet = numpy.array(myProblem.setOfProblem, dtype=set)
print(NParrayOfSet[index2])
print(NParrayOfSet[indexOfsolution])



