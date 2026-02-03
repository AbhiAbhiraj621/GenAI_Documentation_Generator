from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import requests
import asyncio

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class GenerateRequest(BaseModel):
    pipeline_code: str
    doc_type: str

async def call_llm(prompt: str) -> str:
    def _call():
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "phi3",
                "prompt": prompt,
                "stream": False,
                "options": {
                    "num_predict": 650,
                    "temperature": 0.2,
                    "top_p" : 0.9
                }
            },
            timeout=300
        )
        response.raise_for_status()
        return response.json()["response"]

    return await asyncio.to_thread(_call)

@app.post("/generate")
async def generate(request: GenerateRequest):
    pipeline_code = request.pipeline_code
    doc_type = request.doc_type

    # Prepare prompt for LLM
    prompt = f"""
    You are a senior data engineer. 
    
    Generate {doc_type} documentation for the following ETL code:\n{pipeline_code}
    Rules:
    - Exactly 8 bullet points
    - 1-2 sentences per bullet
    - Max 250 words total
    - Use numeric dates only (YYYY-MM-DD)
    - No introductions or conclusions
    """

    llm_response = await call_llm(prompt)

    return {
        "status": "completed",
        "documentation": llm_response
    }

@app.get("/")
def root():
    return {"status": "OK"}
