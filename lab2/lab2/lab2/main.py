import problem
import myEA
N = 10
seed = 42
populationSize = 20
offspringSize = 4
generatorsSize = 50
myProblem = problem.Problem(N, seed)
ea = myEA.EA(N, populationSize, offspringSize, generatorsSize, myProblem.setOfProblem)
print(ea.listOfIndevidualsAndTheirFitness)
print(ea.rankedListOfIndevidualsAndTheirFitness)
print(ea.roulletWheelOfIndevidualsAndTheirFitness)