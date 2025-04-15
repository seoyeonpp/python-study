import random
import algorithm

"""
탐색 알고리즘 예제 코드
"""

@algorithm.helper.time_logger
def linear_search(arr, target):
    # 선형 탐색 : 순서대로 하나씩 비교
    # 최악, 평균, 최선 - O(n)
    for i in range(len(arr)):
        if arr[i] == target:
            return i # 찾은 인덱스
    return -1 # 찾지 못함

@algorithm.helper.time_logger
def binary_search(arr, target):
    print("정렬된 arr:", arr)
    # 정렬된 배열에서만 쓸 수 있음!!
    # 배열을 반으로 나누고, 중앙값과 비교
    # 시간복잡도 O(log n)
    left, right = 0, len(arr) - 1

    while left <= right: # 범위가 겹치지 않을때까지 반복
        mid = (left + right) // 2
        if arr[mid] == target: # 중간값이 target과 같으면 바로 반환
            return mid
        elif arr[mid] < target: # 중간값이 target보다 작으면 왼쪽은 버리고 오른쪽만 탐색
            left = mid + 1
        else: # 중간값이 target보다 크면 오른쪽은 버리고 왼쪽만 탐색
            right = mid - 1
    return -1

@algorithm.helper.time_logger
def binary_search_recursive(arr, target, left, right):
    # 재귀적으로 이진 탐색
    if left > right: # 범위가 겹치지 않을때까지 반복
        return -1

    mid = (left + right) // 2
    if arr[mid] == target: # 중간값이 target과 같으면 바로 반환
        return mid
    elif arr[mid] < target: # 중간값이 target보다 작으면 왼쪽은 버리고 오른쪽만 탐색
        return binary_search_recursive(arr, target, mid + 1, right)
    else: # 중간값이 target보다 크면 오른쪽은 버리고 왼쪽만 탐색
        return binary_search_recursive(arr, target, left, mid - 1)

# 파라메트릭 서치
# 답이 되는 값을 직접 찾지 않고, 조건을 만족하는 값을 이분 탐색으로 찾는 기법
# 예를 들어, 특정 조건을 만족하는 가장 작은 값이나 가장 큰 값을 찾는 경우에 유용함
# 최소한읭 000, 가장 큰 000까지 가능, 이 조건을 만족하는 최소/최대값은? 이런말 들어가면 거의...

# [문제] 나무 자르기
# 높이가 서로 다른 나무가 N개 있다.
# 톱의 높이 H를 정해서 자르면, H 이상인 나무는 자르고,
# 그 아래는 그대로 둔다. 자른 나무의 총 길이가 M 이상이 되도록 하고 싶다.
# → 가능한 H 중에서 최댓값을 구해라!
trees = [20, 15, 10, 17]
M = 7
def cut_tree(H):
    total = 0
    for tree in trees:
        if tree > H:
            total += tree - H
    return total >= M

def find_max_height(low, high):
    # 이분 탐색으로 최대 높이 찾기
    while low <= high:
        mid = (low + high) // 2
        if cut_tree(mid): # 조건을 만족하면 높이를 높여야함
            low = mid + 1
        else: # 조건을 만족하지 않으면 높이를 낮춰야함
            high = mid - 1
    return high # 최댓값 반환


if __name__=="__main__":
    random_array = random.sample(range(100), 30)
    random_target = random.randint(1,100)
    sorted_random_array = sorted(random_array)
    print("찾을 배열: ", random_array)
    print("찾을 값: ", random_target)
    print("---------------------------------------")

    print(f"선형탐색 결과 : {linear_search(random_array,random_target )}") # 실행 시간: 0.000002초
    print(f"이진탐색 (반복문) 결과 : {binary_search(sorted_random_array,random_target )}") # 실행 시간: 0.000008초
    print(f"이진탐색 (재귀) 결과 : {binary_search_recursive(sorted_random_array,random_target, 0, len(sorted_random_array) - 1 )}") # 실행 시간: 0.000011초
    # 재귀가 반복문보다 조금 느림
    # 재귀는 호출될때마다 새로운 스택 프레임이 쌓임 (시간 + 메모리 오버헤드 발생)
    # python에서는 깊은 재귀는 RecursionError 발생 가능성 있음! 최대한 반복문으로..

    low, high = 0, max(trees)
    print(f"나무 자르기 문제의 최대 높이: {find_max_height(low, high)}")
