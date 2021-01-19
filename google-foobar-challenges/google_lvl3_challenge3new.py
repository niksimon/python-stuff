import unittest
from fractions import Fraction

def makeIdentityMatrix(n):
    newMatrix = []
    for row in range(n):
        newRow = []
        for col in range(n):
            if(row == col):
                newRow.append(Fraction(1, 1))
            else:
                newRow.append(0)
        newMatrix.append(newRow)
    return newMatrix

def makeSubMatrix(m, rows, cols):
    newMatrix = []
    for row in rows:
        currentRow = []
        for col in cols:
            currentRow.append(m[row][col])
        newMatrix.append(currentRow)
    return newMatrix

def convertRowPositionToOne(m, row, multiplier):
    for idx, i in enumerate(m[row]):
        m[row][idx] *= multiplier
    return m

def convertColPositionToZero(m, row, col, addition):
    for idx, i in enumerate(m[col]):
        m[col][idx] += addition * m[row][idx]
    return m

def findLeastCommonMultiple(arr):
    maxLCM = max(arr)
    allDivisible = True
    for i in arr:
        if(not maxLCM % i == 0):
            allDivisible = False
            break

    if(allDivisible):
        return maxLCM

    startMax = maxLCM
    while(not allDivisible):
        allDivisible = True
        maxLCM += startMax
        for i in arr:
            if(not maxLCM % i == 0):
                allDivisible = False
                break
    
    return maxLCM

def solution(m):
    terminalStates = []
    nonTerminalStates = []

    # Get terminal and non-terminal states
    for idx, row in enumerate(m):
        if (sum(row) == 0):
            terminalStates.append(idx)
        else:
            nonTerminalStates.append(idx)

    # If only 1 terminal state, return [1, 1]
    if(len(terminalStates) == 1):
        return [1, 1]

    # Prepare matrix with fractions and identity
    for rowIdx, row in enumerate(m):
        rowSum = sum(row)
        if(rowSum == 0):
            m[rowIdx][rowIdx] = 1
        else:
            for colIdx, col in enumerate(row):
                m[rowIdx][colIdx] = Fraction(col, rowSum)

    # Get Q matrix
    matrixQ = makeSubMatrix(m, nonTerminalStates, nonTerminalStates)

    # Get R matrix
    matrixR = makeSubMatrix(m, nonTerminalStates, terminalStates)

    # Make identity matrix
    matrixI = makeIdentityMatrix(len(matrixQ))

    # Subtract I - Q
    matrixIminusQ = []
    for rowIdx, row in enumerate(matrixI):
        newRow = []
        for colIdx, col in enumerate(matrixQ[rowIdx]):
            newRow.append(row[colIdx] - col)
        matrixIminusQ.append(newRow)

    # Invert F = I - Q
    matrixLength = len(matrixIminusQ)

    matrixF = makeIdentityMatrix(matrixLength)

    for rowIdx in range(matrixLength):
        # Convert to 1 diagonally
        multiplier = Fraction(1, matrixIminusQ[rowIdx][rowIdx])
        matrixIminusQ = convertRowPositionToOne(matrixIminusQ, rowIdx, multiplier)
        matrixF = convertRowPositionToOne(matrixF, rowIdx, multiplier)
        for colIdx in range(matrixLength):
            # Convert to 0 non-diagonally
            if(colIdx != rowIdx):
                addition = -matrixIminusQ[colIdx][rowIdx]
                matrixIminusQ = convertColPositionToZero(matrixIminusQ, rowIdx, colIdx, addition)
                matrixF = convertColPositionToZero(matrixF, rowIdx, colIdx, addition)

    # Make final result matrix same dimensions as R, set everything to 0
    finalResultMatrix = []
    for i in range(len(matrixR)):
        finalRow = []
        for j in matrixR[i]:
            finalRow.append(0)
        finalResultMatrix.append(finalRow)

    # Multiply F x R
    for i in range(len(matrixF)):
        for j in range(len(matrixR[0])):
            for k in range(len(matrixR)):
                finalResultMatrix[i][j] += matrixF[i][k] * matrixR[k][j]

    denominators = []
    for i in finalResultMatrix[0]:
        denominators.append(i.denominator)

    maxDenominator = findLeastCommonMultiple(denominators)

    finalResult = []
    for i in finalResultMatrix[0]:
        finalResult.append(i.numerator * (maxDenominator // i.denominator))
    
    finalResult.append(maxDenominator)

    return finalResult

class TestSolutions(unittest.TestCase):
    def test1(self):
        test_input = [
            [0, 2, 1, 0, 0],
            [0, 0, 0, 3, 4],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]
        self.assertEqual(solution(test_input),
                         [7, 6, 8, 21])

    def test2(self):
        test_input = [
            [0, 1, 0, 0, 0, 1],
            [4, 0, 0, 3, 2, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]
        ]
        self.assertEqual(solution(test_input), [0, 3, 2, 9, 14])

    def test3(self):
        test_input = [
            [1, 2, 3, 0, 0, 0],
            [4, 5, 6, 0, 0, 0],
            [7, 8, 9, 1, 0, 0],
            [0, 0, 0, 0, 1, 2],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]
        ]
        self.assertEqual(solution(test_input), [1, 2, 3])

    def test4(self):
        test_input = [
            [0]
        ]
        self.assertEqual(solution(test_input), [1, 1])

    def test5(self):
        test_input = [
            [0, 0, 12, 0, 15, 0, 0, 0, 1, 8],
            [0, 0, 60, 0, 0, 7, 13, 0, 0, 0],
            [0, 15, 0, 8, 7, 0, 0, 1, 9, 0],
            [23, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            [37, 35, 0, 0, 0, 0, 3, 21, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        self.assertEqual(solution(test_input), [1, 2, 3, 4, 5, 15])

    def test6(self):
        test_input = [
            [0, 7, 0, 17, 0, 1, 0, 5, 0, 2],
            [0, 0, 29, 0, 28, 0, 3, 0, 16, 0],
            [0, 3, 0, 0, 0, 1, 0, 0, 0, 0],
            [48, 0, 3, 0, 0, 0, 17, 0, 0, 0],
            [0, 6, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        self.assertEqual(solution(test_input), [4, 5, 5, 4, 2, 20])

    def test7(self):
        test_input = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        self.assertEqual(solution(test_input), [1, 1, 1, 1, 1, 5])

    def test8(self):
        test_input = [
            [1, 1, 1, 0, 1, 0, 1, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 1, 1, 1, 0, 1, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 1, 0, 1, 0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        self.assertEqual(solution(test_input), [2, 1, 1, 1, 1, 6])

    def test9(self):
        test_input = [
            [0, 86, 61, 189, 0, 18, 12, 33, 66, 39],
            [0, 0, 2, 0, 0, 1, 0, 0, 0, 0],
            [15, 187, 0, 0, 18, 23, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        self.assertEqual(solution(test_input), [6, 44, 4, 11, 22, 13, 100])

    def test10(self):
        test_input = [
            [0, 0, 0, 0, 3, 5, 0, 0, 0, 2],
            [0, 0, 4, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 4, 4, 0, 0, 0, 1, 1],
            [13, 0, 0, 0, 0, 0, 2, 0, 0, 0],
            [0, 1, 8, 7, 0, 0, 0, 1, 3, 0],
            [1, 7, 0, 0, 0, 0, 0, 2, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        self.assertEqual(solution(test_input), [1, 1, 1, 2, 5])

unittest.main()