# src/rag_utils.py
from langchain.tools import tool
import chromadb
from langchain_ollama import OllamaEmbeddings


@tool
def search_manual(query: str) -> str:
    """当用户询问关于特斯拉汽车的具体问题（如：胎压、故障灯、操作说明、保养等），必须调用此工具查阅官方手册。"""
    embedding_model = OllamaEmbeddings(
        model="bge-m3",
        base_url="http://127.0.0.1:11434"
    )
    client = chromadb.PersistentClient(path="./chroma_db")
    collection = client.get_or_create_collection("car_manual")

    query_vector = embedding_model.embed_query(query)
    results = collection.query(query_embeddings=[query_vector], n_results=2)

    if not results['documents'] or not results['documents'][0]:
        return "在手册中没有找到相关内容。"
    return "\n\n".join(results['documents'][0])