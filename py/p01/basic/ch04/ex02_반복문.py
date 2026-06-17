# ctrl+alt+좌우 방향키 
# 제어문
# 1. 조건문: if~elif~else
# 2. 반복문: for, while

# for
'''
for 변수 in 반복자: 
    수행문
    수행문
    수행문
    ...

반복자(iterable):  컬렉션, range()
'''

scores = [80, 90, 70, 65, 85, 95, 90, 80, 75, 80]
new_scores = []

for a in scores:
    new = a + 5
    new_scores.append(new)

print(new_scores)    

# 리스트 컴프리헨션
''' 
수행문1 if 조건문 else 수행문2 for 변수 in 리스트
'''

scores = [80, 90, 70, 65, 95, 100, 90, 80, 75, 80]
new_score = []

for s in scores:
    if s < 100:
        new = s + 5
    else:
        new = s
    new_score.append(new)    

print(new_score)

new_score2 = [s + 5 if s < 100 else s for s in scores ]
print(new_score2)

# while
'''
while 조건식:
    수행문
'''
# len(scores): 아이템 수 -> 10

scores = [80, 90, 70, 65, 95, 100, 90, 80, 75, 80]
new_scores = []
index = 0

while index < len(scores):
    if scores[index] < 100:
        new = scores[index] + 5
    else:
        new = scores[index]
    new_score.append(new)
    index = index + 1
print(len(scores))    
print(new_scores)

# ctrl+d: 블록 설정한 단어 다중 선택
# 흐름 제어

time = 0  # 누적 사용 시간
while True:
    # print('현재 사용량:' + time)
    print('현재 사용량: {}'.format(time))
    if time >= 300 :
        print('[사용 중단]하루 사용 권장량에 도달 또는 초과 하였습니다.')
        break
    else:
        time = time + 50

time = 0
while True:
    print('현재 사용량: {}'.format(time))
    if time < 150:
        # pass
        print('안전') 
    if time >= 300:
        print('[사용 중단] 하루 사용 권장량에 도달 또는 초과하였습니다.')
        break 
    else:
        time = time + 50

# 반복문 연습문제 1
shopping_dict = {'주문번호': 123,
                 '주문자': '김**',
                 '주소': '서울 마포구 상암동',
                 '주문항옥': ['맛좋은 김치', '맛좋은 라면', '시원한 물']}

for item in shopping_dict:
    print(item)

for item in shopping_dict.items():
    print(item)    

for key, value in shopping_dict.items():
    print(key)
    print(value)
    print('-----')

# 반복문 연습문제 2
menu = {"고구마": 200, "떡볶이": 600, "라면": 800}

for key, value in menu.items():
    if value > 500:
        print("{}:X".format(key))
    else:
        print("{}:O".format(key))

# 반복문 연습문제 3
lyric = """산토끼 토끼야. 어디를 가느냐. 깡충깡충 뛰면서. 어디를 가느냐.
 산고개 고개를. 나혼자 넘어서. 토실토실 알밤을. 주워 올 테야."""

count = 0
for l in lyric:
    if l == '토':
        count = count + 1
print(count)

# 구구단: 3단
# range() 함수
