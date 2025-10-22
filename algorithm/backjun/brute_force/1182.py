# 백준 https://www.acmicpc.net/problem/1182

N, S = input().split()
arr = list(map(int,input().split()))

answer = 0
size = 1
pointer = 0
check_arr = []


def solve():
    global answer
    global size
    global pointer
    global check_arr

    print(f"size: {size} / pointer : {pointer} / check_arr:  {check_arr}")

    check_arr.append(arr[pointer])
    pointer += 1

    if len(check_arr) == size:
        if sum(check_arr) == S:
            answer += 1
        else:
            check_arr.pop()
            solve()

    elif pointer >= int(N):
        pointer = 0
        check_arr = []
        size += 1


solve()
print(answer)


