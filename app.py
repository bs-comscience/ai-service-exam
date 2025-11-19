{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPRjTV0eg1GIbdDAg5IpMEE"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "BBLPCdrcm3oP"
      },
      "outputs": [],
      "source": [
        "import streamlit as st\n",
        "from openai import OpenAI\n",
        "\n",
        "# --- 기본 설정 ---\n",
        "st.set_page_config(page_title=\"영어 문장 생성기\", layout=\"centered\")\n",
        "st.title(\"📘 영어 문장 생성기 (GPT)\")\n",
        "\n",
        "# --- API KEY (Streamlit Secrets 사용 권장) ---\n",
        "api_key = st.secrets.get(\"OPENAI_API_KEY\", \"\")\n",
        "\n",
        "if not api_key:\n",
        "    st.warning(\"⚠️ OPENAI_API_KEY가 설정되지 않았습니다. Streamlit Cloud → Secrets에 API 키를 입력하세요.\")\n",
        "else:\n",
        "    client = OpenAI(api_key=api_key)\n",
        "\n",
        "# --- 입력 UI ---\n",
        "word = st.text_input(\"📝 문장 생성에 사용할 영단어 (콤마로 여러 개 가능)\", \"summer\")\n",
        "level = st.selectbox(\"🎓 대상 학교급/학년\", [\"중1\", \"중2\", \"중3\", \"고1\", \"고2\", \"고3\"])\n",
        "count = st.number_input(\"✏️ 생성할 문장 개수\", min_value=1, max_value=10, value=2)\n",
        "\n",
        "# --- 학년 → 어휘 Lexile 변환 ---\n",
        "level_to_lexile_map = {\n",
        "    \"중1\": \"Lexile=600L~800L\",\n",
        "    \"중2\": \"Lexile=700L~900L\",\n",
        "    \"중3\": \"Lexile=800L~1000L\",\n",
        "    \"고1\": \"Lexile=1000L~1150L\",\n",
        "    \"고2\": \"Lexile=1100L~1200L\",\n",
        "    \"고3\": \"Lexile=1200L~1300L\",\n",
        "}\n",
        "\n",
        "lexile_level = level_to_lexile_map[level]\n",
        "\n",
        "# --- 버튼 동작 ---\n",
        "if st.button(\"🚀 문장 생성하기\"):\n",
        "\n",
        "    if not api_key:\n",
        "        st.error(\"🚫 API 키가 설정되어 있지 않습니다.\")\n",
        "        st.stop()\n",
        "\n",
        "    prompt = f\"영단어 {word}를 사용하여 어휘수준 {lexile_level}에 맞는 문장을 총 {count}개 생성해줘.\"\n",
        "\n",
        "    with st.spinner(\"문장을 생성하는 중입니다...\"):\n",
        "\n",
        "        response = client.chat.completions.create(\n",
        "            model=\"gpt-4.1\",\n",
        "            messages=[\n",
        "                {\"role\": \"system\", \"content\": \"번호를 붙여 문장만 생성하고 설명은 하지 마세요.\"},\n",
        "                {\"role\": \"user\", \"content\": prompt},\n",
        "            ],\n",
        "        )\n",
        "\n",
        "        result = response.choices[0].message.content\n",
        "\n",
        "    st.success(\"완료!\")\n",
        "    st.write(result)\n"
      ]
    }
  ]
}