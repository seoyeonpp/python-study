# import 모듈 : 모듈 전체를 가져옴
# from 모듈 import 변수, 함수, 클래스 : 모듈 내부의 변수, 함수, 클래스를 가져옴
# del 모듈 : 모듈을 메모리에서 삭제
#  from importlib import reload reload(모듈) : 모듈을 다시 불러옴

import math
print(math.sqrt(2))
print(math.pi)

import calendar
print(calendar.prmonth(2025,2))

# import webbrowser
# url="http://www.naver.com"
# webbrowser.open(url) # 웹브라우저로 열기


# 시저(카이사르) 암호 만들기
import string
outer_circle = string.ascii_lowercase
inner_circle = string.ascii_uppercase[3:] + string.ascii_uppercase[:3]
encoding = str.maketrans(outer_circle, inner_circle)

print(f"traue nie dem brutus => {"traue nie dem brutus".translate(encoding)}")

# 날짜와 시간 다루기
from datetime import datetime
specific_datetime = datetime(2025, 2, 3, 16, 16, 0)
print(specific_datetime)

datetime1 = datetime.now()
datetime2 = datetime(2025, 2, 14)
diff = datetime2 - datetime1
print(diff)

currnet_datetime = datetime.now()
format_datetime = currnet_datetime.strftime("%B %d, %Y")
print(format_datetime)

