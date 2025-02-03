from functools import reduce
# 람다 (lambda)
# lambda 매개변수 : 표현식

# map(함수, 리스트)
print(list(map(lambda x: x**2, range(5))))

# reduce(함수, 시퀀스)
# 시퀀스(문자열, 리스트, 튜플)의 원소들을 누적적으로 함수에 적용
print(reduce(lambda x,y: x+y, range(5)))
print (reduce(lambda x,y: y+x, 'abcde'))

# filter(함수, 리스트)
print(list(filter(lambda x: x>5, range(10))))
print(list(filter(lambda x: x % 2, range(10)))) # 홀수만 출력됨. 1은 True, 0은 False