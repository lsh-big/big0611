# 시스템 출력
# sep= " "  ->기본값이 공백
print("사과", "복숭아", "망고")
print("사과", "복숭아", "망고", sep =",")
# 구분자: ,
print("사과", "복숭아", "망고", sep ="|") 
# sep,end는 맨끝에만 입력

# 줄바꿈
# 기본값: end= '\n'
print('이것은 문장 입니다.', end="\n")
print('문장 입니다.')

# 줄바꿈 X
print('이것은 문장 입니다.', end="")
print('문장 입니다.')

# 문자열 연결: +
# 나이: 20살
age = '20'  # -> 숫자만쓰면 에러남
print('나이: ' + age + '살')
print('문자열은 + 연산자로 연결한다.')

# 줄바꿈: \n
print("산토끼 토끼야\n어디를 가느냐\n깡총깡총 뛰어서\n어디를 가느냐")

# 포맷스트링
# 문자열.format()
'''
print(문자열.format(값))
print('메세지: {값}'.format(값))
'''
food = "치킨"
text = "나는 {}을 먹고 싶다"
print(text.format(food))
print("나는 {}을 먹고 싶다".format("치킨"))

food1 = '피자'
food2 = '치킨'
text = '나는 {}, {}을 먹고 싶다'
print(text.format(food1, food2))

text = '나는 {1}, {0}을 먹고 싶다'
print(text.format(food1, food2))

# text = '나는 {food1}, {foo2}을 먹고 싶다'
# print(text.format('피자', '카레'))

print('나는 {0} {1}을 먹고싶다. 우리집엔 {1}이 배달되지 않아 슬프다.'.format(food1, food2))
# IndexError: Replacement index 2 out of range for positional args tuple

# 인덱스대신 변수이름으로
text = '{name}님, 반갑습니다. 적립금은 {money}원 입니다..'
print(text.format(name = '홍길동', money = 500))

# text = '{name}님, 반갑습니다. 적립금은 {money}원 입니다..'
# print(text.format('name', 'money'))

# 문자열에 %s를 작성하여, 치환할 문자를 지정
food = "치킨"
print("나는 %s을 먹고 싶다." %food)

# 소수점 셋째자리까지 표시(자동 반올림)
print("{:.3f}% 확신합니다.".format(95.1234567))

# 천 단위마다 , 자동 입력
print('한 달 휴대폰 요금은 {:,}원 입니다.'.format(10000000000))
