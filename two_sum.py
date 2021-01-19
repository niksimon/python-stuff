def two_sum(arr, s):
    sums = []
    hashTable = []

    for i in range(len(arr)):
        sumMinusEl = s - arr[i]

        if(sumMinusEl in hashTable):
            sums.append([arr[i], sumMinusEl])

        hashTable.append(arr[i])
    
    return sums

print(two_sum([2,7,11,15,3,6], 9))