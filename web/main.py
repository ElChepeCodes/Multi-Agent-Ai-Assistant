import json
from fastapi import FastAPI, Request, WebSocket
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import requests
from dotenv import load_dotenv
import os

app = FastAPI()
app.mount("/static", StaticFiles(directory="web/static"), name="static")
templates = Jinja2Templates(directory="web/templates")

# Connect to Ollama (running in Docker)
OLLAMA_URL = "http://localhost:11434"

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.websocket("/chat")
async def websocket_chat(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            user_input = await websocket.receive_text()
            
            # Stream response from DeepSeek
            load_dotenv()

            response = requests.post(
                f"{OLLAMA_URL}/api/generate",
                json={
                    "model": os.getenv("MODEL_NAME"),
                    "prompt": user_input,
                    "stream": False
                },
                stream=True
            )
            
            full_response = ""
            for chunk in response.iter_lines():
                if chunk:
                    data = json.loads(chunk.decode())
                    token = data.get("response", "")
                    full_response += token
                    await websocket.send_text(token)
                    
    except Exception as e:
        print(f"Error: {e}")
    finally:
        await websocket.close()