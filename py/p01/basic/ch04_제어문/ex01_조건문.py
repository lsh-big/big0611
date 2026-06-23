# 제어문 
# 조건문
'''

들여쓰기(indent)
4칸 스페이스바 & 탭키
if 조건식:
    수행문1
else
    수행문2

조건식은 결과가 True 또는 False
비교(> < >= <= == !=), 논리 (and, or, not) 연산의 결과는  True or False.
'''

today_temp = 30

if today_temp > 0:
# print("아이스 아메리카노")
# IndentationError: expected an indented block after 'if' statement on line 18  -> # 들여쓰기 안해서 오류남.
    print("아이스 아메리카노")

today_temp = -10
if today_temp > 0:
    print("아이스 아메리카노")
else:
    print("따뜻한 아메리카노")    

# elif    
'''
if 조건식:
    수행문1
elif 조건식2:
    수행문2    
elif 조건식3:
    수행문2    
else
    수행문4
'''
today_temp = 22

if today_temp > 0:
    print("아이스 아메리카노")
elif today_temp == 0:
    print("디카페인 아메리카노")
else:
    print("따뜻한 아메리카노")

# 중첩 if
weather = "비"
today_temp = 30

if weather == "맑음":
    if today_temp > 0:
        print("아이스 아메리카노")
    elif today_temp == 0:
        print("디카페인 아메리카노")
    else:
        print("따뜻한 아메리카노")
else:
    print('먹지마!')

# 영어 90점 이상, 수학 90점 이상: 용돈 인상
# 영어 80점 이하, 수학 80점 이하: 용돈 삭감
# and   
math_score = 80
eng_score = 100
if eng_score >= 90 and math_score >= 90:
    print("용돈 인상")
elif eng_score <= 80 and math_score <= 80:
    print("용돈 삭감")
else :
    print("동결")    

# or
math_score = 80
eng_score = 100
if eng_score >= 90 or math_score >= 90:
    print("용돈 인상")
elif eng_score <= 80 or math_score <= 80:
    print("용돈 삭감")
else :
    print("동결")    