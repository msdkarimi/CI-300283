import problem
import myEA
import numpy
N = 20
seed = 42
populationSize = 10
problemSize = 4
offspringSize =5
generatorsSize = 500
myProblem = problem.Problem(N, seed)
ea = myEA.EA(problemSize, populationSize, offspringSize, generatorsSize, myProblem.setOfProblem)
print(ea.resultFitness)
print(ea.coveredLists)
# print(ea.roulletWheelOfIndevidualsAndTheirFitness)
# print(ea.rankedListOfIndevidualsAndTheirFitness)
# result = ea.rankedListOfIndevidualsAndTheirFitness
# indexOfsolution = list(result[0].genome)
# NParrayOfSet = numpy.array(myProblem.setOfProblem, dtype=set)
# solution = NParrayOfSet[indexOfsolution]
# print(solution)



