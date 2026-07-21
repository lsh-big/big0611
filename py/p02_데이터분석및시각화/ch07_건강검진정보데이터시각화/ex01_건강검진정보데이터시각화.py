# 데이터 시각화 연습
# 건강검진 정보 데이터 시각화 
# 데이터 준비 및 전처리

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.rcParams['font.family'] = 'Malgun Gothic'

# 한글 폰트 설정
plt.rcParams['font.family'] = 'NanumGothic'

df = pd.read_csv(
    r"C:\LSH\big0611\py\p02_데이터분석및시각화\ch07_건강검진정보데이터시각화\국민건강보험공단_건강검진정보_2023.csv",
    encoding="cp949"
)

df.head()
df.describe()
df.info()

# 1. 불필요한 컬럼 제거 및 컬럼명 변경
# 컬럼 삭제
df.drop(['기준년도', '치아마모증유무', '제3대구치(사랑니) 이상'], inplace=True, axis = 1)

df.rename(columns={'연령대코드(5세단위)':'연령코드', '신장(5cm단위)': '신장', '체중(5kg단위)': '체중', '식전혈당(공복혈당)': '혈당'}, inplace=True)

# 결측치(NaN) 제거
df = df.dropna()
df.info()
df.head()
## 전체 데이터 분포 시각화
fig, axs = plt.subplots(5, 5)
fig.set_size_inches(20,24)

for i in range(5):
    for j in range(5):
        attr = i * 5 + j + 1
        if df[df.columns[attr]].nunique() < 30:
            sns.countplot( x=df.columns[attr], data=df,ax=axs[i][j])
        else:
            sns.histplot( x=df.columns[attr], data=df, kde=True, ax=axs[i][j])

print(df.shape)
# df[df.columns[attr]].nunique() < 30:
df.columns
df.columns[attr]
df['음주여부']
df['음주여부'].unique()
df['음주여부'].value_counts()