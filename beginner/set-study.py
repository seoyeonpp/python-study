import random
# 세트
# 집합을 표현함

fruits = {'apple', 'banana', 'orange', 'grape', 'banana','tomato'}
print(fruits) # 중복된 원소는 제거됨

fruits.add('mango')

vegetables = {'tomato', 'carrot', 'cabbage'}

print(fruits | vegetables) # 합집합
print(fruits & vegetables) # 교집합
print(fruits - vegetables) # 차집합

list_set = [fruits, vegetables]
print(set.union(*list_set)) # 합집합
print(set.intersection(*list_set)) # 교집합
print(set.difference(*list_set)) # 차집합


# 끝말 잇기
# 컴퓨터와 플레이어는 자기 턴(turn, 차례)이 되면 이전에 상대방이 말한 단어의 끝 글자로 시작하는 단어를 말해야 하며, 이전에 썼던 단어는 말할 수 없습니다. 두음 법칙은 무시합니다.
computer_word = {'게맛살', '구멍', '글라이더', '기차', '대롱', '더치페이', '롱다리', '리본', '멍게', '박쥐', '본네트', '빨대', '살구', '양심', '이빨', '이자', '자율', '주기', '쥐구멍', '차박', '트라이앵글'}

print("끝말잇기하자. 내가 먼저 할게.")
computer_said = random.choice(list(computer_word))
print(computer_said)

old_word = []
old_word.append(computer_said)

while True:
  player_said = input()
  if len(player_said) <= 1:
    print("한글자 이상이어야해")
    continue
  if(player_said[0] != computer_said[-1]):
    print("틀렸어. 내가 이겼어.")
    break
  if player_said in old_word:
    print("이미 나온 단어야.")
    break
  # 컴퓨터가 말할 단어 찾기
  elif player_said[-1] in [word[0] for word in computer_word]:
    old_word.append(player_said)
    for word in computer_word:
      if word[0] == player_said[-1]:
        if word in old_word:
          continue
        else:
          computer_said = word
          print(computer_said)
          old_word.append(computer_said)
          break
    else:
      print("내가 졌어.")
      break
  else:
    print("내가 졌어.")
    break
