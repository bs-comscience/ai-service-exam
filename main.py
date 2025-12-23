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

# 🔧 모바일 한 줄 유지용 CSS
st.markdown("""
<style>
/* 텍스트 줄바꿈 방지 */
div[data-testid="stMarkdownContainer"] p {
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    font-size: 0.85rem;
}

/* link_button 최소화 */
a[data-testid="stLinkButton"] {
    padding: 0.25rem 0.5rem !important;
    font-size: 0.75rem !important;
    min-width: unset !important;
}
</style>
""", unsafe_allow_html=True)

for author, desc, link in rows:
    c1, c2, c3 = st.columns([1, 3, 1], gap="small")
    c1.write(author)
    c2.write(desc)
    c3.link_button("링크", link)
