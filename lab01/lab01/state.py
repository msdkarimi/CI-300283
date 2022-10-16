import numpy

class State:
    def __init__(self, data: numpy.ndarray):
        self._data = data

    def __hash__(self):
        return hash(bytes(self._data))
    #
    def __eq__(self, other):
        return bytes(self._data) == bytes(other._data)

    def __lt__(self, other):
        return bytes(self._data) < bytes(other._data)
    #
    def __str__(self):
        return str(self._data)

    def __repr__(self):
        return repr(self._data)

    def __len__(self):
        return len(self._data)

    def contain(self):
        return self._data

    def copyData(self):
        return self._data.copy()

    def createSet (self, x, y):
        return set

