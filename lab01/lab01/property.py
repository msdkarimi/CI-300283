class Properties:
    def __init__(self, numberOfElements, seed, finalGoal, initialList):
        self.N = numberOfElements
        self.seed = seed
        self.goal = list(finalGoal)
        self.initial = list(initialList)