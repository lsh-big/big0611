# 함수 정의
"""
def 함수명([매개변수]):
    문장
    [return]
"""


def test():
    print("함수 연습")


# 함수 호출
"""
함수명([인자])
"""
test()

# 함수 사용의 장점
"""
1. 코드 재사용성
- 동일한 기능을 여러 번 사용할 수 있다.
2. 가독성 향상
- 특정 기능을 함수로 묶어 코드를 체계적으로 관리한다.
3. 유지보수 용이
- 기능별로 분리되어 수정과 디버깅이 쉽다.
"""

# 조건문을 활용한 함수 예제
"""
기온이 0도보다 높으면 '아이스 아메리카노'를 출력하고, 그렇지 않은 경우에는 '핫 아메리카노'를 출력하는 함수를 작성하시오.
"""


def coffee(temp):
    if temp > 0:
        print("아이스 아메리카노")
    else:
        print("핫 아메리카노")


coffee(30)
coffee(-10)


# return문을 사용하면 함수의 결과값을 변수에 저장하여 재활용할 수 있다.
def coffee(temp):
    result = ""
    if temp > 0:
        result = "아이스 아메리카노"
    else:
        result = "핫 아메리카노"
    return result


c = coffee(30)
print("추천 커피는 {}입니다".format(c))

# 1학년 2반의 시험 성적은 다음과 같다.
"""
[80, 90, 70, 65, 85, 95, 90, 80, 75, 80]
"""


# 시험 문제 중, 한 문제가 잘못 출제되어 모두 5점씩 추가 점수를 받도록 조치를 취했다. 변경 후 점수를 반환하는 함수를 작성하시오.
def update_scores(scores):
    new_scores = []

    for s in scores:
        new = s + 5
        new_scores.append(new)
    return new_scores


scores = [80, 90, 70, 65, 85, 95, 90, 80, 75, 80]
new = update_scores(scores)
print(new)

# 동요 '산토끼'에서 '토'는 몇 번이나 나올까?
"""
산토끼 토끼야. 어디를 가느냐. 깡충깡충 뛰면서. 어디를 가느냐.
산고개 고개를. 나혼자 넘어서. 토실토실 알밤을. 주워 올테야.
"""


def get_char_count(lyric, char):
    count = 0
    for l in lyric:
        if l == char:
            count = count + 1
    return count


lyric = """산토끼 토끼야. 어디를 가느냐. 깡충깡충 뛰면서. 어디를 가느냐.
산고개 고개를. 나혼자 넘어서. 토실토실 알밤을. 주워 올 테야."""

print(get_char_count(lyric, "토"))

print(get_char_count(lyric, "산"))

star = """Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky."""

print(get_char_count(star, "w"))

# 여러 값을 반환하는 함수
"""
영어 단어 또는 문장을 인자로 받아서 대문자와 소문자로 출력하는 함수를 작성하시오.
"""


def change_word_case(word):
    upperCase = word.upper()
    lowerCase = word.lower()
    return upperCase, lowerCase


print(change_word_case("I love Seoul."))

upper, lower = change_word_case("I love Seoul.")
print("대문자는 {0} 이고, 소문자는 {1}이야.".format(upper, lower))

# 조건부 return
"""
두 수와 연산자를 입력받아 사칙연산 결과를 출력하는 계산기 함수를 작성하시오.
"""


def calculator(operator, num1, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 != 0:
            return num1 / num2
    else:
        print("{}는 연산이 불가능합니다.".format(operator))
    return -1


print(calculator("+", 200, 300))

print(calculator("*", 50, 7))

print(calculator("?", 89, 20))

# 디폴트 인자
"""
사용자로부터 키와 성별을 입력 받아서 권장 체중을 화면에 출력하는 함수를 작성하시오.
권장 체중은 다음과 같이 계산한다.
- 남성 권장 체중 = (키 - 100) * 0.9
- 여성 권장 체중 = (키 - 100)
"""

# 디폴트(default, 기본값)인자
# 에러: 초기값이 있는 매개변수는 마지막에 기록
def print_weight(height, man=True):
    weight = 0
    if man:
        weight = height - 100
    else:
        weight = (height - 100) * 0.9
    print("권장 체중은 {}kg 입니다".format(weight))


print_weight(170)

print_weight(170, True)

print_weight(170, False)

# def print_weight(man=True, height):
#     weight = 0
#     if man:
#         weight = height - 100
#     else:
#         weight = (height - 100) * 0.9
#     print("권장 체중은 {}kg 입니다".format(weight))


# 가변인자(*args)
# *args를 사용하면 개수에 제한 없이 여러 인자를 튜플 형태로 받을 수 있다.
"""
입력 받은 인자를 모두 더하는 함수를 작성하시오.
"""


def sum(*args):
    print(type(args))  # (1, 2, 3)
    result = 0
    for num in args:
        result += num
    return result


print(sum(1, 2, 3))

print(sum(2, 4, 6, 8, 10))

# 온도 변환 프로그램
'''
(1) 섭씨 온도를 화씨 온도로 변환
화씨 = (섭씨 x 9/5) + 32
(2) 화씨 온도는 소수점 첫째 자리까지만 출력

출력 예시
섭씨 25도는 화씨 77.0도 입니다.
'''

# 함수 사용
def celsius_to_fahrenheit(celsius):
    """섭씨를 화씨로 변환하는 함수 """
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


celsius_temp = 25
fahrenheit_temp = celsius_to_fahrenheit(celsius_temp)
print(f'섭씨 {celsius_temp}도는 화씨 {fahrenheit_temp:.1f}도 입니다.')