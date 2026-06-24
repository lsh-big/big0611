# 튜플(tuple) 생성. 여러 데이터를 하나로 묶는 “변경 불가능한 리스트”
fruit_tuple = ('사과', '바나나', '오렌지')
print(fruit_tuple)

# shift + alt + 방향키 : 줄 복사
fruit_tuple = ('사과', '바나나', '오렌지', '사과', '바나나')
print(fruit_tuple)

# 아이템 선택
print(fruit_tuple[1])  # '바나나'

# 아이템 변경 불가
# fruit_tuple[1] = '키위'  # TypeError: 'tuple'
# 튜플은 리스트보다 메모리를 적게 사용
# 추가불가
# fruit_tuple.append('수박')  # AttributeError: 'tuple' object has no attribute 'append'
# 삭제불가
# fruit_tuple.remove('사과')  # AttributeError: 'tuple' object has no attribute 'remove'

# 아이템 추가/삭제 -> 리스트 형으로 변화 후 가능
# 타입 변환
# 기본: int(), float(), str(), bool()
# 컨테이너: list(), touple(), set(), dict()
# 튜플을 리스트로 변환
fruit_list = list(fruit_tuple)
fruit_list.append('수박')
fruit_list.remove('사과')
fruit_list[1] = '키위'
print('34:', fruit_list)
# 리스트를 튜플로 변환
fruit_tuple = tuple(fruit_list)
print(fruit_tuple)






