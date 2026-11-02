# src/agent_core.py
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from src.hardware_tools import get_vehicle_battery, get_cabin_temperature, set_ac_temperature
from src.rag_utils import search_manual


def build_agent(api_key: str):
    # 解决那个红线问题：把参数传给 ChatOpenAI
    llm = ChatOpenAI(
        model="deepseek-chat",
        api_key=api_key,
        base_url="https://api.deepseek.com",
        temperature=0
    )

    agent = create_agent(
        model=llm,
        tools=[get_vehicle_battery, get_cabin_temperature, set_ac_temperature, search_manual],
        system_prompt="你是智能座舱助手。如果用户问及汽车的具体功能、故障或参数，请优先使用 search_manual 查阅手册。如果是关于温度或电量的感受，先调用相应的硬件工具获取真实数据，再决定是否开空调。"
    )
    return agent