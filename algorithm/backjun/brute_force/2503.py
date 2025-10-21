# 백준 : https://www.acmicpc.net/problem/2503

from itertools import permutations

N = int(input())
num_list = [input().split() for _ in range(0,N)]

answer = 0
# 0은 나오면 안되니까 1~9까지로 순열
for i in permutations(range(1,10),3):
    valid = True

    for j in range(N):
        target,strike,ball = num_list[j]
        strike = int(strike)
        ball = int(ball)
        # temp 설정
        tmp_strike = tmp_ball = 0

        # 3자리수 비교
        for k in range(3):
            if i[k] == int(target[k]):
                tmp_strike += 1
            elif str(i[k]) in str(target):
                tmp_ball += 1

        # 하나라도 안같으면 종료
        if tmp_strike != strike or tmp_ball != ball:
            # N개중에 1개라도 틀렸으니까 이번 순서 숫자는 끝! 종료처리
            valid = False
            break
    if valid:
        # N개중에 모든 조건을 만족한 숫자는 답이 될 경우의 수에 추가
        answer += 1
print(answer)


