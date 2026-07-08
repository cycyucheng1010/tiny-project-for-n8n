# 1. 使用官方輕量版 Python 3.11 作為基底
FROM python:3.11-slim

# 2. 設定容器內的工作目錄
WORKDIR /app

# 3. 先複製 requirements.txt 並安裝套件（利用 Docker 快取機制加速）
COPY requirements.txt .
RUN grep -vi "pywin32" requirements.txt > req_docker.txt && \
    pip install --no-cache-dir -r req_docker.txt

# 4. 複製你的 Python 原始碼到容器中
COPY system_monitor_server.py .

# 5. 宣告容器會開啟 8888 埠口
EXPOSE 8888

# 6. 執行 Python 程式
CMD ["python", "system_monitor_server.py"]