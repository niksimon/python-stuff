import time
start_time = time.time()

def solution(s):
    startIncludingFromLeft = False
    numberOfLastRight = 0

    fromLeftToRightReserved = 0
    fromRightToLeftReserved = 0

    lastMovement = "<"

    score = 0

    c = ''
    i = -1

    for c in s:
        if (c == "-" or (not startIncludingFromLeft and c == "<")):
            pass
        else:
            startIncludingFromLeft = True

            if (c == ">"):
                fromRightToLeftReserved = 0
                fromLeftToRightReserved += 1
                numberOfLastRight += 1
                lastMovement = c
            else:
                numberOfLastRight = 0
                fromRightToLeftReserved += 1

            if (c != lastMovement and c == "<"):
                score += fromLeftToRightReserved * 2

        i += 1

    return score


print(solution(">>-<>-->>-<->><<>-<><--><>><<>-<<<--<<->-><>->><><-><><>"))

print("--- %s seconds ---" % (time.time() - start_time))
