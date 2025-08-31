# 백준 : https://www.acmicpc.net/problem/4779
# 0 <= N <= 12

# bottom-up 방식 - 가장 작은단위부터 시작. 이미 계산한 결과를 저장해두고 재사용. 반복문으로 구현
# 시간복잡도 O(3^N)
ans = ['' for _ in range(13)] # 0~12 까지 만듦
ans[0] = '-'
for i in range(1,13):
    ans[i] = ans[i-1] + (' ' * (3**(i-1))) + ans[i-1]

while True:
    try:
        N = int(input())
        print(ans[N])
    except:
        break

# 재귀함수 방식
# 큰 부분에서 시작해서 작은 부분을 구하는 top-down 방식
# 시간 복잡도 O(3^N)
def func(k):
    # base case
    if k==0:
        return '-'

    # recursive case
    return  func(k-1) + " "* (3**(k-1)) + func(k-1)

while True:
    try:
        N = int(input())
        print(func(N))
    except:
        break

