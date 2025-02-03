f = open('./test.txt')
print(f.read())


write_f = open('./test.txt', 'w') # 원래있던 데이터가 날아감..
write_f.write('Hello, Python!')
write_f.close()

a_f = open('./test.txt', 'a+')
a_f.write('\nHello, Python!2222 \nHello, Python!3333')
a_f.close()