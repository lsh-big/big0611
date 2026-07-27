
import streamlit as st
import pandas as pd

# 학생 성적 데이터 만들기
data = {
    '이름': ['김철수', '이영희', '박민수', '최지연'],
    '수학': [85, 92, 78, 96],
    '영어': [88, 85, 90, 93],
    '과학': [90, 88, 85, 89]
}

# 데이터 분석
df = pd.DataFrame(data)

# 웹 브라우저 표시할 콘텐츠
st.title('학생 성적 데이터 표시하기')
st.dataframe(df)

# 온라인 쇼핑몰 판매 데이터
sales_data = {
    '상품명': ['노트북', '마우스', '키보드', '모니터', '헤드셋'],
    '가격': [1200000, 25000, 80000, 350000, 150000],
    '판매량': [15, 120, 85, 30, 45],
    '평점': [4.5, 4.2, 4.7, 4.1, 4.6]
}

df = pd.DataFrame(sales_data)

# 평점에 따라 색깔 적용
def color_rating(val):
    if val >= 4.5:
        color = 'green'
    elif val >= 4.0:
        color = 'orange' 
    else:
        color = 'red'
    return f'color: {color}'

# 스타일 적용해서 표시
styled_df = df.style.format({
    '가격': '{:,}원',
    '판매량': '{:,}개',
    '평점': '{:.1f}점'
}).applymap(color_rating, subset=['평점'])

st.dataframe(styled_df)

# 기본 차트 컴포넌트
# 1. 선 그래프로 추세 보기
# 웹사이트 방문자 수 데이터 만들기
import numpy as np
from datetime import datetime, timedelta
dates = [datetime.now() - timedelta(days=x) for x in range(30, 0, -1)]
visitors = np.random.randint(100, 500, 30)

visitor_df = pd.DataFrame({
    'Date': dates,
    'Visitors': visitors
})

# 콘텐트 구성
st.title('기본 차트 예시')
st.subheader('웹사이트 방문자 수')
st.line_chart(visitor_df.set_index('Date')['Visitors'])

# 도시별 인구 비교
population_data = {
    '서울': 9720000,
    '부산': 3390000,
    '인천': 2950000,
    '대구': 2410000,
    '대전': 1490000
}

population_df = pd.DataFrame(list(population_data.items()), columns=['도시', '인구수'])
st.subheader('주요 도시 인구 비교')
st.bar_chart(population_df.set_index('도시')['인구수'])


# 월별 매출 구성 비교
monthly_data = pd.DataFrame({
    'Date': dates,
    '온라인_매출': np.random.randint(50, 150, 30),
    '오프라인_매출': np.random.randint(80, 200, 30),
    '모바일_매출': np.random.randint(30, 100, 30)
})

st.subheader('채널별 매출 구성 변화')
st.area_chart(monthly_data.set_index('Date'))