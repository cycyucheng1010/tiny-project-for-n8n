import psutil
from mcp.server.fastmcp import FastMCP

# 初始化 FastMCP
mcp = FastMCP("System Monitor", host="0.0.0.0", port=8888)

@mcp.tool()
def get_system_stats() -> dict:
    """
    獲取目前電腦的資源使用狀況，包括 CPU、記憶體和硬碟。
    """
    # 獲取 CPU 使用率 (阻斷 1 秒以獲得準確數據)
    cpu_usage = psutil.cpu_percent(interval=1)
    
    # 獲取記憶體使用狀況
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    memory_free_gb = round(memory.available / (1024 ** 3), 2)
    
    # 獲取主要硬碟使用狀況
    disk = psutil.disk_usage('/')
    disk_usage = disk.percent
    disk_free_gb = round(disk.free / (1024 ** 3), 2)
    
    return {
        "status": "success",
        "cpu_usage_percent": cpu_usage,
        "memory_usage_percent": memory_usage,
        "memory_free_gb": memory_free_gb,
        "disk_usage_percent": disk_usage,
        "disk_free_gb": disk_free_gb
    }

if __name__ == "__main__":
    mcp.run(transport="sse")