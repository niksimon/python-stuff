"""
For input 4 >>> 4 -> 2 -> 1
For input 15 >>> 15 -> 16 -> 8 -> 4 -> 2 -> 1

Add 1 or remove 1, divide by 2 to reach 1
"""

def solution(n):
    num = int(n)
    counter = 0
    while num > 1:
        print(num)
        if(num % 2 == 0):
            num = int(num / 2)
        else:
            if(num == 3 or ((num - 1) / 2) % 2 == 0):
                num -= 1
            else:
                num += 1
        counter += 1
    print(num)
    return counter

print(solution('4'))