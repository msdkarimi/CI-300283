import itertools
from operator import xor
import random
from RowObjectsPair import RowObjectsPair


class MyNim:

    def __init__(self, numRows : int, k : int = None )-> None:
        self._rows = [(i*2)+1 for i in range(numRows)]
        self._k = k
        self.inferedStatus = dict()

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


    def nimming(self, strategy :RowObjectsPair) -> None:
        row =  strategy.row
        numObjects = strategy.numberOfObject
        # assert self._rows[row] >= numObjects
        # assert self._k is None or numObjects <= self._k
        self._rows[row] -= numObjects

    def doNimming(self):
        strategies = [self.pureRandomStrategy, self.pureRandomStrategyPluseWhole]
        print(f"initial board : {self._rows}")
        player = 0
        while self:
            strategy = strategies[player]()
            self.nimming(strategy)
            print(f" PLayer: {player}, Board: {self._rows}")
            player = 1 - player
        print(f"winner is player {player}")



    def inferableInformation(self) -> None:
        self.inferedStatus["evenRows"] = [count  for count,rowValue in enumerate(self._rows) if rowValue%2]
        self.inferedStatus["oddRows"] = [count for count, rowValue in enumerate(self._rows) if not rowValue % 2]
        self.inferedStatus["nimSim"] = self.nimSum()
        self.inferedStatus["longets"] = self._rows.index(max(self._rows, key= lambda i:i))
        self.inferedStatus["shortest"] = self._rows.index(min(self._rows, key=lambda i: i))
        self.inferedStatus["ifRowsAreEven"] = len([count  for count,rowValue in enumerate(self._rows) if rowValue%2])%2 == 0




    def pureRandomStrategy(self)-> RowObjectsPair:
        selectedRow = random.choice([row for row, count in enumerate(self._rows) if count > 0 ])
        numberOfObjects = random.randint(1,self._rows[selectedRow])
        return RowObjectsPair(selectedRow, numberOfObjects)

    def pureRandomStrategyPluseWhole(self)-> RowObjectsPair:
        selectedRow = random.choice([row for row, count in enumerate(self._rows) if count > 0 ])
        numberOfObjects = self._rows[selectedRow]
        return RowObjectsPair(selectedRow, numberOfObjects)


    def nimSum(self) -> list:
        *_, result = itertools.accumulate(self._rows, xor)
        return result