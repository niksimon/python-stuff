def solution(l):
    l.sort(key=lambda s: list(map(int, s.split('.'))))
    return l

print(solution(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]))