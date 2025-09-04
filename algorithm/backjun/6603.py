# 백준: https://www.acmicpc.net/problem/6603
S= [1,2,3,5,8,13,21,34]
choose = []
def comb(index,level):
    if level == 6:
        print(choose)
        return

    for i in range(index,len(S)):
        choose.append(S[i])
        comb(i+1,level+1)
        choose.pop()

comb(0,0)