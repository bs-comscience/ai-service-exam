import streamlit as st
from openai import OpenAI

# --- API KEY ---
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# 브라우저 제목 변경
st.set_page_config(
    page_title="수준별 영어 문장 만들기",
    page_icon="🇬🇧"
)

st.title("수준별 영어 문장 만들기")
# --- 입력 ---
word = st.text_input("문장 생성에 사용할 영단어", placeholder="vacation")
school_levels = ["중1", "중2", "중3", "고1", "고2", "고3"]

# selectbox로 변경
level = st.selectbox("대상 학교급/학년(어휘 수준)", school_levels)

grammer_list = [ "to 부정사", "동명사", "비교급", "최상급", "원급 비교", "관계대명사"]
grammer = st.multiselect("핵심 문법(중복 선택 가능)", grammer_list)

count = st.text_input("문장 생성 개수", placeholder="3")

# --- 실행 버튼 ---
if st.button("문장 만들기"):
    level_to_lexile_map = {
        "중1": "Lexile=600L~800L",
        "중2": "Lexile=700L~900L",
        "중3": "Lexile=800L~1000L",
        "고1": "Lexile=1000L~1150L",
        "고2": "Lexile=1100L~1200L",
        "고3": "Lexile=1200L~1300L",
    }
    # 원본 코드의 규칙 그대로 유지
    lexile_level = level_to_lexile_map[level]

    prompt = f"영단어 {word}를 사용, 어휘수준 {level}에 맞는, {grammer}를 포함한, 문장 {count}개 생성"

    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[
            {"role": "system", "content": "문장 생성, 번호 부여, 다른 답은 하지 말것"},
            {"role": "user", "content": prompt},
        ]
    )

    # --- 출력 ---
    st.write(response.choices[0].message.content)
