class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string

    def row(self, index):
        newArray = []
        result = []
        # append rows from the matrix to newArray
        for row in self.matrix_string.split("\n"):
            newArray.append(row.split())
        # append to result the value of the chosen row, converted to int
        for row in range(len(newArray[0])):
            result.append(int(newArray[index-1][row]))
        return result
    
    def column(self, index):
        newArray = []
        result = []
        # append rows from the matrix to newArray
        for row in self.matrix_string.split("\n"):
            newArray.append(row.split())
        # append to result the value of the chosen column, converted to int
        for row in range(len(newArray)):
            result.append(int(newArray[row][index-1]))
        return result
