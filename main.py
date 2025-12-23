import streamlit as st
from PIL import Image

# 브라우저 제목 변경
st.set_page_config(
    page_title="융합탐구반 온라인 전시 사이트",
    page_icon="mark.png"
)

st.write("융합탐구반 온라인 전시 사이트입니다.")

rows = [
    ("김학생", "Streamlit 공식 사이트", "https://streamlit.io"),
    ("이학생", "Streamlit 문서", "https://docs.streamlit.io"),
    ("박학생", "GitHub 저장소", "https://github.com"),
    ("최학생", "OpenAI 홈페이지", "https://openai.com"),
]

# 헤더 행
h1, h2, h3 = st.columns([2, 4, 2])
h1.markdown("**작성자**")
h2.markdown("**설명**")
h3.markdown("**링크**")

st.divider()

# 데이터 행 (4행)
for author, desc, link in rows:
    c1, c2, c3 = st.columns([2, 4, 2])
    c1.write(author)
    c2.write(desc)
    c3.link_button("바로가기", link)
