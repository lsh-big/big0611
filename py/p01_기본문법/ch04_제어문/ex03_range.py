# range(start, stop, step)
# start: 0(default)
# step: 1

# range(stop): 매개변수가 1개일 때
# 0부터 시작해서 5 직전(4)까지 생성
for i in range(5):
    print(i, end=" ")
# 출력 결과: 0 1 2 3 4

# range(start, stop): 매개변수가 2개일 때
# 2부터 시작해서 7 직전(6)까지 생성
for i in range(2, 7):
    print(i)
# 출력 결과: 2 3 4 5 6

# range(start, stop, step): 매개변수가 3개일 때
# 1부터 시작해서 10 직전까지 2씩 건너뛰며 생성 (홀수만)
for i in range(1, 10, 2):
    print(i, end=" ")
# 출력 결과: 1 3 5 7 9

# 역순(거꾸로) 숫자 생성하기
# 5부터 시작해서 1 직전(2)까지 1씩 감소하며 생성
for i in range(5, 1, -1):
    print(i, end=" ")
# 출력 결과: 5 4 3 2



# range 사용할 때 가장 많이 하는 실수
print(range(5))
# 출력 결과: range(0, 5)

print(list(range(5)))
# 출력 결과: [0, 1, 2, 3, 4]

# 구구단 3단
# range([시작값], 끝값, [증감값]) 함수
range(9)

for num in range(9):
    print(num)

for num in range(9):
    print("3 * {} = {}".format(num + 1, (num + 1) * 3)) 

# 공부 스케줄
bookmark = 0
for day in range(20):
    print("[{}일차 공부계획]".format(day + 1))
    for page in range(5):
        print(" {}쪽 공부".format(bookmark + page + 1))
    bookmark = bookmark + page + 1       

# 상품 재고 관리 시스템
