# 예외처리
# 파이썬에서는 예약어 표에서 보았던try와except를 사용하여 예외를 잡아냅니다.
try:
    # 💥 에러가 발생할 가능성이 있는 코드
    num = int(input("숫자를 입력하세요: "))
    print(f"입력하신 숫자는 {num}입니다.")
except:
    # 🛠️ 에러가 발생했을 때 우회해서 실행할 대처 코드
    print("⚠️ 에러 발생: 올바른 숫자를 입력하셔야 합니다!")

print("프로그램이 죽지 않고 안전하게 다음 코드로 넘어왔습니다.")


# 예외 처리의 완성형 구조
try:
    f = open("data.txt", "r", encoding="utf8")
except FileNotFoundError:
    print("파일이 존재하지 않습니다.")
else:
    print("파일을 성공적으로 읽었습니다.")  # 에러가 없을 때만 실행
finally:
    print("구문을 종료합니다.")            # 에러가 나든 안 나든 무조건 실행

# 구체적인 에러 메시지 받아오기
try:
    result = 10 / 0
except ZeroDivisionError as e:
    # 컴퓨터가 내뱉는 공식 에러 메시지를 e라는 변수에 담아 출력합니다.
    print(f"에러가 발생했습니다. 원인: {e}")
    # 출력: 에러가 발생했습니다. 원인: division by zero    

# 의도적으로 에러 발생시키기
age = -5

# if age < 0:
#     # 의도적으로 ValueError를 발생시킴
#     raise ValueError("나이는 음수가 될 수 없습니다.")

# 예외 처리
'''
try:
    예외 발생 code
except Exception as e:
    특정 예외 처리 code
except:
    모든 예외 처리 code
finally:
    항상 실행되는 code
'''

# 사용자로부터 나이를 입력받아 유효성을 검증하는 코드를 작성하시오. 사용자가 잘못된 값을 입력하더라도 프로그램이 중단되지 않고 올바른 값을 입력할 때까지 반복 요청하시오.

# 나이 입력 및 검증 시스템
def get_valid_age():
    while True:
        try:
            age_input = input("나이를 입력하세요: ")
            age = int(age_input)

            if age < 0:
                print('나이는 0 이상이어야 합니다.')
                continue
            elif age > 150:
                print('유효하지 않은 나이입니다.')
                continue
            else:
                return age
        
        except ValueError as e:
            print('숫자만 입력해주세요:{e}')
        except KeyboardInterrupt:
            print('\n프로그램을 종료합니다.')
            break

# 함수 호출
try:
    user_age = get_valid_age()
    if user_age:
        print(f'입력하신 나이는 {user_age}세입니다.')
except:
    print('예상치 못한 오류가 발생했습니다.')

'''
출력결과
나이를 입력하세요: -100
나이는 0 이상이어야 합니다.
나이를 입력하세요: 300
유효하지 않은 나이입니다.
나이를 입력하세요: 다섯살
숫자만 입력해주세요.
나이를 입력하세요: 5세
숫자만 입력해주세요.
나이를 입력하세요: #$%%^
숫자만 입력해주세요.
나이를 입력하세요: 30
입력하신 나이는 30세입니다.
'''