# for문 실습
number_input = input("반복할 숫자를 입력하세요 : ")
for i in range(0, int(number_input)):
    print(number_input)
    
    
# 제곱표(for)
square_number = input("1부터 몇까지의 제곱표를 만들까요? :")
for i in range(1, int(square_number) + 1):
    print(i, " ", i ** 2)
    
    
# 대학교의 화학자들은 상처를 매우 빠르게 치료하는 약물을 제조하는 새로운 과정을 개발했다.
# 제조 과정은 매우 길고 화학 약품을 매번 모니터링해야 하므로 몇 시간씩 걸린다!
# 학생들은 졸거나 딴짓을 하므로 이 일을 믿고 맏길 수가 없다.
# 그러므로 약물의 제조를 모니터링하는 자동 장치를 프로그래밍해야 한다. 장치는 15초마다 온도를 측정해 프로그램에 제공한다.
# 프로그램은 먼저 최소와 최대의 안전 온도를 나타내는 두 개의 정수를 읽는다.
# 그 다음에, 장치가 제공하는 온도(정수)를 계속 읽는다.
# 화학 반응이 완료되면 장치는 끝을 알리는 -999를 보낸다.
# 기록된 온도가 올바른 범위에 있을 경우(최솟값 또는 최댓값과 같아도 된다) Nothing to report를 표시해야 한다.
# 하지만 온도가 위험 수준에 도달하면 Alert!를 표시하고 온도 측정을 중단한다(장치가 온도값을 계속 보내더라도).

min_temp = int(input("최저 온도를 입력하세요: "))
max_temp = int(input("최고 온도를 입력하세요: "))

while True:
    temp = int(input("온도를 입력하세요: "))
    if temp == -999:
        print("측정을 종료합니다.")
        break
    if temp < min_temp or temp > max_temp:
        print("Alert!")
        break
    else:
        print("Nothing to report")
        
# for 문으로 하려면 고정값이 필요한데, (예를 들면 10번 입력한다. 등) 이 문제는 입력값에 따라 반복횟수가 달라지므로 iter() 함수로 무한 반복을 쓸 수 있다. 근데 while문이 더 가독성이 좋을듯..
# iter(int,1) 은 무한 반복을 생성하는 트릭

for i in iter(int, 1):
    temp = int(input("온도를 입력하세요: "))
    if temp == -999:
        print("측정을 종료합니다.")
        break
    if temp < min_temp or temp > max_temp:
        print("Alert!")
        break
    else:
        print("Nothing to report")