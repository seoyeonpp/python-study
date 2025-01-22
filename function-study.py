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