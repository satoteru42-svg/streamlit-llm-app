import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
import streamlit as st

# Load environment variables
load_dotenv()

# Initialize LangChain LLM
llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

def get_llm_response(input_text, expert_type):
    """
    Function to get LLM response based on input text and expert type.
    """
    system_message = ""
    if expert_type == "ヘルスケア専門家":
        system_message = "You are a healthcare expert."
    elif expert_type == "動物飼育の専門家":
        system_message = "You are an animal care expert."

    messages = [
        SystemMessage(content=system_message),
        HumanMessage(content=input_text),
    ]
    result = llm(messages)
    return result.content

# Streamlit app UI
st.title("専門家アドバイスアプリ")

st.write("このアプリでは、以下の2つの専門家からアドバイスを受けることができます:")
st.write("1. ヘルスケア専門家: 健康に関するアドバイスを提供します。")
st.write("2. 動物飼育の専門家: ペットや動物の飼育に関するアドバイスを提供します。")

# Radio button for expert selection
expert_type = st.radio(
    "専門家の種類を選択してください:",
    ["ヘルスケア専門家", "動物飼育の専門家"]
)

# Input form for user query
user_input = st.text_input("専門家に相談したい内容を入力してください:")

# Button to submit query
if st.button("アドバイスを受ける"):
    if user_input:
        # Get response from LLM
        response = get_llm_response(user_input, expert_type)
        st.write("### 専門家からのアドバイス:")
        st.write(response)
    else:
        st.error("相談内容を入力してください！")