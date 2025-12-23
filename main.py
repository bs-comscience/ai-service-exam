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

for author, desc, link in rows:
    col1, col2, col3 = st.columns(
        [1.2, 2.8, 1],   # 👉 모바일 기준으로 비율 조정
        gap="small"
    )
    col1.write(author)
    col2.write(desc)
    col3.link_button("이동", link)
