
from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage



llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.5)

def get_llm_response(input_message: str, selected_item: str) -> str:
    """
    入力テキストと選択値を受け取り、LLMからの回答を返す関数。
    エラー時は例外を投げる。
    """
    if selected_item == "健康に関するアドバイザー":
        messages = [
            SystemMessage(content="あなたは健康に関するアドバイザーです。安全なアドバイスを提供してください。"),
            HumanMessage(content=input_message),
        ]
    else:
        messages = [
            SystemMessage(content="あなたは歴史に関するアドバイザーです。"),
            HumanMessage(content=input_message),
        ]
    response = llm.invoke(messages)
    return response.content


st.title("Lesson21_Chapter6 ②: LLM機能を搭載したWebアプリを開発しよう")
st.write("##### 動作モード1: 健康に関するアドバイザー")
st.write("健康に関する質問を入力することで、AIが回答します。")
st.write("##### 動作モード2: 歴史に関するアドバイザー")
st.write("歴史に関する質問を入力することで、AIが回答します。")

selected_item = st.radio(
    "動作モードを選択してください。",
    ["健康に関するアドバイザー", "歴史に関するアドバイザー"]
)

st.divider()

if selected_item == "健康に関するアドバイザー":
    input_message = st.text_input(label="健康に関する質問を入力してください。")
else:
    input_message = st.text_input(label="歴史に関する質問を入力してください。")

if st.button("実行"):
    st.divider()
    if input_message:
        try:
            response_text = get_llm_response(input_message, selected_item)
            st.write(response_text)
        except Exception as e:
            st.error(f"AIの応答取得中にエラーが発生しました: {e}")
    else:
        st.error("質問内容を入力してから「実行」ボタンを押してください。")
