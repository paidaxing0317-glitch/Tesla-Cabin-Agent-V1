# app.py
import gradio as gr
import os
from dotenv import load_dotenv
from src.agent_core import build_agent

# 1. 加载 .env 文件中的环境变量
load_dotenv()

# 2. 从环境变量中安全地读取 API Key
API_KEY = os.getenv("DEEPSEEK_API_KEY")

if not API_KEY:
    raise ValueError("❌ 未找到 API Key！请检查根目录下的 .env 文件是否正确配置。")

# 3. 调用核心模块构建 Agent
agent = build_agent(API_KEY)

def chat_response(message, history):
    response = agent.invoke({"messages": [("user", message)]})
    return response["messages"][-1].content

demo = gr.ChatInterface(
    fn=chat_response,
    title="🚗 特斯拉智能座舱助手 (企业级架构)",
    description="支持查询手册、读取实时车况硬件数据。你可以问我：'我有点热' 或 '胎压打多少'",
)

if __name__ == "__main__":
    demo.launch()