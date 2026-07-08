# 引入你剛剛寫好的那個檔案（假設檔名叫 system_monitor_server.py）
from mcp.system_monitor_server import get_system_stats

print("正在嘗試抓取系統數據...")
try:
    # 直接呼叫你寫的那個工具函式
    result = get_system_stats()
    print("\n🎉 成功抓取數據！結果如下：")
    import pprint
    pprint.pprint(result)
except Exception as e:
    print(f"\n❌ 抓取失敗，錯誤訊息: {e}")