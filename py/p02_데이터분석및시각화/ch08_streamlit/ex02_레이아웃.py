import streamlit as st

st.set_page_config(
    page_title="학생 성적 관리",
    page_icon="📚",
    layout="wide"
)

st.title('페이지 설정이 완료된 애플리케이션')
st.text('페이지 설정이 완료되었습니다.')
st.write('이제 더 넓은 화면에서 볼 수 있습니다!')

# 레이아웃 컴포넌트
# 1. 열로 나누어 배치하기
st.title('학생 정보 관리 시스템')

# 4개의 열로 나누기
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric('전체 학생 수', '245명')
with col2:
    st.metric('평균 점수', '82.5점')
with col3:
    st.metric('출석률', '94.2%')
with col4:
    st.metric('과제 제출률', '87.8%')