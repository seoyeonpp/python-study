import random
import algorithm

"""
정렬 알고리즘 예제 코드
"""

@algorithm.helper.time_logger
def bubble_sort(arr):
    # 버블정렬은 인접한 두값을 비교해서 큰값을 오른쪽으로 한칸씩 밀어내는 방식
    # 비교할때마다 swap
    # 평균,최악 - O(n^2), 최선 - O(n)
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1): # j는 0부터 n-i-1까지 (정렬이 완료된 값을 다시 비교할 필요가 없기 떄문에)
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j] # swap
    print("버블정렬 완료:", arr)

@algorithm.helper.time_logger
def selection_sort(arr):
    # 선택정렬은 현재 위치에서 가장 작은값을 선택해서 앞으로 가져옴
    # 한 라운드에 한번만 swap
    # 평균,최악,최선 - O(n^2)
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1,n): # i의 다음 인텍스부터 비교
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i] # swap
    print("선택정렬 완료:", arr)

@algorithm.helper.time_logger
def insertion_sort(arr):
    # 삽입정렬은 데이터를 하나씩 왼쪽의 정렬된 영역에 적절한 위치에 삽입하면서 정렬
    # 한칸씩 밀어내며 삽입
    # 값들을 한칸씩 밀기만하다가 마지막에 딱 한번 삽입함. (swap이 적음)
    # 최악,평균 - O(n^2), 최선 - O(n)
    for i in range(1, len(arr)): # 0번째 인덱스는 정렬된 상태라고 가정
        key = arr[i]
        j = i -1 # j는 key의 왼쪽 인덱스
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    print("삽입정렬 완료:", arr)


# 병합 함수
def merge(left, right):
    result = []
    i = j = 0

    # 두 리스트를 정렬된 상태로 병합
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # 남은 요소들 추가
    result += left[i:]
    result += right[j:]

    return result

@algorithm.helper.time_logger
def merge_sort(arr):
    # 리스트를 반으로 나누고, 정렬해서 합치는 분할 정복 알고리즘
    # 평균,최악,최선 - O(n log n)
    # 리스트가 엄청 크고, 안정성이 필요할때 좋음.
    if len(arr) <= 1:  # 기저 조건
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])     # 왼쪽 정렬 - 재귀
    right = merge_sort(arr[mid:])    # 오른쪽 정렬 - 재귀

    return merge(left, right)    # 정렬된 두 배열 병합

@algorithm.helper.time_logger
def quick_sort(arr):
    # 최선,평균 - O(n log n), 최악 - O(n^2)
    # n 개의 데이터를 log n 깊이로 계속 나눔

    if len(arr) <= 1: # 기저 조건
        return arr
    #pivot = arr[0] # 실행 시간: 0.000374초로 느림.. 0 번째가 가장 작은수거나 큰수가 되면 left나 right가 빈배열이 되어서 선형비교 수행해서 느림
    pivot = random.choice(arr) # pivot을 랜덤으로 선택 - 실행 시간: 0.000166초
    print("pivot:", pivot)

    left = [x for x in arr if x < pivot] # pivot보다 작은 값들
    mid = [x for x in arr if x == pivot]  # pivot과 같은 값들
    right = [x for x in arr if x > pivot] # pivot보다 큰 값들

    return quick_sort(left) + mid + quick_sort(right)


if __name__=="__main__":
    random_array = random.sample(range(100), 30)
    print("정렬할 배열:", random_array)
    print("---------------------------------------")
    bubble_sort(random_array) # 실행 시간: 0.000048초 - 왜 느릴까? : 비교할때마다 조건을 만족하면 swap을 하기 때문
    selection_sort(random_array) # 실행 시간: 0.000022초
    insertion_sort(random_array) # 실행 시간: 0.000009초 - 왜 빠를까? : 버블, 선택정렬은 항상 전체 범위를 비교하지만 삽입 정렬은 앞쪽이 정렬되어있으면 바로 넘어감 (early stop)
    print("병합정렬 완료 ", merge_sort(random_array)) # 실행 시간: 0.000167초 - 왜 느릴까? : 데이터 양이 작을땐 단순한 정렬이 더 빨라서그렇다. 재귀 + 리스트복사가 많다.
    print("퀵정렬 완료 ", quick_sort(random_array)) # 실행 시간: 0.000158초