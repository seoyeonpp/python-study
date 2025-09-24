# 백준 : https://www.acmicpc.net/problem/23246


def format_handler(arr):
    format_arr = []
    for item in arr:
        back_number,x,y,z = map(int,item.split())
        # 곲한값, 더한값, 등번호 순서로
        temp_arr = [x*y*z, x+y+z, back_number]
        format_arr.append(tuple(temp_arr))
    return format_arr

n = int(input())
init_arr = [input() for _ in range(n)]
player = format_handler(init_arr)

for el in sorted(player)[:3]:
    print(el[-1], end=" ")