import itertools
from operator import xor
import random
from RowObjectsPair import RowObjectsPair
from copy import deepcopy
from typing import Callable


class MyNim:

    def __init__(self, numRows : int, k : int = None )-> None:
        self.countOfRows = numRows
        self._rows = [(i*2)+1 for i in range(numRows)]
        self.copyOfRows = list()
        self._k = k
        self.inferedStatus = dict()
        self.inferedStatusForCopiedRows = dict()
        self.inferableInformation()

    def __bool__(self):
        return sum(self._rows) > 0

    def __str__(self):
        return "<" + " ".join(str(_) for _ in self._rows) + " >"

    @property
    def rows(self) -> tuple:
        return tuple(self._rows)

    @property
    def k(self) -> int:
        return self._k

    def deepCopyOf_rows(self):
        self.copyOfRows = deepcopy(self._rows)
        return self.copyOfRows

# 3.1, 3,2
    def nimming(self, strategy :RowObjectsPair, ifFindingNimSum = None) -> None:
        if not ifFindingNimSum:
            row =  strategy.row
            numObjects = strategy.numberOfObject
            # assert self._rows[row] >= numObjects
            # assert self._k is None or numObjects <= self._k
            self._rows[row] -= numObjects
        else:
            row = strategy.row
            numObjects = strategy.numberOfObject
            self.copyOfRows[row] -= numObjects

    def staticNimming(self, rows, strategy :RowObjectsPair):
        row = strategy.row
        numObjects = strategy.numberOfObject
        rows[row] -= numObjects
        return deepcopy(rows)

    def doNimming(self, gemone:dict = None):
        if gemone is not None:
            strategies = [self.properActionToPerformNimSum, self.evaluate(gemone)]
        else:
            strategies = [self.properActionToPerformNimSum, self.pureRandomStrategy]
        print(f"initial board : {self._rows}")
        player = 0
        while self:
            # if not player:
            #     strategy = strategies[player]()
            # else:
            strategy = strategies[player]()
            self.nimming(strategy)
            print(f" PLayer: {player}, Board: {self._rows}")
            player = 1 - player
        print(f"winner is player {player}")


    def inferableInformation(self, evaluation = False) -> None:
        if not evaluation:
            self.inferedStatus["oddRows"] = [count  for count,rowValue in enumerate(self._rows) if rowValue%2]
            self.inferedStatus["evenRows"] = [count for count, rowValue in enumerate(self._rows) if not rowValue % 2]
            self.inferedStatus["nimSum"] = self.nimSum()
            self.inferedStatus["longets"] = self._rows.index(max(self._rows, key= lambda i:i))
            # self.inferedStatus["shortest"] = self._rows.index(min(i for i in self._rows if i > 0))
            self.inferedStatus["ifRowsAreEven"] = len([count  for count,rowValue in enumerate(self._rows) if rowValue%2])%2 == 0
            self.inferedStatus["possible_moves"] = set([(r, a1) for r,i in enumerate(self._rows) for a1 in range(i + 1) if a1 >= self.k and a1 <= a1 + 1])
        else:
            self.inferedStatusForCopiedRows["oddRows"] = [count for count, rowValue in enumerate(self._rows) if rowValue % 2]
            self.inferedStatusForCopiedRows["evenRows"] = [count for count, rowValue in enumerate(self._rows) if not rowValue % 2]
            self.inferedStatusForCopiedRows["nimSum"] = self.nimSum()
            self.inferedStatusForCopiedRows["longets"] = self._rows.index(max(self._rows, key=lambda i: i))
            # self.inferedStatusForCopiedRows["shortest"] = self._rows.index(min(i for i in self._rows if i > 0))
            self.inferedStatusForCopiedRows["ifRowsAreEven"] = len([count for count, rowValue in enumerate(self._rows) if rowValue % 2]) % 2 == 0
            self.inferedStatusForCopiedRows["possible_moves"] = set([(r, a1) for r, i in enumerate(self._rows) for a1 in range(i + 1) if a1 >= self.k and a1 <= a1 + 1])


    def pureRandomStrategy(self)-> RowObjectsPair:
        selectedRow = random.choice([row for row, count in enumerate(self._rows) if count > 0 ])
        numberOfObjects = random.randint(1,self._rows[selectedRow])
        return RowObjectsPair(selectedRow, numberOfObjects)

    def pureRandomStrategyPluseWhole(self)-> RowObjectsPair:
        selectedRow = random.choice([row for row, count in enumerate(self._rows) if count > 0 ])
        numberOfObjects = self._rows[selectedRow]
        return RowObjectsPair(selectedRow, numberOfObjects)


    def nimSum(self, ifFindingNimSum = None) -> list:
        if not ifFindingNimSum:
            *_, result = itertools.accumulate(self._rows, xor)
            return result
        else:
            *_, result = itertools.accumulate(self.copyOfRows, xor)
            return result


    def properActionToPerformNimSum(self) -> RowObjectsPair:
       self.inferableInformation()
       x = self.inferedStatus["nimSum"]
       if x:
            possibleMoves = self.inferedStatus["possible_moves"]

            for rowActionPair in possibleMoves:
                _ = self.deepCopyOf_rows()
                indexOfPossibleObjects, possibleObjects = rowActionPair
                self.nimming(RowObjectsPair(indexOfPossibleObjects, possibleObjects), self.copyOfRows)
                if  not self.nimSum(self.copyOfRows):
                    self.copyOfRows = list()
                    return RowObjectsPair(indexOfPossibleObjects, possibleObjects)

            self.copyOfRows = list()
            return self.pureRandomStrategy()
       self.copyOfRows = list()
       return self.pureRandomStrategy()

    def evaluate(self, selectionThreshold: dict) -> Callable:
        def evolvable() -> RowObjectsPair:
            self.inferableInformation()
            if random.random() < selectionThreshold["p"]:
                ply = RowObjectsPair(self.inferedStatus["shortest"], random.randint(1, self._rows[self.inferedStatus["shortest"]]))
            else:
                ply = RowObjectsPair(self.inferedStatus["longets"], random.randint(1, self._rows[self.inferedStatus["longets"]]))
            return ply
        return evolvable


#3.3 MIN MAX

    def ifWinner(self, playerState):
        if playerState.count(0) == (self.countOfRows-1):
            return True


    def evaluateMinMAx(self, p0,p1):

        if self.ifWinner(p0):
            return 1
        elif self.ifWinner(p1):
            return -1
        else:
            return 0


    def minMax(self, s0, s1):
        self.inferableInformation()
        possibleActions = self.inferedStatus["possible_moves"]
        eval = self.evaluateMinMAx(s0, s1)
        if eval != 0:
            return eval

        evaluation = list()
        for possibleAction in possibleActions :
            s0 = deepcopy(s1)
            if s0[possibleAction[0]]>= possibleAction[1]:
                s0 = self.staticNimming(s0, RowObjectsPair(possibleAction[0], possibleAction[1]))
            else:
                continue
            eval = self.minMax(s1, s0)
            if type(eval) == tuple:
                _, eval = eval
            evaluation.append((possibleAction,-eval))
        return max(evaluation, key=lambda k: k[1])