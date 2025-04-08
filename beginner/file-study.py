f = open('test.txt')
print(f.read())


write_f = open('test.txt', 'w') # 원래있던 데이터가 날아감..
write_f.write('Hello, Python!')
write_f.close()

a_f = open('test.txt', 'a+')
a_f.write('\nHello, Python!2222 \nHello, Python!3333')
a_f.close()

# pickle
users = {'kim':'3kid9', 'sun80':'393948', 'ljm':'py90390'}
f1 = open('users.txt', 'wb')
import pickle
pickle.dump(users, f1)
f1.close()

f2 = open('users.txt', 'rb')
a = pickle.load(f2)
print(a)

# glob
# 파일들의 리스트를 뽑을 때 사용
from glob import glob
print(glob('*.txt'))