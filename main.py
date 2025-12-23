import streamlit as st
from PIL import Image

# 브라우저 제목 변경
st.set_page_config(
    page_title="융합탐구반 온라인 전시 사이트",
    page_icon="mark.png"
)

st.write("융합탐구반 온라인 전시 사이트입니다.")

st.link_button("인터넷 작명소", "https://www.naver.com")
st.link_button("영어 문장 자동 생성", "https://www.naver.com")
st.link_button("화학....", "https://www.naver.com")
st.link_button("남일사랑 Quiz~!", "https://www.naver.com")

rows = [
    ("Streamlit 공식 사이트", "https://streamlit.io"),
    ("Streamlit 문서", "https://docs.streamlit.io"),
    ("GitHub", "https://github.com"),
    ("OpenAI", "https://openai.com"),
]

for desc, link in rows:
    col1, col2 = st.columns([3, 2])
    col1.write(desc)
    col2.link_button("바로가기", link)
