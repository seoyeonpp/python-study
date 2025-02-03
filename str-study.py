# 문자열
x = "banana"
print(x[0])
print(x[1:4])
print(x[4:])
# x[0] = "n" # 문자열은 수정이 불가능하다. TypeError: 'str' object does not support item assignment

# find
s = "hello world"
print(x.find("na"))
print(s.find("na")) # 없으면 -1 반환
print(s[0:5].rstrip()) # 오른쪽 공백 제거

# 리스트
prime = [3,7,11]
prime.append(5) # 리스트 뒤에 원소 추가
print(prime)
prime.sort() # 리스트 정렬
print(prime)

prime.insert(0,2) # 리스트 특정 위치에 원소 추가
print(prime)

del prime[4] # 리스트 특정 위치의 원소 삭제
print(prime)

del_num = prime.pop() # 리스트 마지막 원소 삭제 후 리턴
print(prime)
print(del_num)

prime[0] = 1 # 리스트 특정 위치의 원소 수정
print(prime)

orders = ['potato', ['pizza', 'Coke', 'salad'], 'hamburger']
print(orders[1])
print(orders[1][0])

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1][1])

character = []
sentence = "Be happy!"
for char in sentence:
    character.append(char)

new_character = [n for n in character if n != " "] # 리스트 컴프리헨션으로 스페이스바 제거
print(new_character)

# 리스트 원소들의 합 구하기
one_to_ten = range(1,11)
print(sum(one_to_ten))

# 성적표
chulsu = [90, 85, 70]
younghee = [88, 79, 92]
minsu = [90, 60, 70]
me = [100, 100, 100]

students = [chulsu, younghee, minsu, me]
for score in students:
    total = sum(score)
    average = total / 3
    print(f"합계 : {total}, 평균 : {round(average)}")
    
    
# 뉴진스를 좋아하는 사람: 철수, 영희, 민수, 지현, 서연
# 아이브를 좋아하는 사람: 영희, 민수, 지수, 서연, 하나
# 에스파를 좋아하는 사람: 철수, 지현, 지수, 서연, 나영
# 이 중에서 뉴진스와 아이브를 모두 좋아하지만 에스파는 좋아하지 않는 사람은 누구일까요?
newjeans = ["철수", "영희", "민수", "지현", "서연"]
ive = ["영희", "민수", "지수", "서연", "하나"]
aespa = ["철수", "지현", "지수", "서연", "나영"]

both_like = set(newjeans) & set(ive)
print(both_like)  # 뉴진스와 아이브를 모두 좋아하는 사람

not_like_aespa = both_like - set(aespa)
print(not_like_aespa)  # 뉴진스와 아이브를 모두 좋아하지만 에스파는 좋아하지 않는 사람

print(",".join(both_like - set(aespa)))

# 거꾸로 배열해도 같은 단어 혹은 문장이 되는 것을 회문(palindrome)이라고 합니다.
# 주어진 단어가 회문인지 판별하는 함수 palindrome()을 작성하세요.

def palindrome(word):
    format_word = word.lower().replace(" ", "")
    return format_word == format_word[::-1]

print(palindrome(input("단어를 입력하세요: ")))

# 정수 num을 매개변수로 받아 각 자리 숫자(digit)의 합을 계산하는 sumOfDigits() 함수를 작성하세요. 단, 나눗셈을 이용하지 말고 리스트를 사용해서 풀어보세요.
def sumOfDigits(num):
    num_list = []
    for i in str(num):
        num_list.append(int(i))
    
    return print(sum(num_list))
  
sumOfDigits(input("각 자릿수의 합을 구할 정수를 입력하세요: "))

# 소수(素數, prime number)는 1 과 그 자체만을 인수(factor)로 갖는 수입니다1. 또는 “1보다 큰 자연수 중 1과 자기 자신만을 약수로 가지는 수”라고 정의할 수 있습니다. 입력받은 수까지의 소수를 모두 찾아서 출력하는 함수 primeNumber()를 작성하세요.
def primeNumber(num):
    L = list(range(2, num+1))
    for i in L:
        for j in L:
            if j % i == 0 and j != i:
                L.remove(j)
    return print(L)
  
primeNumber(int(input("소수를 찾을 범위를 입력하세요: ")))