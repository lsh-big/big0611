
# 변수
# 5를 a에 할당(대입)
# = 대입 연산자
a = 5
# alt+위아래방향키: 줄 이동
# == (같다)
a == 5
print(a)

b = 3
print(b)

print(a + b)

# 문자열 데이터:'', ""
c = '가나다'
print(c)

radio_freq = 107.9
print(radio_freq)

# 잘못된 변수명: 숫자로 시작
# 2var = '행복'
# print(2var)

# 2. 공백이 들어있으면 안됨
# happy var = '공백'

# 3. _, $를 제외한 특수문자 사용 불가
# happyvar! = '행복'

# 잘못된 변수명 : 예약어는 사용X
# def = '행복'

# 영문의 대소문자 구별한다.
abc = 5
ABC = 'Apple'
print(abc, ABC)

#------------------------------

# 다중 변수 동시 선언
x, y, z = '사과', '바나나', '당근'
print(x, y, z)

# 변수명에 _ (언더스코어)사용하기
# -> 이는 주로 사용하지 않을 변수를 위한 자리 쵸시자로 사용!
_, var = 'Not use', 'Use'
print(_, var)

# 단일 값의 다중 변수 할당
x = y = z = 'Dog'
print(x, y, z)