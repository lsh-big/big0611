# 문자열 포맷팅
# print('현재 사용량: {}'.format(time))

# 기본 포맷 스트링
food = '치킨'
text = '나는 {}을 먹고 싶다'
print(text.format(food))

print('나는 {}을 먹고 싶다'.format('치킨'))

# 다중 값 치환
food1 = '피자'
food2 = '치킨'
text = '나는 {}, {}을 먹고 싶다'
print(text.format(food1, food2))

# 인덱스를 이용한 위치 지정
print('나는 {0}, {1}을 먹고 싶다. 우리집엔 {1}이 배달되지 않아 슬프다.'.format('피자', '치킨'))

# 키워드를 활용한 명명
text = '{name}님, 반갑습니다. 적립금은 {money}원 입니다.'
print(text.format(name='홍길동', money=500))

# 숫자 포맷팅
# 문자열에 %s를 작성하여, 치환할 문자를 지정
food = '치킨'
print('나는 %s을 먹고 싶다.' % food)

print('{:.2f}% 확신합니다.'.format(95.1234567))

print('한 달 휴대폰 요금은 {:,}원 입니다.'.format(100000))