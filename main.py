from fastapi import FastAPI
from fastapi.responses import Response
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
    response_text = data.get("response", "")

    if "</think>" in response_text:
        response_text = response_text.split("</think>", 1)[1].strip()

    return {
        "status": True,
        "creator": "Yori",
        "response": response_text
    }

@app.get("/ai/anime")
def anime(prompt: str, negative_prompt: str = ""):
    r = requests.get(
        "https://apis.prexzyvilla.site/ai/anime",
        params={
            "prompt": prompt,
            "negative_prompt": negative_prompt
        },
        timeout=120
    )

    return Response(
        content=r.content,
        media_type="image/png"
    )

@app.get("/ai/pixel")
def pixel(prompt: str, negative_prompt: str = ""):
    r = requests.get(
        "https://apis.prexzyvilla.site/ai/pixel-art",
        params={
            "prompt": prompt,
            "negative_prompt": negative_prompt
        },
        timeout=120
    )

    return Response(
        content=r.content,
        media_type="image/png"
    )

@app.get("/ai/cartoon")
def cartoon(imageurl: str):
    r = requests.get(
        "https://apis.prexzyvilla.site/ai/cartoon",
        params={"imageurl": imageurl},
        timeout=120
    )

    data = r.json()

    return {
        "status": True,
        "creator": "Yori",
        "original_image": data.get("original_image", ""),
        "anime_image": data.get("anime_image", ""),
        "service": data.get("service", "")
    }
