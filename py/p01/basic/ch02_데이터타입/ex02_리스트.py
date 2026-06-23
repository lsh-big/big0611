# 리스트 생성
# 비효율적인 방법
# ctrl + d: 커서가 있는 단어를 선택하여 동시에 편집
fruit_1 = '사과'
fruit_2 = '오렌지'
fruit_3 = '바나나'

# 컨테이너 자료형
# : 리스트, 튜플, 세트, 딕셔너리

# 효율적인 방법
fruits = ['사과', '오렌지', '바나나']
print(fruits)

fruits2 = ['사과', '오렌지', '바나나', '사과', '오렌지']
print(fruits2)

#리스트 아이템 선택
# 아이템 선택
# 인덱싱
print(fruits[0])  # 결과: '사과'
print(fruits[-1])  # 결과: '바나나'  
# 슬라이싱
print(fruits[1:3])  # 결과: ['오렌지', '바나나']
fruit_list = ['사과', '오렌지', '바나나']

#수정(update)
fruit_list[1] = '딸기'
print(fruit_list)  # 결과: ['사과', '딸기', '바나나']

# 추가
# insert() 메서드: 특정 위치에 아이템 추가
# append() 메서드: 리스트의 끝에 아이템 추가
# 메서드(): 객체가 가지고 있는 함수
# 함수(): 독립적으로 존재하는 함수

fruit_list.insert(2, '망고')
print(fruit_list)  # 결과: ['사과', '딸기', '망고', '바나나']

fruit_list.append('수박')
print(fruit_list)  # 결과: ['사과', '딸기', '망고', '바나나', '수박']

# 리스트1.extend(리스트2): 리스트1에 리스트2의 아이템을 추가
vegetable_list = ['당근', '토마토', '양파']
fruit_list.extend(vegetable_list)
print(fruit_list)  # 결과: ['사과', '딸기', '망고', '바나나', '수박', '당근', '토마토', '양파']

# + 연산
list1 = [1, 2, 3]
list2 = ['가', '나', '다']
print(list1 + list2)  # 결과: [1, 2, 3, '가', '나', '다']

# 리스트 아이템 제거
# remove() 메서드: 아이템 값을 사용하여 제거
# del 키워드: 인덱스[]를 사용하여 아이템 제거
fruit_list.remove('토마토')
print(fruit_list)  # 결과: ['사과', '딸기', '망고', '바나나', '수박', '당근', '양파']

del fruit_list[-1]
print(fruit_list)  # 결과: ['사과', '딸기', '망고', '바나나', '수박', '당근']   

#del 키워드로 리스트 전체 삭제
# del fruit_list
# print(fruit_list)  # 결과: NameError: name 'fruit_list' is not defined

fruit_list = ['사과', '키위', '망고']
print(fruit_list)  # 결과: ['사과', '키위', '망고']

# 리스트. clear() 메서드: 리스트의 모든 아이템 제거
fruit_list.clear()
print(fruit_list)  # 결과: []

# 아이템 정렬
# sort() 메서드: 리스트의 아이템을 오름차순으로 정렬
fruit_list = ['딸기', '망고', '블루베리', '수박', '사과', '바나나', '오렌지' ]
fruit_list.sort()
print(fruit_list)  # 결과: ['사과', '바나나', '블루베리', '딸기', '망고', '수박', '오렌지']

# reverse=True 매개변수: 내림차순으로 정렬
fruit_list.sort(reverse=True)
print(fruit_list)  # 결과: ['오렌지', '수박', '망고', '딸기', '블루베리', '바나나', '사과']

