# 전역변수 지역변수
snack = '새우깡'

def eat():
    snack = '홈런볼'
    print(f"eat : {snack}")

print(f"global : {snack}")
eat()

def eat2():
    global snack # 근데 전역변수가 이미 같은 이름으로 되어있는데 여기서 다시 재정의 하는게 왜 되는거지?
    snack='홈런볼'
    print(f"eat2 : {snack}")
    
eat2()

# global 키워드는 실제로 두 가지 역할을 합니다:
# 이미 존재하는 전역 변수를 참조할 때
# 새로운 전역 변수를 선언할 때