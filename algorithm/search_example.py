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
