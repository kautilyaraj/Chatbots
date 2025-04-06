
from fastapi import FastAPI, Request
from pydantic import BaseModel
import subprocess

app = FastAPI()

class ChatRequest(BaseModel):
    query: str

@app.post("/chat")
def chat_with_obx(request: ChatRequest):
    prompt = request.query
    full_prompt = f"User: {prompt}\nAI:"
    result = subprocess.run(
        ["./main", "-m", "./mistral_model/mistral-7b-instruct.gguf", "-p", full_prompt, "-n", "200"],
        capture_output=True,
        text=True
    )
    output = result.stdout.strip()
    return {"response": output}
