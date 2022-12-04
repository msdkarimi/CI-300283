class RowObjectsPair:
    def __init__(self, row, numberOfObject):
        self.row = row
        self.numberOfObject = numberOfObject

    def __str__(self):
        return "<STRATEGY= row: " + str(self.row) + ", objects: " + str(self.numberOfObject)+ ">"