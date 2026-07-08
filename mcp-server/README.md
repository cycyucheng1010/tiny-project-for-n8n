# PC Status Monitor MCP Server

A lightweight Model Context Protocol (MCP) server built with Python and FastMCP. This project exposes your computer's system hardware status (CPU, memory, and disk usage) as a standard MCP tool. It is designed to run over SSE (Server-Sent Events) for seamless integration with automation platforms like **n8n** and LLM clients.

---

## 🚀 Features

- **Real-time CPU Metrics**: Fetches current CPU utilization (averaged over 1 second).
- **Memory Monitor**: Returns total memory usage percentage and remaining free memory (in GB).
- **Disk Inspector**: Returns primary storage usage percentage and available space (in GB).
- **Standardized MCP Tool**: Exposes the `get_system_stats` tool which any MCP-compliant client can discover and call.
- **SSE Transport**: Runs over Server-Sent Events on port `8888` for simple network connectivity.
- **Dockerized**: Includes a Docker setup for containerized deployments.

---

## 📁 Project Structure

- **`system_monitor_server.py`**: The core FastMCP server file defining the `get_system_stats` tool and running the SSE listener.
- **`test_stats.py`**: A helper script to verify system stats fetching locally without launching the full server.
- **`Dockerfile`**: Defines the container build configuration for hosting the MCP server.
- **`requirements.txt`**: Project dependencies (fully cross-platform compatible).

---

## 🛠️ Local Installation & Running

### 1. Prerequisite
Ensure you have **Python 3.10+** installed.

### 2. Setup Virtual Environment
```bash
# Create virtual environment
python -m venv env

# Activate virtual environment
# On Windows:
.\env\Scripts\activate
# On Linux/macOS:
source env/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Verify System Data Fetching
Run the diagnostic script to ensure `psutil` can read your system stats:
```bash
python test_stats.py
```

### 5. Launch the MCP Server
Start the SSE server:
```bash
python system_monitor_server.py
```
The server will boot up and print:
`INFO: Uvicorn running on http://0.0.0.0:8888 (Press CTRL+C to quit)`

---

## 🐳 Docker Deployment

### 1. Build the Docker Image
```bash
docker build -t pc-monitor-mcp:latest .
```

### 2. Run the Container
Run the container and map port `8888` to your host machine:
```bash
docker run -d \
  --name my-mcp-server \
  -p 8888:8888 \
  --pid=host \
  pc-monitor-mcp:latest
```
*(Note: `--pid=host` is used to allow the container to access host processes. When running Docker Desktop on Windows, the metrics will reflect the WSL 2 virtual machine environment rather than the native host Windows OS).*

---

## 🔗 Connecting with n8n

This MCP server uses **Server-Sent Events (SSE)**. You can connect it to n8n to build automated workflows that monitor system health or trigger alerts:

1. **Host Address**: `http://localhost:8888` (or your machine's LAN IP if running Docker or on a remote machine).
2. **Endpoint path**: FastMCP hosts the SSE endpoint at `/sse` and client messages at `/messages/`.
3. **In n8n**:
   - Use the **MCP Node** or an **HTTP Request Node** to connect.
   - Point your configuration to the SSE endpoint: `http://<YOUR_IP>:8888/sse`.
   - The node will auto-discover the `get_system_stats` tool.
   - Call the tool to retrieve the JSON payload containing your CPU, memory, and disk usage.