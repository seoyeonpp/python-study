import algorithm

# 브루트포스 알고리즘
#  Brute(무식한) + Force(힘) 으로 무식하게 모든 경우를 확인한다는 의미
# 추상적 알고리즘이기 때문에 구체적으로 쓰이는 상황을 정의하긴 어려움 (접근방식에 더 가까움)

# [문제]
# 자연수 N이 주어지면, 1부터 N이하의 자연수 중에서 소수(prime number)의 개수를 출력하는 프로그램을 작성하시오.
# (단, N은 1,000 이하의 자연수이고, 시간 제한은 1초이다.)
# 시간 제한이 1초이므로, 약 1억 번의 연산을 넘기면 안 됨.

# 근데 사실 소수찾는건 에라토스테네스의 체 알고리즘을 활용하는게 O(N log(logN)) 으로 더 빠름
@algorithm.helper.time_logger
def brute_force(n):
    result = 0
    for i in range(1, n+1): # O(n)
        if i == 1: # 1은 소수가 아님
            continue

        is_prime = True

        for j in range(2,i):
            if i % j == 0:
                is_prime = False

        if is_prime:
            result += 1
    return result


# 그리디 알고리즘
# Greedy Algorithm (탐욕 알고리즘)
# 매 순간에서 가장 최선의 선택을 한다는 의미 = 문제에서의 최적해

# [문제]
# 동전 1원, 2원, 4원을 가지고 N원을 만들어야 한다.
# 최소한의 동전의 개수로 N원을 만드는 경우를 출력하는 프로그램을 적성하시오. 답이 여러 가지인 경우 아무 경우나 출력하시오.
# (단, N은 1,000,000 이하의 자연수이고, 시간 제한은 1초이다.)
# 시간 제한이 1초이므로, 약 1억 번의 연산을 넘기면 안 됨.
def greedy(n):
    coins = [1, 2, 4] # 동전 종류
    result = 0

    coins_dict = {1: 0, 2: 0, 4: 0} # 동전 개수 저장용
    for coin in reversed(coins): # 큰 동전부터 차례로 확인
        if n == 0:
            break
        result += n // coin # 몫을 더함
        coins_dict[coin] += n // coin # 동전 개수 업데이트
        n %= coin # 나머지로 업데이트

    return result, coins_dict
# 만약 동전이 1원, 3원, 4원이면 그리디알고리즘으로 풀수 없다.
# 예를 들어 6원을 만들때 4+1+1 의 결과를 도출할텐데, 실제로는 3+3 이라는 더 좋은 경우가 존재한다. -> DP 알고리즘으로 풀어야함.

# DP 알고리즘
# Dynamic Programming (동적 프로그래밍)
# DP는 문제를 작은 부분 문제로 나누어 해결하는 알고리즘 (복잡한 문제를 간단한 여러 개의 문제로 나누어 푸는 기법)
# 메모이제이션 기법을 활용 - 한번 계산한 결과를 저장해두었다가 다시 씀으로써 중복 계산을 방지하는 기법
# 핵심은 문제의 재귀적인 구조를 찾는데에 있음!
# 1. 문제의 재귀적인 구조 파악
# 2. 수식으로 표현
# 3. 초기값 처리

# [문제]
# 동전 1원, 3원, 4원을 가지고 N원을 만들어야 한다.
# 최소한의 동전의 개수로 N원을 만드는 경우를 출력하는 프로그램을 적성하시오. 답이 여러 가지인 경우 아무 경우나 출력하시오.
# (단, N은 1,000,000 이하의 자연수이고, 시간 제한은 1초이다.)
# 시간 제한이 1초이므로, 약 1억 번의 연산을 넘기면 안 됨.
def dp(n):
    coins = [1, 3, 4]
    f = [float('inf')] * (n + 1) # n까지의 동전 개수 저장용
    f[0] = 0

    for i in range(1, n + 1):
        for coin in coins:
            if i - coin >= 0:
                f[i] = min(f[i], f[i - coin] + 1)

    return f[n] # 최소 동전 개수 출력

# gpt 답변
def min_coin_count(N):
    coins = [1, 3, 4]
    dp = [float('inf')] * (N + 1)
    prev = [-1] * (N + 1)  # 경로 추적용

    dp[0] = 0  # 0원을 만들 때 필요한 동전 수는 0

    for i in range(1, N + 1):
        for coin in coins:
            if i - coin >= 0 and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                prev[i] = i - coin  # 어떻게 왔는지 저장

    # 결과 출력
    print(f"최소 동전 개수: {dp[N]}")

    # 경로 추적
    path = []
    curr = N
    while curr > 0:
        path.append(curr - prev[curr])  # 사용된 동전
        curr = prev[curr]

    print(f"사용된 동전들: {path[::-1]}")  # 앞에서부터 보기 좋게 뒤집기

if __name__ == "__main__":
    n = 1000
    result = 0

    print("1부터", n, "까지의 소수 개수:", brute_force(n)) # 실행 시간: 0.024345초
    print("11원을 만들기 위한 동전 개수:", greedy(11)[0], "개", greedy(11)[1])
    print("6원을 만들기 위한 동전 개수:", dp(6), "개")
    min_coin_count(6)