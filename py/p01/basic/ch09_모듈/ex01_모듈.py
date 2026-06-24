# 모듈
# diet.py
'''
변수: menu
함수: get_recomment_weight()
'''
# import 모듈
import diet
# 모듈.함수
diet.get_recommend_weight(160, False)

# import 모듈 as 별칭
import diet as dd
dd.get_recommend_weight(160, False)

dd.print_valid_menu()
print(dd.menu)

# from 모듈 import 함수, 변수, 모듈
from diet import get_recommend_weight, print_valid_menu
get_recommend_weight(160, False)

print_valid_menu()