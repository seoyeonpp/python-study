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
