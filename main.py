from fastapi import FastAPI
import requests

app = FastAPI(title="Yori API", version="1.0.0")

@app.get("/")
def home():
    return {
        "status": True,
        "message": "Yori API Online"
    }

@app.get("/ai/code")
def code(prompt: str, history: str = ""):
    r = requests.get(
        "https://apis.prexzyvilla.site/ai/blackbox",
        params={
            "prompt": prompt,
            "history": history
        },
        timeout=120
    )

    data = r.json()

    return {
        "status": True,
        "creator": "Yori",
        "response": data.get("response", "")
    }
