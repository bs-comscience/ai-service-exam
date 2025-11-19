import streamlit as st
from openai import OpenAI

# --- API KEY ---
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("수준별 영어 문장 생성기")

# --- 입력 ---
word = st.text_input("문장 생성에 사용할 영단어", "summer")
level = st.text_input("대상 학교급/학년", "고1")
count = st.text_input("문장 생성 개수", "2")

# --- 실행 버튼 ---
if st.button("생성하기"):
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

    prompt = f"영단어 {word}를 사용하여 어휘수준 {level}에 맞는 문장 rmsi{count}개 생성"

    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[
            {"role": "system", "content": "문장 생성, 번호 부여, 다른 답은 하지 말것"},
            {"role": "user", "content": prompt},
        ]
    )

    # --- 출력 ---
    st.write(response.choices[0].message.content)
