# 백준 https://www.acmicpc.net/problem/1759

result = []
select = []
def comb(index, level):
    if level == L:
        vowel_count = sum(1 for el in select if el in vowels)
        consonant_count = L - vowel_count
        # 모음 1개 자음2개
        if vowel_count >= 1 and consonant_count >=2:
            result.append("".join(sorted(select)))
        return

    for i in range(index,C):
        select.append(arr[i])
        comb(i+1,level+1)
        select.pop()

L,C = map(int, input().split())
arr = sorted(input().split()) # 미리 정렬을 하기
vowels = ['a','e','i','o','u']

comb(0,0)

for password in result:
    print(password)
# for item in sorted(result):
#     if not item in unique_result and any(char in vowels for char in item):
#         unique_result.append(item)
#
# for element in unique_result:
#     print(element)
