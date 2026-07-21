# 데이터 시각화 연습
# 건강검진 정보 데이터 시각화 
# 데이터 준비 및 전처리
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib import font_manager, rc

# 한글 폰트 설정
plt.rcParams['font.family'] = 'NanumGothic'

df = pd.read_csv(
    r"C:\LSH\big0611\py\p02_데이터분석및시각화\ch07_건강검진정보데이터시각화\국민건강보험공단_건강검진정보_2023.csv",
    encoding="cp949"
)

df.head()
df.describe()
df.info()

