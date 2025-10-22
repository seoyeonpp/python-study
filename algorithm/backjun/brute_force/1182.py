# 백준 https://www.acmicpc.net/problem/1182

from itertools import combinations

N, S = input().split()
arr = list(map(int,input().split()))

answer = 0

for count in range(1, int(N)+1):
    for combo in combinations(arr,count):
        if sum(combo) == int(S):
            answer += 1

print(answer)
