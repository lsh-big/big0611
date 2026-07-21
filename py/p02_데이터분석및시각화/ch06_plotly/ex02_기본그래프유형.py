# 히스토그램(histogram)
# 빠른 수정: ctrl+.
import numpy as np
import pandas as pd
import plotly.express as px
'''
- 연속 데이터의 분포를 시각화
- 데이터의 빈도와 분포 패턴을 파악

px.histogram()
- data_frame: 데이터프레임
- x: x축 컬럼명
- y: y축 컬럼명
- color: 그룹별 색상 구분
- title: 그래프 제목
- nbins: 구간 수
- marginal: 추가 통계 차트
- opacity: 투명도
- barmode: 막대 배치 방식
'''

# 1. 기본 히스토그램
# 시험 점수 분포 데이터

np.random.seed(42)
'''
무작위(Random) 숫자를 생성할 때 기준이 되는 '시드 값'을 42로 고정합니다. 이 줄 덕분에 코드를 내 컴퓨터에서 실행하든 다른 사람 컴퓨터에서 실행하든 항상 똑같은 무작위 점수 데이터가 만들어져 실험의 재현성을 보장합니다.
42를 1이나 100, 2026 등 다른 숫자로 바꿔도 컴퓨터는 아무런 문제 없이 똑같이 작동합니다.
np.random.seed(42) -> A 형태로 생성된 무작위 배열 출력
np.random.seed(7) -> B 형태로 생성된 무작위 배열 출력
'''
scores = np.random.normal(75, 15, 1000)
'''
통계학의 정규분포(Normal Distribution)를 따르는 난수를 생성합니다.75: 평균 점수($\mu$)15: 표준편차($\sigma$, 점수가 평균으로부터 얼마나 멀리 퍼져 있는지의 척도)1000: 생성할 데이터의 총 개수 (학생 1000명의 점수)결과적으로 75점을 중심으로 종 모양(Bell-curve) 형태로 퍼진 1000개의 점수가 생성됩니다.
'''
scores = np.clip(scores, 0, 100)
'''
정규분포 특성상 무작위로 뽑다 보면 간혹 105점이나 -5점 같은 비현실적인 점수가 나올 수 있습니다.

np.clip(array, min, max)은 데이터 중 0보다 작은 값은 무조건 0으로, 100보다 큰 값은 무조건 100으로 강제 고정하여 시험 점수 세계관에 맞게 데이터를 다듬어주는 역할을 합니다.
'''

df_hist = pd.DataFrame({'점수': scores})

fig = px.histogram(df_hist, x='점수',
                    title='시험 점수 분포',
                    nbins=20,
                    marginal='rug')
'''
nbins=20: 데이터를 쪼갤 막대 격자(Bin)의 개수를 20개로 지정합니다. 0점부터 100점까지의 범위를 20개로 쪼갰으므로, 하나의 막대는 약 5점 단위(0~5, 5~10...)의 범위를 가지며 그 안에 속한 학생 수를 셉니다.
marginal='rug':히스토그램 상단(혹은 하단) 여백에 러그(Rug, 양탄자 술) 플롯을 추가합니다.데이터 포인트 1개당 아주 얇은 세로선 한 줄(|)을 그어주는 방식인데, 막대로 뭉뚱그려진 히스토그램 밑에 실제 데이터가 어디에 촘촘하게 몰려있고 어디가 텅 비었는지 미세하게 짚어주는 서브 차트 역할을 합니다.이 옵션에는 'rug' 외에도 박스플롯을 붙여주는 'box', 바이올린 플롯을 붙여주는 'violin' 등을 넣을 수 있습니다.
'''

fig.update_layout(
    xaxis_title="점수",
    yaxis_title="빈도"
)

fig.show()


# 2. 그룹별 히스토그램
# 성별 키 분포 비교
height_data = []
np.random.seed(42)

# 남성 키 데이터 (평균 175cm)
male_heights = np.random.normal(175, 6, 500)
for height in male_heights:
    height_data.append({'키': height, '성별': '남성'})

# 여성 키 데이터 (평균 162cm)
female_heights = np.random.normal(162, 5, 500)
for height in female_heights:    
    height_data.append({'키': height, '성별': '여성'})

df_height = pd.DataFrame(height_data)

fig = px.histogram(df_height, x='키', 
                   color='성별',
                   title='성별 키 분포 비교',
                   marginal='box',
                   opacity=0.7,
                   barmode='overlay')

fig.update_layout(
    xaxis_title="키 (cm)",
    yaxis_title="빈도"
)

fig.show()