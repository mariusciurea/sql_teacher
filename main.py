import os
from google.adk.cli.fast_api import get_fast_api_app
from fastapi import FastAPI

AGENT_DIR = os.path.dirname(os.path.abspath(__file__))

# Create FastAPI app with enabled cloud tracing
app: FastAPI = get_fast_api_app(
    agents_dir=AGENT_DIR,
    web=True,
)

app.title = "teacher-agent"
app.description = "API for interacting with the Agent teacher-agent"


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8080)