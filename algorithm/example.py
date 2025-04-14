import math
from functools import reduce

# 모듈러 알고리즘
# 모듈러 연산 = “나머지만 가지고 계산하는 세계”
# 색의 원소 R, G, B가 있고, "R → G → B → R → G → ... " 순서로 성질이 바뀌는 문제가 있다고 해봅시다.
# 99번째 원소는?
def modular_algorithm(n):
    # 0: R, 1: G, 2: B
    # n % 3 = 0: R, n % 3 = 1: G, n % 3 = 2: B
    colors = ['R', 'G', 'B']
    return colors[(n-1) % 3] # n-1을 하는 이유는 0부터 시작하기 때문


# 에라토스테네스의 체 알고리즘
# 소수(Prime Number)를 빠르게 찾는 대표적인 고전 알고리즘
# 자연수 n에 대해 에라토스테네스의 체 알고리즘을 수행하고나면 2~n 범위의 자연수는 O(1)만에 소수인지 아닌지 판별 가능
# O(n log(log n))
def sieve_of_eratosthenes(n):
    # n까지의 소수를 찾는 함수
    # 시간복잡도 O(n log log n)
    is_prime = [True] * (n + 1) # 0~n까지 True로 초기화
    print("is_prime 초기화:", is_prime)
    is_prime[0], is_prime[1] = False, False # 0,1은 소수가 아님

    for i in range(2, int(math.sqrt(n)) + 1): # 2부터 n의 제곱근까지 반복 (약수는 쌍으로 존재하기때문에 루트n까지만 확인하면됨)
        if not is_prime[i]: continue
        for j in range(2 * i, n +1, i):
            is_prime[j] = False

    return [i for i in range(n + 1) if is_prime[i]] # 소수 리스트 반환

# 유클리드 알고리즘
# 두 수의 최대 공약수(GCD)를 구하는 알고리즘
def gcd(a, b):
    # a와 b의 최대 공약수 구하기
    while b != 0:
        a, b = b, a % b
    return a

# 최소공배수 (LCM) 구하기
def lcm(a, b):
    # a와 b의 최소 공배수 구하기
    return a * b // math.gcd(a, b) # 두 수의 곱을 최대공약수로 나누면 최소공배수가 나옴

# 여러수의 최소공배수
def lcm_multiple(numbers):
    # 여러 수의 최소 공배수 구하기
    return reduce(lcm, numbers) # reduce는 리스트의 모든 요소에 대해 lcm 함수를 적용하여 결과를 반환

if __name__ == "__main__":
    n = 99
    print(f"{n}번째 원소는 {modular_algorithm(n)}입니다.")
    print("------------------------------")
    print("에라토스테네스의 체 알고리즘으로 100까지의 소수 찾기")
    primes = sieve_of_eratosthenes(100)
    print("소수:", primes)
    print("------------------------------")
    print("유클리드 알고리즘으로 40과 6의 최대 공약수 구하기")
    a = 40
    b = 6
    print(f"{a}와 {b}의 최대 공약수는 {gcd(a, b)}입니다.")
    print("------------------------------")
    print(f"python 내장 함수 (Python 3.5+) : {math.gcd(a,b)}")
    print("------------------------------")
    print("40과 6의 최소 공배수 구하기")
    print(f"{a}와 {b}의 최소 공배수는 {lcm(a, b)}입니다.")
    print("------------------------------")
    print("여러 수의 최소 공배수 구하기")
    numbers = [4, 6, 8]
    print(f"{numbers}의 최소 공배수는 {lcm_multiple(numbers)}입니다.")
    print("------------------------------")

