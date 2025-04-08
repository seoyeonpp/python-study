# num = 1
# while num <= 10:
#     print(num)
#     num += 1
    
# 입력받은 숫자만큼 반복하기
user_number = input("반복할 숫자를 입력하세요: ")
print("입력하신 숫자 %d를 %d 번 반복합니다." % (int(user_number), int(user_number)))
print("=" * 50)
num = 1
while num <= int(user_number):
    print(user_number)
    num += 1
    
#제곱표
square_number = input("1부터 몇까지의 제곱표를 만들까요? :")
print("1부터 %d까지의 제곱표를 만들겠습니다." % int(square_number))
square_num = 1
while square_num <= int(square_number):
    print(square_num, " ", square_num ** 2)
    square_num += 1
    
# 고무 공을 100 미터 높이에서 떨어뜨리는데, 이 공은 땅에 닿을 때마다 원래 높이의 3/5 만큼 튀어오른다. 10번 튈 때까지의 모든 높이를 계산해보기
origin_height = 100
bounce_number = 1
while bounce_number <= 10:
    origin_height = origin_height * 3 / 5
    print("%d 번째 튈때의 높이는 %.4f 입니다." % (bounce_number, round(origin_height,4))) #"%f"는 기본적으로 소수점 6자리를 출력하므로, 원하는 자리수로 제한하려면 "%0.4f"와 같이 사용
    bounce_number += 1
print("10번 튈 때까지의 높이를 계산했습니다.")