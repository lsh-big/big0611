import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
import numpy as np


# Streamlit 페이지 설정
st.set_page_config(
    page_title="주식 분석기",
    page_icon="📈",
    layout="wide"
)


# 미국 주요 종목 딕셔너리
STOCKS = {
    "AAPL": "Apple Inc.",
    "MSFT": "Microsoft Corp.",
    "GOOGL": "Alphabet Inc.",
    "TSLA": "Tesla Inc.",
    "NVDA": "NVIDIA Corp."
}


# 주식 데이터 가져오기
@st.cache_data(ttl=300)
def get_stock_data(symbol, period="1y"):
    try:
        ticker = yf.Ticker(symbol)
        hist_data = ticker.history(period=period)

        try:
            company_info = ticker.info
        except Exception:
            company_info = {}

        if hist_data.empty:
            return None, None

        return hist_data, company_info

    except Exception as e:
        st.error(f"데이터를 가져오는 중 오류가 발생했습니다: {e}")
        return None, None


# 기업 정보 표시
def display_company_info(company_info, current_price):
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("현재가", f"${current_price:,.2f}")

    with col2:
        market_cap = company_info.get("marketCap")

        if market_cap:
            st.metric("시가총액", f"${market_cap:,.0f}")
        else:
            st.metric("시가총액", "N/A")

    with col3:
        pe_ratio = company_info.get("trailingPE")

        if pe_ratio:
            st.metric("PER", f"{pe_ratio:.2f}")
        else:
            st.metric("PER", "N/A")

    with col4:
        dividend_yield = company_info.get("dividendYield")

        if dividend_yield:
            st.metric(
                "배당수익률",
                f"{dividend_yield * 100:.2f}%"
            )
        else:
            st.metric("배당수익률", "N/A")


# 주가 캔들스틱 차트 생성
def create_price_chart(hist_data, symbol):
    fig = go.Figure()

    fig.add_trace(
        go.Candlestick(
            x=hist_data.index,
            open=hist_data["Open"],
            high=hist_data["High"],
            low=hist_data["Low"],
            close=hist_data["Close"],
            name=symbol
        )
    )

    # 20일 이동평균선
    if len(hist_data) >= 20:
        ma20 = hist_data["Close"].rolling(window=20).mean()

        fig.add_trace(
            go.Scatter(
                x=hist_data.index,
                y=ma20,
                mode="lines",
                name="20일 이동평균",
                line=dict(
                    color="orange",
                    width=2
                )
            )
        )

    # 60일 이동평균선
    if len(hist_data) >= 60:
        ma60 = hist_data["Close"].rolling(window=60).mean()

        fig.add_trace(
            go.Scatter(
                x=hist_data.index,
                y=ma60,
                mode="lines",
                name="60일 이동평균",
                line=dict(
                    color="royalblue",
                    width=2
                )
            )
        )

    fig.update_layout(
        title=f"{symbol} 주가 차트",
        yaxis_title="가격 ($)",
        xaxis_title="날짜",
        height=500,
        xaxis_rangeslider_visible=False,
        template="plotly_white"
    )

    return fig


# 거래량 차트 생성
def create_volume_chart(hist_data, symbol):
    colors = np.where(
        hist_data["Close"] >= hist_data["Open"],
        "#ef5350",
        "#42a5f5"
    )

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=hist_data.index,
            y=hist_data["Volume"],
            marker_color=colors,
            name="거래량"
        )
    )

    fig.update_layout(
        title=f"{symbol} 거래량",
        xaxis_title="날짜",
        yaxis_title="거래량",
        height=350,
        template="plotly_white"
    )

    return fig


