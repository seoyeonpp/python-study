# 백준 : https://www.acmicpc.net/problem/10974


def permutation(level):
    if level == N:
        print(*selected)
        return

    for i in range(1,N+1):
        if not isChoose[i-1]:
            isChoose[i-1] = True
            selected.append(i)
            # 재귀
            permutation(level+1)
            # 백트래킹
            isChoose[i - 1] = False
            selected.pop()


N = int(input())
selected=[]
isChoose = [False] * N

permutation(0)