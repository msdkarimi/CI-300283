import problem
import myEA
seed = 42
Ns = [5, 10, 20, 100, 500, 1000]
populationSizes = [10, 10, 10, 20, 30, 200]
problemSizes = [4, 4, 4, 7, 10, 13]
offspringSizes = [5, 5, 5, 10, 15, 50]
generatorsSize = 500
for index in range(len(Ns)):
    myProblem = problem.Problem(Ns[index], seed)
    ea = myEA.EA(problemSizes[index], populationSizes[index], offspringSizes[index], generatorsSize, myProblem.setOfProblem)
    print(ea.resultFitness)
    print(ea.coveredLists)




