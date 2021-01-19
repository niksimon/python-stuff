from fractions import Fraction

def transposeMatrix(m):
    return map(list,zip(*m))

def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def getMatrixDeternminant(m):
    #base case for 2x2 matrix
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c]*getMatrixDeternminant(getMatrixMinor(m,0,c))
    return determinant

def getMatrixInverse(m):
    determinant = getMatrixDeternminant(m)
    #special case for 2x2 matrix:
    if len(m) == 2:
        return [[m[1][1]/determinant, -1*m[0][1]/determinant],
                [-1*m[1][0]/determinant, m[0][0]/determinant]]

    #find matrix of cofactors
    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = getMatrixMinor(m,r,c)
            cofactorRow.append(((-1)**(r+c)) * getMatrixDeternminant(minor))
        cofactors.append(cofactorRow)
    cofactors = transposeMatrix(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c]/determinant
    return cofactors

def solution(m):
    barArray = []
    copyMatrix = m
    rowLength = len(m[0])
    zeroRowAt = 0
    insertVerticalBarAt = 0
    rowSumArray = []
    matrixQ = []
    matrixR = []
    matrixI = []

    for idx, i in enumerate(copyMatrix):
        if(i.count(0) == len(i)):
            zeroRowAt = idx
            break

    insertVerticalBarAt = rowLength - (len((m)) - zeroRowAt)

    for idx, i in enumerate(copyMatrix):
        rowSum = sum(i)
        rowSumArray.append(rowSum)
        if(len(barArray) == 0 and i.count(0) == len(i)):
            for j in range(len(i)):
                barArray.append("-")
            barArray.insert(insertVerticalBarAt, "|")
            copyMatrix.insert(idx, barArray)
        else:
            i.insert(insertVerticalBarAt, "|")

    for idx, i in enumerate(m):
        newIdentityRow = []
        if(idx == zeroRowAt):
            break
        for j in range(insertVerticalBarAt):
            if(j == idx):
                newIdentityRow.append(1)
            else:
                newIdentityRow.append(0)
        matrixI.append(newIdentityRow)
        matrixQ.append(i[0:insertVerticalBarAt])
        matrixR.append(i[insertVerticalBarAt + 1:len(i)])

    for idxi, i in enumerate(matrixQ):
        for idxj, j in enumerate(i):
            i[idxj] /= rowSumArray[idxi]

    for idxi, i in enumerate(matrixR):
        for idxj, j in enumerate(i):
            i[idxj] /= rowSumArray[idxi]

    matrixIminusQ = []
    for idxi, i in enumerate(matrixI):
        newIQrow = []
        for idxj, j in enumerate(matrixQ[idxi]):
            newIQrow.append(i[idxj] - j)
        matrixIminusQ.append(newIQrow)

    matrixF = getMatrixInverse(matrixIminusQ)
    
    finalResultMatrix = []
    for i in range(len(matrixR)):
        finalRow = []
        for j in matrixR[i]:
            finalRow.append(0)
        finalResultMatrix.append(finalRow)

    for i in range(len(matrixF)):
        for j in range(len(matrixR[0])):
            for k in range(len(matrixR)):
                finalResultMatrix[i][j] += matrixF[i][k] * matrixR[k][j]
    
    finalRow = finalResultMatrix[0]

    denominators = []
    finalResult = []
    for i in finalRow:
        fraction = Fraction.from_float(i).limit_denominator()
        if(not i == 0):
            finalResult.append([int(str(fraction).split("/")[0]), int(str(fraction).split("/")[1])])
            denominators.append(int(str(fraction).split("/")[1]))
        else:
            finalResult.append([int(i), int(i)])
        
    maxDenominator = max(denominators)
    for idx, i in enumerate(finalResult):
        if(not (i[1] == 0) and (i[1] < maxDenominator)):
            multiply = maxDenominator / i[1]
            finalResult[idx][0] = int(finalResult[idx][0] * multiply)
            finalResult[idx][1] = maxDenominator

    output = []
    for i in finalResult:
        output.append(i[0])
    output.append(maxDenominator)

    return output
    
#print(solution([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]]))
print(solution([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))