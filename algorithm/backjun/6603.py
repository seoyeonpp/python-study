# 백준: https://www.acmicpc.net/problem/6603

choose = []
def comb(index,level):
    if level == 6:
        print(" ".join(choose))
        return

    for i in range(index,len(S)):
        choose.append(S[i])
        comb(i+1,level+1)
        choose.pop()

while True:
    try:
        isEnd = False
        temp = input().split(" ")
        k = temp[0]
        S = temp[1:]
        if k == "0" or k == 0:
            break
        comb(0,0)
        isEnd = True

        if isEnd:
            print()
    except:
        break