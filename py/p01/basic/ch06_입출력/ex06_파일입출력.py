# 파일 입력
# 파일 모드
'''
r(read): 읽기 -> read()
w(write): 쓰기 -> write(), 덮어 씌운다.
a(append): 추가 -> write()
'''

f = open('abc2.txt', 'w')
f.write('a b c d e f g')
f.close()

f = open('abc1.txt', 'w') # w는 덮어씌움
f.write('a b c d e f g')
f.close()

# 추가(append)모드로 파일 열기
f = open('abc1.txt', 'a')
f.write('H I J K L M N O P')
f.close()

# 파일 출력
f =  open('abc1.txt', 'r')
print(f.read())
f.close()

# readlines() 글자를 한줄씩 읽기
f = open('abc2.txt', 'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()

# with 문: close() 자동 처리
'''with open('파일이름.txt', encoding='utf-8') as 별칭(변수):
    별칭.write()
    별칭.read()
    .write('2026년 6월 22일 월요일\n')'''

with open('일기.txt', 'w', encoding='utf-8') as f:
    f.write('2026년 6월 22일 월요일\n')    

with open('일기.txt', 'a', encoding='utf-8') as f:
    f.write('대체로 흐림')

with open('일기.txt', 'r', encoding='utf-8') as f:
    print(f.read())

# 파일 삭제    
# 내부 모듈 가져오기
import os 

fileName = 'abc1.txt'
if os.path.exists(fileName):
    os.remove(fileName)
    print('{}파일을 삭제하였습니다.'.format(fileName))
else:
    print('{}파일이 존재하지 않습니다.'.format(fileName))
