# src/hardware_tools.py
from langchain.tools import tool
import psutil

@tool
def get_vehicle_battery() -> str:
    """查询当前车辆电池电量（SOC）。当用户问及续航、电量时调用。"""
    try:
        battery = psutil.sensors_battery()
        if battery:
            charging = "正在充电" if battery.power_plugged else "未充电"
            return f"当前车辆动力电池电量为 {battery.percent}%，{charging}。"
    except Exception:
        pass
    return "当前车辆电池电量为 85%。"

@tool
def get_cabin_temperature() -> str:
    """查询当前车内/电机温度。当用户说'我有点热/冷'等模糊感受时，必须先调用此工具。"""
    try:
        cpu_load = psutil.cpu_percent(interval=0.5)
        simulated_temp = 22.0 + (cpu_load / 10.0)
        return f"当前车内温度约为 {simulated_temp:.1f} 摄氏度（系统负载：{cpu_load}%）。"
    except Exception:
        return "当前车内温度为 26.0 度。"

@tool
def set_ac_temperature(temp: int) -> str:
    """设置空调温度，参数temp是16到30之间的整数。"""
    return f"✅ 空调已设为{temp}度，已为您调节风量。"