from fastapi import FastAPI, HTTPException
from fastapi.responses import Response
import requests

app = FastAPI(title="Yori API", version="1.0.0")


@app.get("/")
def home():
    return {
        "status": True,
        "message": "Yori API Online",
        "endpoints": [
            "/ai/code",
            "/ai/anime",
            "/ai/pixel",
            "/ai/cartoon",
            "/tools/download"
        ]
    }


@app.get("/ai/code")
def code(prompt: str, history: str = ""):
    try:
        r = requests.get(
            "https://apis.prexzyvilla.site/ai/blackbox",
            params={
                "prompt": prompt,
                "history": history
            },
            timeout=120
        )
        r.raise_for_status()
        data = r.json()

        response_text = data.get("response", "")
        if "</think>" in response_text:
            response_text = response_text.split("</think>", 1)[1].strip()

        return {
            "status": True,
            "creator": "Yori",
            "response": response_text
        }

    except requests.RequestException as e:
        raise HTTPException(status_code=502, detail=f"Upstream error: {str(e)}")
    except ValueError:
        raise HTTPException(status_code=502, detail="Invalid JSON from upstream")


@app.get("/ai/anime")
def anime(prompt: str, negative_prompt: str = ""):
    try:
        r = requests.get(
            "https://apis.prexzyvilla.site/ai/anime",
            params={
                "prompt": prompt,
                "negative_prompt": negative_prompt
            },
            timeout=120
        )
        r.raise_for_status()

        return Response(
            content=r.content,
            media_type="image/png"
        )

    except requests.RequestException as e:
        raise HTTPException(status_code=502, detail=f"Upstream error: {str(e)}")


@app.get("/ai/pixel")
def pixel(prompt: str, negative_prompt: str = ""):
    try:
        r = requests.get(
            "https://apis.prexzyvilla.site/ai/pixel-art",
            params={
                "prompt": prompt,
                "negative_prompt": negative_prompt
            },
            timeout=120
        )
        r.raise_for_status()

        return Response(
            content=r.content,
            media_type="image/png"
        )

    except requests.RequestException as e:
        raise HTTPException(status_code=502, detail=f"Upstream error: {str(e)}")


@app.get("/ai/cartoon")
def cartoon(imageurl: str):
    try:
        r = requests.get(
            "https://apis.prexzyvilla.site/ai/cartoon",
            params={"imageurl": imageurl},
            timeout=120
        )
        r.raise_for_status()
        data = r.json()

        return {
            "status": True,
            "creator": "Yori",
            "original_image": data.get("original_image", ""),
            "anime_image": data.get("anime_image", ""),
            "service": data.get("service", "")
        }

    except requests.RequestException as e:
        raise HTTPException(status_code=502, detail=f"Upstream error: {str(e)}")
    except ValueError:
        raise HTTPException(status_code=502, detail="Invalid JSON from upstream")


@app.get("/tools/download")
def download(url: str):
    try:
        r = requests.get(
            "https://apis.prexzyvilla.site/download/aio",
            params={"url": url},
            timeout=120
        )
        r.raise_for_status()
        data = r.json()

        return {
            "status": True,
            "creator": "Yori",
            "platform": data.get("platform", ""),
            "original_url": data.get("original_url", url),
            "media_count": data.get("media_count", 0),
            "has_images": data.get("has_images", False),
            "has_videos": data.get("has_videos", False),
            "has_audios": data.get("has_audios", False),
            "medias": data.get("medias", [])
        }

    except requests.RequestException as e:
        raise HTTPException(status_code=502, detail=f"Upstream error: {str(e)}")
    except ValueError:
        raise HTTPException(status_code=502, detail="Invalid JSON from upstream")
