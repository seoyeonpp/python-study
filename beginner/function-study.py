# 함수 실습
def print_hello():
    print("Hello")
    
print_hello()

def comparison(a, b):
    if a > b:
        print(f"{a}이 {b}보다 큽니다.")
    elif a < b:
        print(f"{a}이 {b}보다 작습니다.")
    else:
        print(f"{a}와 {b}는 같습니다.")
        

isValid = False
while (isValid == False):
    compare_num = input("비교할 두 수를 띄어쓰기로 입력하세요: ").split()
    if(len(compare_num) != 2):
        print("두 수를 입력해주세요.")
        isValid = False
    else:
        comparison(int(compare_num[0]), int(compare_num[1]))
        isValid = True
        
        
# 양(陽)의 정수를 입력받아, 그 수가 몇 자리 숫자인지 출력하는 함수 numOfDigits()를 만들어 보세요.
def numOfDigits(num):
    if num < 0:
        return print("양의 정수를 입력해주세요.")
    return print(f"{len(str(num))} 자리수 입니다.")

num_input = int(input("양의 정수를 입력하시면 자리수를 알려드립니다. : "))
numOfDigits(num_input)


# 구구단을 2단부터 9단까지 계산해서 출력하는 프로그램
def ninenine():
    for i in range(2,10):
        print(f"====={i}단=====")
        for j in range(1,10):
            print(f"{i} * {j} = {i*j}")

ninenine()


# 태어난 해를 네 자리 숫자로 입력하면 한국 나이를 반환하는 함수 korean_age()를 작성하세요.
from datetime import datetime
this_year = datetime.today().year
this_month = datetime.today().month

def korean_age():
    year_input = input("태어난 해를 네 자리 숫자로 입력하세요: ")
    month_input = input("태어난 달을 두 자리 숫자로 입력하세요: ")
    if int(month_input) > this_month:
        return print(f"한국 나이는 {this_year - int(year_input) + 1}세 이고, 만 나이는 {this_year - int(year_input) - 1}세 입니다.")
    else:
        return print(f"한국 나이는 {this_year - int(year_input) + 1}세 이고, 만 나이는 {this_year - int(year_input)}세 입니다.")
korean_age()

# 원금(p), 단리 이율(r), 기간(t)이 주어졌을 때 이자를 구하는 함수 simple_interest()를 작성하세요.
def simple_interest(p, r, t):
    return print(f"이자는 {p*r*t} 입니다.")
simple_interest(10000000, 0.03875, 5)

# 원금(p), 단리 이율(r), 기간(t)이 주어졌을 때 원리금을 계산하는 함수 simple_interest_amount()를 작성하세요.
def simple_interest_amount(p, r, t):
    return print(f"원리금은 {p * (1+r*t)} 입니다.")
simple_interest_amount(10000000, 0.03875, 5)

# 놀이 기구의 이름과 키 제한을 나타낸 문자열을 입력받아서, 놀이 기구의 이름, 탑승 가능한 키의 하한(下限)과 상한(上限)을 각 행에 출력합니다.
def ride_reader(text):
    text_array = text.split(":")
    ridename = text_array[0].strip() #공백 제거
    cm_text = text_array[1]
    
    cmmin = cmmax = None  # 초깃값 설정
    
    print(cm_text)
    if "~" in cm_text:
        cmmin, cmmax = cm_text.split("~")
        cmmin = int(cmmin.strip().replace("cm", ""))
        cmmax = int(cmmax.strip().replace("cm", ""))
    else:
          if "이상" in cm_text:
              cmmin = int(cm_text.split("cm")[0].strip())
          elif "이하" in cm_text:
              cmmax = int(cm_text.split("cm")[0].strip())
              
    return ridename, cmmin, cmmax
    
if __name__ == "__main__":
    ridename, cmmin, cmmax = ride_reader(input())
    print("이름:", ridename)
    print("하한:", cmmin)
    print("상한:", cmmax)