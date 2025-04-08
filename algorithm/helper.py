import time
from functools import wraps

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

