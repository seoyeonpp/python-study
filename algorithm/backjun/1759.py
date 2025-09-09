# 백준 https://www.acmicpc.net/problem/1759

result = []
unique_result = []
select = []
def comb(index, level):
    global select
    if level == C:
        result.append("".join(sorted(select)))
        return

    for i in range(index,L):
        select.append(arr[i])
        comb(i+1,level+1)
        select.pop()

C, L = map(int, input().split())
arr = input().split()

comb(0,0)
vowels = ['a','e','i','o','u']
for item in sorted(result):
    if not item in unique_result and any(char in vowels for char in item):
        unique_result.append(item)

for element in unique_result:
    print(element)
