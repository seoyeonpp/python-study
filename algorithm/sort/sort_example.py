import time
from functools import wraps
import random

# 함수 시간 측정 decorator
def time_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()  # 더 정밀한 시간 측정
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"[{func.__name__}] 실행 시간: {end_time - start_time:.6f}초")
        return result
    return wrapper


@time_logger
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print("버블정렬 완료:", arr)


if __name__=="__main__":
    bubble_sort(random.sample(range(100), 50))