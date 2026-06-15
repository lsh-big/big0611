# 자료형
# 1. 숫자형
# 정수형: int
x, y = 10, 3.14
# 실수형: float
z = -25

# 2. 불리언: True, False -> 예약어
# 3. 문자형

#숫자형
# print() 함수: 괄호 안의 값을 출력하는 함수
# type() 함수: 자료형을 알려주는 함수
print(type(x), type(y), type(z))

# 지수 표현식: e 또는 E를 사용하여 10의 거듭제곱을 나타냄
# e3은 10의 3승을 의미하며, 17e3은 17 곱하기 10^3을 의미함

a = 17e3
b = 17E3
c = -35.2e2
d = 275e-2
print(a, b, c, d)

# 불(bool): 참과 거짓을 나타내는 자료형
# True는 참, False는 거짓을 나타냄
# 대입 연산자: = 
# 비교 연산자: >, <, == 등

a = 100 > 50
b = 100 < 50
c = 100 == 50
print(a, b, c)
# type(): 데이터의 유형을 확인 내장 함수
type(a)

# 문자형(str): "", ''
a = "Hello"
b = '123'
c = 'How are you?'

# 다중 커서: ctrl + alt + 위아래방향키
print(type(a))
print(type(b))
print(type(c))  

# 다중 행 문자열: """ """ 또는 ''' '''
x = """abc abc abc abc abc abc
abc abc abc abc abc abc"""
print(x)

a1 = 'He said "I love you."'
a2 = "He said \"I love you.\""
print(a2)
print(a1)

# 타입변환
# int(): 정수형으로 변환하는 함수
# float(): 실수형으로 변환하는 함수 
# str(): 문자열로 변환하는 함수
# bool(): 불리언으로 변환하는 함수
temperature = '20'
humidity = '50'
# 문자끼리는 문자열 연결
# 숫자끼리는 덧셈
print(temperature + humidity)

print(int(temperature) + int(humidity))

a = 0  # 0 이외의 숫자는 모두 True로 간주됨
b = 500 
c = '' # 빈 문자열은 False로 간주됨
d = 'Hello' # 빈 문자열이 아닌 문자열은 모두 True로 간주됨
e = None # None은 False로 간주됨
print(bool(a), bool(b), bool(c), bool(d), bool(e))
# False, True, False, True, False
# 0, 빈 문자열은 False, 나머지는 True 
# bool() 함수는 주어진 값을 불리언으로 변환하는 함수
 
