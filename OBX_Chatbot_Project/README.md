
# OBX 4.0 – AI Employee Chatbot (Offline)

**Goal:** Internal Chatbot to answer employee queries (HR, IT, Finance, Project)

**LLM Used:** Mistral-7B-Instruct (GGUF format)
**Framework:** llama.cpp + FastAPI
**Fine-Tuning:** 1000 Q&A using prompt-completion format
**Platform:** Runs on Windows locally (No API cost)

## Setup Instructions:
1. Download `mistral-7b-instruct.gguf` from HuggingFace and place inside `mistral_model/`
2. Install llama.cpp: `git clone`, `cmake`, and `make`
3. Run FastAPI: `uvicorn app:app --reload`
4. Use Postman or simple HTML to hit `/chat` endpoint.

**Optional UI:** Connect with text-generation-webui frontend for ChatGPT-like interface.
