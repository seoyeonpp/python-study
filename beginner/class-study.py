class Singer:
    def sing(self):
        print("LaLaLa~~~")
        
newjeans = Singer()
newjeans.sing()


class Amazon:
    strength = 20
    dexterity = 25
    vitality = 20
    energy = 15

    def attack(self):
        return 'Jab!!!'

jane = Amazon()
print(jane.attack())

class Person:
    eyes = 2
    nose = 1
    mouth = 1
    ears = 2
    arms = 2
    legs = 2

    def eat(self):
        print('얌냠...')

    def sleep(self):
        print('쿨쿨...')

    def talk(self):
        print('주절주절...')
        
        
class Student(Person):     # Person 클래스를 상속받음
    def study(self):
        print('열공열공...')

student = Student()
student.eat()


class Book:
    def setData(self, title, price, author):
        self.title = title
        self.price = price
        self.author = author
    def printData(self):
        print('제목 : ', self.title)
        print('가격 : ', self.price)
        print('저자 : ', self.author)
    # 초기화 메서드
    def __init__(self):
        print('책 객체를 새로 만들었어요~')
    # 소멸자
    def __del__(self):
        print('책 객체를 삭제했어요!')
    # 문자열을 리턴함.
    def __repr__(self):
        return f'제목 : {self.title}, 가격 : {self.price}, 저자 : {self.author}'
        
new_book = Book()
new_book.setData('파이썬 정복', 20000, '짱구')
new_book.printData()
print(new_book)