"""
날짜 : 2023/01/11
이름 : 구홍모
내용 : 파이썬 클래스 실습하기
"""

from sub1.Car import Car # Car 파일 안의 Car 클래스 참조
from sub1.Account import Account # Account 파일 안의 Account 클래스 참조

# 객체 실습
bmw = Car('BMW', '검정색', 5000)
bmw.speedUp()
bmw.speedDown()
bmw.show()

sonata = Car('소나타','흰색',3000)
sonata.speedUp()
sonata.speedDown()
sonata.show()

kb = Account('KB은행','223-33-2323','김유신', 20000)
kb.deposit(1000)
kb.withdraw(500)
kb.show()

wr = Account('우리은행','111-11-111','김춘추',3000)
wr.deposit(100)
wr.withdraw(10)
wr.show()

# 캡슐화
#kb.__balance += 1
kb.show()



