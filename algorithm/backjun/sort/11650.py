# 백준 : https://www.acmicpc.net/problem/11650

def solve(arr):
    pairs = []
    for item in arr:
        x, y = map(int, item.split())
        # 튜플로 넣기
        # 튜플은 : 순서가 있음 (첫 번째 요소로 먼저 정렬, 같으면 두 번째 요소로 정렬)
        pairs.append((x, y))

    pairs.sort()

    for x, y in pairs:
        print(x, y)

    return

N = input()
initial_arr = [input() for _ in range(int(N))]
solve(initial_arr)