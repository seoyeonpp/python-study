# list를 배워보자
fruits = ['apple', 'banana', 'coconut', 'avocado']
print(len(fruits))
print(fruits[2])

# 리스트 컴프리헨션
new_fruits = [fruit for fruit in fruits if fruit != 'banana']
print(new_fruits)