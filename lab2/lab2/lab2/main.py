import problem
import myEA
import numpy
N = 1000
seed = 42
populationSize = 200
problemSize = 13
offspringSize =100
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



