import random

class Problem:

    def __init__(self, n, seed):
        self.prombelSize = n
        self.listOfProblem = self.myProblem(n, seed)
        self.setOfProblem = self.creatSetFromListOfProblem()

    def myProblem(self, N, seed=None):
        """Creates an instance of the problem"""

        random.seed(seed)
        return [
            list(set(random.randint(0, N - 1) for n in range(random.randint(N // 5, N // 2))))
            for n in range(random.randint(N, N * 5))
        ]

    def creatSetFromListOfProblem(self):
        sortedList = set()
        for _ in self.listOfProblem:
            sortedelement  = sorted(_)
            sortedList.add(tuple(sortedelement))
        return sorted(sortedList)
