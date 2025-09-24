# 백준 : https://www.acmicpc.net/problem/23246

def solve():
    return

def format_handler(arr):
    format_arr = []
    for item in arr:
        back_number,x,y,z = map(int,item.split())
        # 곲한값, 더한값, 등번호 순서로
        temp_arr = [x*y*z, x+y+z, back_number]
        format_arr.append(tuple(temp_arr))
    return format_arr

n = int(input())
# player = [tuple(map(int,input().split())) for _ in range(n)]
init_arr = [input() for _ in range(n)]
player = format_handler(init_arr)

print(sorted(player))