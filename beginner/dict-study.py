# 딕셔너리
snack_dict = {}
snack_dict['새우깡'] = 1000
snack_dict['감자깡'] = 1200
snack_dict['고구마깡'] = 1500
snack_dict['양파링'] = 1700

print(snack_dict.keys())
print(snack_dict.values())
print(snack_dict.items())

del snack_dict['고구마깡']
print(snack_dict)

print('새우깡' in snack_dict)
print('고구마깡' in snack_dict)
