# 시스템 입력
# input()
print(input('입력:'))

# 사용자로부터 이름을 입력
'''
이름을 입력하세요: 홍길동
'''

name = input('이름을 입력하세요:')
print(name + '님, 안녕하세요')

# 키에 따른 권장 체중
# 입력받은 input 값은 문자열이다. -> '170'
height = int(input('키를 입력하세요:'))
weight = (height - 100) * 0.9
# print('당신의 권장체중은 weightkg 입니다.')

print('당신의 권장체중은 ' + str(weight) + 'kg 입니다.')

# print('당신의 권장체중은 {}kg 입니다.'.fomat(weight))
# print(f'당신의 권장체중은 {weight}kg 입니다.')