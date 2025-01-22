# 조건문 연습
# dictionary
number_to_korean = {
    1: '일',
    2: '이',
    3: '삼',
    4: '사',
    5: '오',
    6: '육',
    7: '칠',
    8: '팔',
    9: '구',
    10: '십'
}

user_input = input("숫자를 입력하세요: ")
if int(user_input) > 10:
    print("10 이하의 숫자만 입력해주세요.")
elif int(user_input) < 1:
    print("1 이상의 숫자만 입력해주세요.")
else:
    print(f"{user_input}을 한글로 쓰면 {number_to_korean[int(user_input)]}입니다.")


# input()으로 사용자로부터 입력받은 정수를 계속 더해나가다가, 음수가 입력되면 중단하고 그 전까지 계산한 값을 출력하는  파이썬 스크립트를 작성하세요.
sum_num = 0
while True:
    num_input = input("숫자를 입력하세요. : ")
    if(int(num_input) >= 0):
        sum_num += int(num_input)
    else:
        print(sum_num)
        break
      
      
# 윤년 판별하기
# 연도가 4로 나누어 떨어지는 해는 윤년이다. 그 중 100으로 나누어 떨어지는 해는 평년이다. 그 중 400으로 나누어 떨어지는 해는 윤년이다.
year = input("연도를 입력하세요: ")
if(int(year) % 4 == 0):
    if(int(year) % 100 == 0):
        print("%d 년은 평년입니다." % int(year))
        if(int(year) % 400 == 0):
            print("%d 년은 윤년입니다." % int(year))
    else:
        print("%d 년은 윤년입니다." % int(year))
else:
    print("%d 년은 평년입니다." % int(year))

# 위의 코드를 리팩토링하기
year = int(input("연도를 입력하세요: "))

if year % 400 == 0:  # 400으로 나누어 떨어지면 윤년
    print(f"{year} 년은 윤년입니다.")
elif year % 100 == 0:  # 100으로 나누어 떨어지면 평년
    print(f"{year} 년은 평년입니다.")
elif year % 4 == 0:  # 4로 나누어 떨어지면 윤년
    print(f"{year} 년은 윤년입니다.")
else:  # 나머지는 평년
    print(f"{year} 년은 평년입니다.")
    
    
# and/or 연산자
s = 'banana'
if 'd' in s or 'c' in s:
    print("banana 글자에 d 또는 c가 있습니다.")
if 'a' in s and 'b' in s:
    print("banana 글자에 a와 b가 있습니다.")