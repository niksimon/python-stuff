"""
Find divisible triples in array
[1, 2, 3, 4, 5, 6]

[1, 2, 3], [1, 2, 4], [1, 2, 6], [2, 4, 6]
"""

def solution(l):
    total = 0
    counter = [0] * len(l)
    for i in range(0, len(l)):
        for j in range(0, i):
            if (l[i] % l[j] == 0):
                counter[i] += 1
                total += counter[j]
    return total
        

print(solution([1,1,1]))