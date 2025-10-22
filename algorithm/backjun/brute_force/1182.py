# 백준 https://www.acmicpc.net/problem/1182

N, S = input().split()
arr = list(map(int,input().split()))

answer = 0
for size in range(1, int(N) + 1):
    for start in range(int(N) - size + 1):
        if sum(arr[start:start+size]) == int(S):
            answer += 1

print(answer)

