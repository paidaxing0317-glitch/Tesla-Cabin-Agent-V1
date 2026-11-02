# 🚗 特斯拉智能座舱 Agent (RAG + Tool Calling)

基于 LangChain 和 Gradio 开发的智能座舱助手，具备**本地知识库检索**和**实时硬件数据感知**能力。

## ✨ 核心功能
1. **RAG 知识检索**：基于本地部署的 `bge-m3` 模型和 `ChromaDB` 向量数据库，能够精准查询《特斯拉车主手册》（800+文本块），解决大模型“幻觉”问题。
2. **工具调用 (Agent)**：基于 LangChain 最新 `create_agent` 构建，能自动判断用户意图，调用不同的工具。
3. **真实硬件感知**：通过 Python `psutil` 库实时读取系统 CPU 温度和电池电量，模拟真实车辆 CAN 总线数据交互。
4. **流式交互 Web UI**：使用 Gradio 搭建友好的聊天界面。

## 🛠️ 技术栈
- **大语言模型**：DeepSeek-Chat (通过 API)
- **Embedding 模型**：Ollama (bge-m3)
- **框架**：LangChain 1.x, Gradio
- **数据库**：ChromaDB

## 🚀 快速开始
1. 安装依赖：`pip install -r requirements.txt`
2. 确保本地 Ollama 已启动：`ollama serve`
3. 运行项目：`python app.py`