"""
날짜 : 2023/01/11
이름 : 구홍모
내용 : 파이썬 모듈 실습하기
"""
import sub2.calc
import sub2.calc as c # class 는 from , module 은 import 부터
from sub2.calc import *

r1 = sub2.calc.plus(1,2)
print('r1 : ',r1)

r2 = c.minus(3,1)
print('r2 : ',r2)

r3 = multi(3,4)
print('r3 : ',r3)

r4 = div(4,2)
print('r4 : ',r4)
