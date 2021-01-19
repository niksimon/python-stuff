def convertRowPositionToOne(m, row, multiplier):
    for idx, i in enumerate(m[row]):
        m[row][idx] *= multiplier
    return m

def convertColPositionToZero(m, row, col, addition):
    for idx, i in enumerate(m[col]):
        m[col][idx] += addition * m[row][idx]
    return m

def makeIdentityMatrix(n):
    newMatrix = []
    for row in range(n):
        newRow = []
        for col in range(n):
            if(row == col):
                newRow.append(1)
            else:
                newRow.append(0)
        newMatrix.append(newRow)
    return newMatrix

def invert(m):
    matrixLength = len(m)

    for i in m:
        print(i)

    inverseMatrix = makeIdentityMatrix(matrixLength)

    for rowIdx in range(matrixLength):
        # Convert to 1 diagonally
        multiplier = 1 / m[rowIdx][rowIdx] * 1.0
        m = convertRowPositionToOne(m, rowIdx, multiplier)
        inverseMatrix = convertRowPositionToOne(inverseMatrix, rowIdx, multiplier)
        for colIdx in range(matrixLength):
            # Convert to 0 non-diagonally
            if(colIdx != rowIdx):
                addition = -m[colIdx][rowIdx]
                m = convertColPositionToZero(m, rowIdx, colIdx, addition)
                inverseMatrix = convertColPositionToZero(inverseMatrix, rowIdx, colIdx, addition)
    print()
    for i in inverseMatrix:
        print(i)

    return 0

#invert([[2,1],[3,2]])
invert([[2,1,1],[3,2,1],[2,1,2]])