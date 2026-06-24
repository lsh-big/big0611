# 문자열 분리
# split()

text = "나는 자랑스러운 태극기 앞에 자유롭고 정의로운 대한민국의 무궁한 영광을 위하여 충성을 다할 것을 굳게 다짐합니다."
print(text.split(" ")) # 공백을 구분자로 하여 문장을 쪼갬

text = '+82-10-1234-5678'
print(text.split("-"))  #"-"을 구분자로 하여 문장을 쪼갬
# split(sep='-', maxsplit=2)
# sep: 구분자
# maxsplit: 최대 구분 개수
print(text.split("-", 2)) # 2개까지만 제한한다는 의미


# 좌우 공백 제거
# strip: 좌우 모두
# lstrip: 왼쪽만
# rstrip: 오른쪽만
text = "     토실토실 아기 돼지    "
print(text.strip())

text = "\n\n\n\n토실토실 아기 돼지\n\n\n\n"
print(text.strip("\n"))

text = "XXaaaaa토실토실 아기 돼지aaaaa"
print(text.strip("a"))

text = "ababab토실토실 아기 돼지ababab"
print(text.strip("ab"))

text = "aaabbbccccc토실토실 아기 돼지aaabbbccccc"
print(text.strip("abc"))

text = "ssss토실토실 아기 돼지sssss"
print(text.lstrip('s'))

text = "ssss토실토실 아기 돼지sssss"
print(text.rstrip('s'))

# join() - 문자열 연결
# 문자열1. join(문자열2)
text1 = "->"
text2 = ["인천", "도쿄", "뉴욕", "파리"]
print(text1.join(text2))

# find() - 문자열 검색
# 찾고자 하는 문자또는 문자열의 첫 번째 위치를 반환한다. 찾지못하면 -1을 반환한다.
text = "송아지 송아지 얼룩 송아지"
print(text.find("지"))  # 첫번째 지 출력

text = "송아지 송아지 얼룩 송아지"
print((text.find("얼룩")))

# count() - 문자열 개수 세기
text = "송아지 송아지 얼룩 송아지"
print(text.count("송아지"))

# startswith(), endswith()
# 문자열이 특정 문자열로 시작하거나 끝나는지 확인한다.
animals = ['강아지', '송아지', '돼지']
for i in animals:
    print(i.startswith('강'))

animals = ['강아지', '송아지', '돼지']
for i in animals:
    print(i.endswith('지'))

# replace() - 문자열 치환
# 지정된 문자열을 다른 문자열로 바꾼다.    
text = '강아지'
print(text.replace('강', '송'))

# lower(), upper() - 대소문자 변환
text = 'Coffee'
print(text.lower())  # 소문자 출력
print(text.upper())  # 대문자 출력