# 기술적 지표 계산
def calculate_technical_indicators(hist_data):
    close_price = hist_data["Close"].dropna()

    if len(close_price) < 2:
        return {
            "total_return": 0.0,
            "avg_daily_return": 0.0,
            "volatility": 0.0,
            "max_drawdown": 0.0,
            "sharpe_ratio": 0.0
        }

    # 일일 수익률
    daily_returns = close_price.pct_change().dropna()

    # 총수익률
    total_return = (
        (close_price.iloc[-1] / close_price.iloc[0]) - 1
    ) * 100

    # 일일 평균 수익률
    avg_daily_return = daily_returns.mean() * 100

    # 연간 변동성
    volatility = daily_returns.std() * np.sqrt(252) * 100

    # 최대 낙폭
    cumulative_max = close_price.cummax()
    drawdown = (close_price / cumulative_max) - 1
    max_drawdown = drawdown.min() * 100

    # 샤프 비율
    daily_std = daily_returns.std()

    if daily_std and not np.isnan(daily_std):
        sharpe_ratio = (
            daily_returns.mean() / daily_std
        ) * np.sqrt(252)
    else:
        sharpe_ratio = 0.0

    return {
        "total_return": total_return,
        "avg_daily_return": avg_daily_return,
        "volatility": volatility,
        "max_drawdown": max_drawdown,
        "sharpe_ratio": sharpe_ratio
    }


# 메인 앱
def main():
    st.title("📈 주식 분석 대시보드")
    st.caption("Yahoo Finance 데이터를 이용한 미국 주식 분석")

    col1, col2 = st.columns(2)

    with col1:
        selected_symbol = st.selectbox(
            "분석할 종목을 선택하세요.",
            list(STOCKS.keys()),
            format_func=lambda x: f"{x} - {STOCKS[x]}"
        )

    period_options = {
        "3개월": "3mo",
        "6개월": "6mo",
        "1년": "1y",
        "2년": "2y"
    }

    with col2:
        selected_period = st.selectbox(
            "분석 기간을 선택하세요.",
            list(period_options.keys())
        )

    period_code = period_options[selected_period]

    with st.spinner("주식 데이터를 가져오는 중입니다..."):
        hist_data, company_info = get_stock_data(
            selected_symbol,
            period_code
        )

    if hist_data is None:
        st.error("주식 데이터를 가져올 수 없습니다.")
        return

    current_price = hist_data["Close"].iloc[-1]

    st.divider()

    # 기업 정보
    st.subheader(f"{STOCKS[selected_symbol]} 기업 정보")
    display_company_info(company_info or {}, current_price)

    st.divider()

    # 주가 차트
    st.subheader("주가 차트")
    price_chart = create_price_chart(
        hist_data,
        selected_symbol
    )

    st.plotly_chart(
        price_chart,
        use_container_width=True
    )

    # 거래량 차트
    st.subheader("거래량")
    volume_chart = create_volume_chart(
        hist_data,
        selected_symbol
    )

    st.plotly_chart(
        volume_chart,
        use_container_width=True
    )

    # 기술적 지표
    st.subheader("기술적 지표")

    indicators = calculate_technical_indicators(hist_data)

    metrics_df = pd.DataFrame({
        "지표": [
            "총수익률",
            "일일 평균 수익률",
            "연간 변동성",
            "최대 손실폭",
            "샤프 비율"
        ],
        "값": [
            f'{indicators["total_return"]:.2f}%',
            f'{indicators["avg_daily_return"]:.3f}%',
            f'{indicators["volatility"]:.2f}%',
            f'{indicators["max_drawdown"]:.2f}%',
            f'{indicators["sharpe_ratio"]:.2f}'
        ]
    })

    st.dataframe(
        metrics_df,
        use_container_width=True,
        hide_index=True
    )

    # 최근 데이터
    with st.expander("최근 주가 데이터 확인"):
        recent_data = hist_data[
            ["Open", "High", "Low", "Close", "Volume"]
        ].tail(10)

        st.dataframe(
            recent_data,
            use_container_width=True
        )


# 모든 함수를 정의한 다음 마지막에 실행
if __name__ == "__main__":
    main()