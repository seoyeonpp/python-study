from datetime import datetime

# 튜플
a = 10
b = 20
print(a, b)
a, b = b, a
print(a, b)

# 나머지 마구마구 프린트
def magu_magu(x, y, *rest):
    print(x,y,rest)
magu_magu(1,2,3,4,5) # 1 2 (3, 4, 5) 출력. 함수를 정의할 때 인자에 별표를 붙여두면 그 이후에 들어오는 것은 모두 튜플에 집어넣는 것

# 튜플을 만들 때는 위와 같이 괄호를 써도 되고 안 써도 됩니다. 다만, 원소가 없는 튜플을 만들 때는 괄호를 꼭 써야 합니다.
t = 1,2,3,4,5
print(t)
empty = ()
print(empty)
# 원소를 하나만 가진 튜플을 만들 땐 원소 뒤에 콤마(,)를 꼭 찍어야 한다.
one = 1,
print(one)

#  튜플은 리스트와 달리 원소값을 직접 바꿀 수 없다.
# t[0] = 100 # TypeError: 'tuple' object does not support item assignment

# 튜플을 리스트로, 리스트를 튜플로 쉽게 바꿀 수 있다.
l = list(t)
print(l)
tt = tuple(l)
print(tt)

# 두 수를 입력받아서 덧셈, 뺄셈, 곱셈, 나눗셈 결과를 반환하는 프로그램을 작성하세요. (단, 입력은 정수로 가정하며, 0으로 나누는 경우 등에 관한 오류를 고려할 필요는 없습니다.)
def calculator(a,b):
    a = int(a)
    b = int(b)
    return a+b, a-b, a*b, a/b
input_num = input("두 수를 띄어쓰기로 입력하세요: ")
answer = calculator(input_num.split()[0], input_num.split()[1])
print(" ".join(list(map((lambda x: str(x)), answer))))


# 사용자로부터 날짜를 나타내는 세 개의 숫자를 입력받습니다. 첫 번째 숫자는 연도를 나타내는 네 자리 숫자이고, 두 번째 숫자는 월을, 세 번째 숫자는 일을 나타냅니다.
# 입력받은 날짜를 mm/dd/yyyy 형식으로 출력합니다. 월을 두 자리 숫자(01, 02, 03, ..., 12)로, 일을 두 자리 숫자(01, 02, 03, ..., 31)로, 연도를 네 자리 숫자로 나타냅니다.
# 입력받은 날짜의 다음 날에 해당하는 날짜도 같은 형식으로 출력합니다. 단, 윤년은 무시합니다(2월은 항상 28일까지 있다고 가정합니다).
month_end_day = [31,28,31,30,31,30,31,31,30,31,30,31]
def next_day(year,month,day):
    if day < month_end_day[month-1]:
        day += 1
    else:
        day = 1
        if month < 12:
            month += 1
        else:
            month = 1
            year += 1
    return f"{month:02d}/{day:02d}/{year:04d}"
today_year = datetime.today().year
today_month = datetime.today().month
today = datetime.today().day
next_day(today_year, today_month, today)
print(f"오늘은 {today_month:02d}/{today:02d}/{today_year:04d} 이고, 내일은 {next_day(today_year, today_month, today)} 입니다.")