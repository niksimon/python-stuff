import math

def how_many_times(a, b):
    count = set()
    
    diff = abs(a - b)
    m = min(a, b)
    
    for i in range(1, int(math.sqrt(diff)) + 1):
        if(diff % i == 0 and i <= m):
            count.add(i)
            count.add(diff / i)
    
    return len(count)

#how_many_times(20, 9008)
print(how_many_times(9, 8997))
#how_many_times(743474089202, 405656018150)