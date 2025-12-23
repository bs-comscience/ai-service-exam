import streamlit as st
from PIL import Image

# 브라우저 제목 변경
st.set_page_config(
    page_title="융합탐구반 온라인 전시 사이트",
    page_icon="mark.png"
)

st.write("융합탐구반 온라인 전시 사이트입니다.")

rows = [
    ("1404 김예준", "영어 문장 자동 생성", "https://streamlit.io"),
    ("1723 정홍재", "인터넷 작명소", "https://docs.streamlit.io"),
    ("1825 조현욱", "화학....", "https://github.com"),
    ("1723 정홍재", "남일사랑 Quiz!\n퀴즈를 다 풀면 선착순으로 상품을 증정합니다. 별관 2층 컴퓨터실습실!", "https://openai.com"),
]

st.markdown("""
<style>
/* 전체 행 */
.rowline{
  display:flex;
  align-items:center;
  gap:8px;
  width:100%;
  white-space:nowrap;
  padding:6px 4px;
  border-bottom:1px solid rgba(0,0,0,0.08);   /* ✅ 행 구분선 */
}

/* 마지막 행 선 제거 */
.rowline:last-child{
  border-bottom:none;
}

/* 작성자 */
.rowline .author{
  flex:0 1 auto;
  max-width:120px;
  overflow:hidden;
  text-overflow:ellipsis;
  font-size:0.85rem;
}

/* 설명 */
.rowline .desc{
  flex:1 1 auto;
  overflow:hidden;
  text-overflow:ellipsis;
  font-size:0.85rem;
  padding-left:6px;
  border-left:1px solid rgba(0,0,0,0.05);     /* ✅ 열 구분 느낌 */
}

/* 링크 */
.rowline .link{
  padding-left:6px;
  border-left:1px solid rgba(0,0,0,0.05);     /* ✅ 열 구분 느낌 */
}

.rowline .link a{
  display:inline-block;
  padding:4px 10px;
  border:1px solid rgba(49,51,63,0.2);
  border-radius:10px;
  text-decoration:none;
  font-size:0.75rem;
}
</style>
""", unsafe_allow_html=True)

for author, desc, link in rows:
    st.markdown(
        f"""
        <div class="rowline">
          <div class="author" title="{author}">{author}</div>
          <div class="desc" title="{desc}">{desc}</div>
          <div class="link"><a href="{link}" target="_blank">링크</a></div>
        </div>
        """,
        unsafe_allow_html=True
    )
