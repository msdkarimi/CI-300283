import problem
import myEA
import numpy
N = 200
seed = 42
populationSize = 15
problemSize = 10
offspringSize = 6
generatorsSize = 500
myProblem = problem.Problem(N, seed)
ea = myEA.EA(problemSize, populationSize, offspringSize, generatorsSize, myProblem.setOfProblem)
print(ea.roulletWheelOfIndevidualsAndTheirFitness)
print(ea.rankedListOfIndevidualsAndTheirFitness)
result = ea.rankedListOfIndevidualsAndTheirFitness
indexOfsolution = list(result[0].genome)
NParrayOfSet = numpy.array(myProblem.setOfProblem, dtype=set)
solution = NParrayOfSet[indexOfsolution]
print(solution)



