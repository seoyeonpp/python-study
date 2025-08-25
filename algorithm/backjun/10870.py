# 재귀함수
# 백준 : https://www.acmicpc.net/problem/10870
# --------------------------------------------
n = int(input())
# 1. 반복문을 통한 피보나치 구하기 - O(n)
arr = [-1] * (n+2) # -1은 피보나치에서 절대 나올 수 없는 수여서 초기값으로 해줌. n+1로 하면 n이 0일때 오류가 발생.
arr[0] = 0
arr[1] = 1
for i in range(2,n+1):
    arr[i] = arr[i-1] + arr[i-2]
print(arr[n])

# 2. 재귀함수 - O(2^n)
def fibonacci(x):
    # base case
    if x== 0:
        return 0
    if x == 1:
        return 1
    # recursive case
    return fibonacci(x- 2) + fibonacci(x - 1)
print(fibonacci(n))

# 3. 재귀함수 + 메모이제이션 - O(n) : 중복된 계산을 하지 않게 하기
def fibonacci_ver2(x):
    global arr2

    # base case
    # 값이 있으면 해당 값 리턴
    if arr2[x] != -1:
        return arr2[x]
    # recursive case
    # 값 저장
    arr2[x] = fibonacci_ver2(x-1) + fibonacci_ver2(x-2)
    return arr2[x]

arr2 = [-1] * (n+2)
arr2[0] = 0 # base case
arr2[1] = 1 # base case
print(fibonacci_ver2(n))
