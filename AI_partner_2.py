import streamlit as st
import os
from openai import OpenAI



st.set_page_config(
    page_title="AI智能伴侣",
    page_icon="🤖",
    #布局
    layout="wide",
    #控制侧边栏状态
    initial_sidebar_state="expanded",
    menu_items={ }
)

#大标题
st.title("AI智能伴侣")

#logo

#系统提示词
system_prompt = "你是一个 helpful的助手，能够帮助用户回答问题，解决问题。"

#初始化聊天信息
if 'messages' not in st.session_state:
    st.session_state.messages = []

#展示聊天信息
for message in st.session_state.messages:
    st.chat_message(message["role"]).write(message["content"])
    # if message ["role"] == "user":
    #     st.chat_message("user").write(message["content"])
    # else:
    #     st.chat_message("assistant").write(message["content"])


#创建与AI大模型交互的客户端对象
client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'),base_url="https://api.deepseek.com")

#消息输入框
prompt = st.chat_input("请输入您的问题：")
if prompt:
    st.chat_message("user").write(prompt)
    print("-------->调用大模型，提示词：", prompt)

    #添加用户消息到会话状态
    st.session_state.messages.append({"role": "user", "content": prompt})

    #调用AI大模型
    response = client.chat.completions.create(
        model="deepseek-flash",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ],
        stream=False,

    )

    #输出大模型的回复
    print("<-------- 大模型回复：", response.choices[0].message.content)
    st.chat_message("assistant").write(response.choices[0].message.content)
    #保存大模型返回结果
    st.session_state.messages.append({"role": "assistant", "content": response.choices[0].message.content})
