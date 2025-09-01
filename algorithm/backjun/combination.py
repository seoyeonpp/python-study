# 조합
# 재귀함수로 구현하기

arr = [1,2,3,4,5,6,7,8,9,10]
choose = []

# 10개의 원소중 5개를 고르는 모든 경우
N = 10
R = 5
def combination(index, level):
    # base case
    if level == R:
        print(choose)
        return

    # recursive case
    for i in range (index,N):
        choose.append(arr[i]) # 인덱스가 i인 원소를 선택(추가)
        combination(i+1, level+1) # 다음 for문으로 들어감
        choose.pop() # 넣었던 인덱스가 i인 원소를 제거

combination(0,0)
