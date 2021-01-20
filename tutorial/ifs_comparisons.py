def max_two(n1, n2):
    return n1 if n1 > n2 else n2

def max_num(num1, num2, num3):
    max = num1
    if num2 > max:
        max = num2
    if num3 > max:
        max = num3
    return max

def max_nums(*nums):
    return max(nums)

print(max_two(1, 5))
print(max_num(3, 7, 4))
print(max_nums(3, 7, 4, 6, 12, 22, 67))