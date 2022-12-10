import itertools
from operator import xor
import random
from RowObjectsPair import RowObjectsPair
from copy import deepcopy
from typing import Callable


class MyNim:

    def __init__(self, numRows : int, k : int = None )-> None:
        self._rows = [(i*2)+1 for i in range(numRows)]
        self.copyOfRows = list()
        self._k = k
        self.inferedStatus = dict()
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



    def doNimming(self):
        strategies = [self.properActionToPerformNimSum, self.evaluate({"p":random.random()})]
        print(f"initial board : {self._rows}")
        player = 0
        while self:
            if not player:
                strategy = strategies[player]()
            else:
                strategy = strategies[player]()
            self.nimming(strategy)
            print(f" PLayer: {player}, Board: {self._rows}")
            player = 1 - player
        print(f"winner is player {player}")


    def inferableInformation(self) -> None:
        self.inferedStatus["oddRows"] = [count  for count,rowValue in enumerate(self._rows) if rowValue%2]
        self.inferedStatus["evenRows"] = [count for count, rowValue in enumerate(self._rows) if not rowValue % 2]
        self.inferedStatus["nimSum"] = self.nimSum()
        self.inferedStatus["longets"] = self._rows.index(max(self._rows, key= lambda i:i))
        self.inferedStatus["shortest"] = self._rows.index(min(i for i in self._rows if i > 0))
        self.inferedStatus["ifRowsAreEven"] = len([count  for count,rowValue in enumerate(self._rows) if rowValue%2])%2 == 0
        self.inferedStatus["possible_moves"] = [(r, a1) for r,i in enumerate(self._rows) for a1 in range(i + 1) if a1 >= self.k and a1 <= a1 + 1]




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