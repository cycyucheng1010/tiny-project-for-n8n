# Tiny Project for Connecting n8n with MCP

## System Architecture

* The system uses Docker to run both **n8n** and the **MCP server**.
* The MCP server uses **FastMCP** to create an MCP service for PC status monitoring.
* **n8n** uses the **Google Gemini AI Agent** to process user inputs and send emails. The AI Agent uses the **MCP client** to fetch PC status details from the MCP server.

![n8n testing](system_architecture.png)

## Workflow

1. When a user sends a chat message to n8n, the workflow is triggered.
2. The AI Agent processes the user input, queries the MCP server for system stats if needed, and can send an email to the user.

## How to Run

```bash
docker compose up -d --build
```

## Future Work

* Add a cron job to query the MCP server every 10 minutes and log the data to Google Sheets.