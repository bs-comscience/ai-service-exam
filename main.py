import streamlit as st
from PIL import Image

# 브라우저 제목 변경
st.set_page_config(
    page_title="융합탐구반 온라인 전시 사이트",
    page_icon="mark.png"
)

st.write("융합탐구반 온라인 전시 사이트입니다.")

st.markdown("""
<style>
/* link_button 스타일 고정 */
a[data-testid="stLinkButton"] {
    width: 220px !important;
    height: 50px !important;
    display: inline-flex !important;
    justify-content: center !important;
    align-items: center !important;
    font-size: 16px !important;
}
</style>
""", unsafe_allow_html=True)

st.link_button("인터넷 작명소", "https://www.naver.com")
st.link_button("영어 문장 자동 생성", "https://www.naver.com")
st.link_button("화학....", "https://www.naver.com")
st.link_button("남일사랑 Quiz~!", "https://www.naver.com")
