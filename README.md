# MCP Tool Server (FastAPI)

A lightweight **Model Context Protocol (MCP)**-style server built with **FastAPI** that exposes backend tools (e.g., sentiment analysis, calculator) to LLM/agent workflows via structured JSON requests and responses.

## Key Features
- Tool routing layer to invoke backend utilities through a single API
- Structured JSON I/O designed for LLM/agent compatibility
- Example tools included: sentiment analysis + calculator
- Clean, minimal project structure for easy extension

## Project Structure
.
├── main.py
├── tools_registry.py
├── tools/
├── models/
├── ml_training/
└── README.md

## API Endpoints

### POST /invoke-tool
Invokes a registered backend tool using structured JSON input.

**Request**
```json
{
  "tool": "sentiment",
  "input": "I really like how this MCP server works"
}

{
  "tool": "sentiment",
  "result": {
    "label": "positive",
    "score": 0.91
  }
}

**Response**
```json
{
  "tool": "sentiment",
  "result": {
    "label": "positive",
    "score": 0.91
  }
}

### Available Tools
- `sentiment` – sentiment analysis on input text
- `calculator` – evaluates arithmetic expressions


