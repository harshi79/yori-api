from fastapi import FastAPI, HTTPException
from fastapi.responses import Response, HTMLResponse
from fastapi.openapi.docs import get_redoc_html
import requests

app = FastAPI(
    title="Yori API",
    version="1.0.0",
    docs_url=None,
    redoc_url=None
)


@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Yori API</title>
        <style>
            :root {
                --bg1: #0f172a;
                --bg2: #111827;
                --card: rgba(255, 255, 255, 0.08);
                --border: rgba(255, 255, 255, 0.14);
                --text: #e5e7eb;
                --muted: #94a3b8;
                --accent: #38bdf8;
                --accent2: #22c55e;
                --shadow: 0 20px 60px rgba(0, 0, 0, 0.35);
            }

            * {
                box-sizing: border-box;
                margin: 0;
                padding: 0;
            }

            body {
                min-height: 100vh;
                font-family: Arial, Helvetica, sans-serif;
                color: var(--text);
                background:
                    radial-gradient(circle at top, rgba(56, 189, 248, 0.18), transparent 35%),
                    linear-gradient(135deg, var(--bg1), var(--bg2));
                display: flex;
                align-items: center;
                justify-content: center;
                padding: 24px;
            }

            .wrap {
                width: 100%;
                max-width: 980px;
            }

            .hero {
                background: var(--card);
                border: 1px solid var(--border);
                border-radius: 28px;
                box-shadow: var(--shadow);
                backdrop-filter: blur(14px);
                -webkit-backdrop-filter: blur(14px);
                padding: 32px;
                overflow: hidden;
                position: relative;
            }

            .badge {
                display: inline-flex;
                align-items: center;
                gap: 8px;
                padding: 8px 14px;
                border-radius: 999px;
                background: rgba(56, 189, 248, 0.14);
                border: 1px solid rgba(56, 189, 248, 0.22);
                color: #7dd3fc;
                font-size: 14px;
                margin-bottom: 18px;
            }

            h1 {
                font-size: clamp(2rem, 6vw, 4rem);
                line-height: 1.05;
                margin-bottom: 14px;
            }

            .subtitle {
                font-size: 1.05rem;
                color: var(--muted);
                max-width: 760px;
                line-height: 1.7;
                margin-bottom: 28px;
            }

            .grid {
                display: grid;
                grid-template-columns: 1.2fr 0.8fr;
                gap: 20px;
                margin-top: 24px;
            }

            .panel {
                background: rgba(15, 23, 42, 0.48);
                border: 1px solid var(--border);
                border-radius: 22px;
                padding: 22px;
            }

            .panel h2 {
                font-size: 1.05rem;
                margin-bottom: 14px;
                color: #f8fafc;
            }

            .endpoint-list {
                display: grid;
                grid-template-columns: repeat(2, minmax(0, 1fr));
                gap: 10px;
            }

            .endpoint {
                padding: 12px 14px;
                border-radius: 14px;
                background: rgba(255, 255, 255, 0.05);
                border: 1px solid rgba(255, 255, 255, 0.08);
                color: #dbeafe;
                font-size: 14px;
                word-break: break-word;
            }

            .actions {
                display: flex;
                flex-wrap: wrap;
                gap: 12px;
                margin-top: 24px;
            }

            .btn {
                appearance: none;
                border: none;
                cursor: pointer;
                text-decoration: none;
                display: inline-flex;
                align-items: center;
                justify-content: center;
                gap: 10px;
                padding: 14px 18px;
                border-radius: 14px;
                font-weight: 700;
                transition: transform 0.2s ease, box-shadow 0.2s ease, opacity 0.2s ease;
                user-select: none;
            }

            .btn:hover {
                transform: translateY(-2px);
                box-shadow: 0 12px 28px rgba(0, 0, 0, 0.25);
            }

            .btn-primary {
                background: linear-gradient(135deg, #38bdf8, #0ea5e9);
                color: #fff;
            }

            .btn-secondary {
                background: linear-gradient(135deg, #22c55e, #16a34a);
                color: #fff;
            }

            .meta {
                margin-top: 18px;
                color: var(--muted);
                font-size: 14px;
                line-height: 1.7;
            }

            .footer {
                margin-top: 18px;
                color: rgba(229, 231, 235, 0.7);
                font-size: 13px;
            }

            @media (max-width: 820px) {
                .grid {
                    grid-template-columns: 1fr;
                }

                .endpoint-list {
                    grid-template-columns: 1fr;
                }

                .hero {
                    padding: 24px;
                }
            }
        </style>
    </head>
    <body>
        <main class="wrap">
            <section class="hero">
                <div class="badge">⚡ Yori API Online</div>
                <h1>Yori API</h1>
                <p class="subtitle">
                    AI, downloader, image generation, cartoonizer, pixel art aur Hindi TTS ke liye ek clean public API.
                    FastAPI pe built, Render pe live, aur Telegram bots ke liye ready.
                </p>

                <div class="actions">
                    <button class="btn btn-primary" onclick="window.location.href='/docs'">
                        🚀 Getting Started
                    </button>
                    <button class="btn btn-secondary" onclick="window.location.href='https://t.me/yorichiiprime'">
                        👨‍💻 Developer
                    </button>
                </div>

                <div class="grid">
                    <div class="panel">
                        <h2>Available Endpoints</h2>
                        <div class="endpoint-list">
                            <div class="endpoint">/ai/code</div>
                            <div class="endpoint">/ai/anime</div>
                            <div class="endpoint">/ai/pixel</div>
                            <div class="endpoint">/ai/cartoon</div>
                            <div class="endpoint">/tools/download</div>
                            <div class="endpoint">/tts/hindi</div>
                        </div>

                        <div class="meta">
                            OpenAPI schema: <strong>/openapi.json</strong>
                        </div>
                    </div>

                    <div class="panel">
                        <h2>Quick Info</h2>
                        <div class="meta">
                            <strong>Status:</strong> Online<br />
                            <strong>Version:</strong> 1.0.0<br />
                            <strong>Base URL:</strong> yori-api.onrender.com
                        </div>

                        <div class="footer">
                            Built for bots, tools, and fast integrations.
                        </div>
                    </div>
                </div>
            </section>
        </main>
    </body>
    </html>
    """


@app.get("/docs", response_class=HTMLResponse)
def docs():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Yori API Docs</title>
        <style>
            :root {
                --bg1: #07111f;
                --bg2: #0b1220;
                --card: rgba(255, 255, 255, 0.06);
                --border: rgba(255, 255, 255, 0.12);
                --text: #e5e7eb;
                --muted: #94a3b8;
                --accent: #38bdf8;
                --accent2: #22c55e;
                --accent3: #a78bfa;
                --shadow: 0 20px 60px rgba(0, 0, 0, 0.35);
            }

            * { box-sizing: border-box; margin: 0; padding: 0; }

            body {
                min-height: 100vh;
                font-family: Arial, Helvetica, sans-serif;
                color: var(--text);
                background:
                    radial-gradient(circle at top left, rgba(56, 189, 248, 0.15), transparent 28%),
                    radial-gradient(circle at top right, rgba(167, 139, 250, 0.15), transparent 24%),
                    linear-gradient(135deg, var(--bg1), var(--bg2));
                padding: 28px;
            }

            .wrap {
                max-width: 1200px;
                margin: 0 auto;
            }

            .hero {
                background: var(--card);
                border: 1px solid var(--border);
                border-radius: 28px;
                box-shadow: var(--shadow);
                backdrop-filter: blur(14px);
                -webkit-backdrop-filter: blur(14px);
                padding: 30px;
                margin-bottom: 20px;
            }

            .topline {
                display: flex;
                flex-wrap: wrap;
                gap: 12px;
                justify-content: space-between;
                align-items: flex-start;
            }

            .badge {
                display: inline-flex;
                align-items: center;
                gap: 8px;
                padding: 8px 14px;
                border-radius: 999px;
                background: rgba(56, 189, 248, 0.14);
                border: 1px solid rgba(56, 189, 248, 0.22);
                color: #7dd3fc;
                font-size: 14px;
                margin-bottom: 14px;
            }

            h1 {
                font-size: clamp(2rem, 5vw, 3.4rem);
                line-height: 1.05;
                margin-bottom: 12px;
            }

            .subtitle {
                color: var(--muted);
                line-height: 1.75;
                max-width: 820px;
                font-size: 1.02rem;
            }

            .actions {
                display: flex;
                flex-wrap: wrap;
                gap: 12px;
                margin-top: 22px;
            }

            .btn {
                display: inline-flex;
                align-items: center;
                justify-content: center;
                gap: 10px;
                padding: 13px 18px;
                border-radius: 14px;
                border: none;
                cursor: pointer;
                text-decoration: none;
                font-weight: 700;
                transition: transform 0.2s ease, box-shadow 0.2s ease;
            }

            .btn:hover {
                transform: translateY(-2px);
                box-shadow: 0 12px 28px rgba(0, 0, 0, 0.24);
            }

            .btn-primary {
                background: linear-gradient(135deg, #38bdf8, #0ea5e9);
                color: white;
            }

            .btn-success {
                background: linear-gradient(135deg, #22c55e, #16a34a);
                color: white;
            }

            .btn-dark {
                background: linear-gradient(135deg, #334155, #1f2937);
                color: white;
            }

            .stats {
                display: grid;
                grid-template-columns: repeat(4, minmax(0, 1fr));
                gap: 14px;
                margin-top: 22px;
            }

            .stat {
                padding: 16px;
                border-radius: 18px;
                background: rgba(255,255,255,0.05);
                border: 1px solid rgba(255,255,255,0.08);
            }

            .stat .k {
                color: var(--muted);
                font-size: 13px;
                margin-bottom: 8px;
            }

            .stat .v {
                font-size: 1.15rem;
                font-weight: 800;
            }

            .section {
                margin-top: 18px;
                background: var(--card);
                border: 1px solid var(--border);
                border-radius: 24px;
                box-shadow: var(--shadow);
                padding: 22px;
            }

            .section h2 {
                margin-bottom: 12px;
                font-size: 1.2rem;
            }

            .cards {
                display: grid;
                grid-template-columns: repeat(2, minmax(0, 1fr));
                gap: 14px;
                margin-top: 16px;
            }

            .card {
                padding: 18px;
                border-radius: 18px;
                background: rgba(255,255,255,0.05);
                border: 1px solid rgba(255,255,255,0.08);
            }

            .method {
                display: inline-flex;
                align-items: center;
                justify-content: center;
                padding: 5px 10px;
                border-radius: 999px;
                font-size: 12px;
                font-weight: 800;
                margin-bottom: 10px;
                background: rgba(56, 189, 248, 0.16);
                color: #7dd3fc;
                letter-spacing: 0.04em;
            }

            .path {
                font-size: 1.04rem;
                font-weight: 800;
                margin-bottom: 8px;
            }

            .desc {
                color: var(--muted);
                line-height: 1.65;
                font-size: 14px;
            }

            .snippet {
                margin-top: 14px;
                padding: 14px;
                border-radius: 16px;
                background: #020617;
                border: 1px solid rgba(255,255,255,0.08);
                overflow-x: auto;
                color: #cbd5e1;
                font-size: 13px;
                line-height: 1.7;
            }

            .footer {
                margin-top: 16px;
                color: rgba(229,231,235,0.7);
                font-size: 13px;
            }

            @media (max-width: 900px) {
                .stats,
                .cards {
                    grid-template-columns: 1fr;
                }

                body {
                    padding: 16px;
                }

                .hero {
                    padding: 22px;
                }
            }
        </style>
    </head>
    <body>
        <div class="wrap">
            <section class="hero">
                <div class="badge">📚 Yori API / Docs</div>
                <div class="topline">
                    <div>
                        <h1>Getting Started</h1>
                        <p class="subtitle">
                            This page is the clean entry point for Yori API. Use it to check available routes,
                            open the schema, or jump straight into the interactive reference.
                        </p>
                    </div>
                </div>

                <div class="actions">
                    <a class="btn btn-primary" href="/redoc">Open Interactive Reference</a>
                    <a class="btn btn-success" href="/openapi.json">View OpenAPI JSON</a>
                    <a class="btn btn-dark" href="/">Back to Home</a>
                </div>

                <div class="stats">
                    <div class="stat">
                        <div class="k">Status</div>
                        <div class="v">Online</div>
                    </div>
                    <div class="stat">
                        <div class="k">Version</div>
                        <div class="v">1.0.0</div>
                    </div>
                    <div class="stat">
                        <div class="k">Base URL</div>
                        <div class="v">yori-api.onrender.com</div>
                    </div>
                    <div class="stat">
                        <div class="k">Routes</div>
                        <div class="v">6</div>
                    </div>
                </div>
            </section>

            <section class="section">
                <h2>Quick Start</h2>
                <div class="cards">
                    <div class="card">
                        <div class="method">STEP 1</div>
                        <div class="path">Open the base URL</div>
                        <div class="desc">
                            Visit the home page to see the product overview and jump to the docs page.
                        </div>
                        <div class="snippet">GET https://yori-api.onrender.com/</div>
                    </div>

                    <div class="card">
                        <div class="method">STEP 2</div>
                        <div class="path">Test an endpoint</div>
                        <div class="desc">
                            Start with the coding API or any image endpoint to confirm everything is working.
                        </div>
                        <div class="snippet">GET /ai/code?prompt=hello</div>
                    </div>

                    <div class="card">
                        <div class="method">STEP 3</div>
                        <div class="path">Use in Telegram bot</div>
                        <div class="desc">
                            Connect the routes to your bot commands and forward user input to the API.
                        </div>
                        <div class="snippet">/code  /anime  /pixel  /cartoon  /download  /tts</div>
                    </div>

                    <div class="card">
                        <div class="method">TIP</div>
                        <div class="path">Use the reference</div>
                        <div class="desc">
                            Open the interactive reference for request/response testing and schema browsing.
                        </div>
                        <div class="snippet">Open /redoc or /openapi.json</div>
                    </div>
                </div>
            </section>

            <section class="section">
                <h2>Endpoint Overview</h2>
                <div class="cards">
                    <div class="card">
                        <div class="method">GET</div>
                        <div class="path">/ai/code</div>
                        <div class="desc">Coding AI wrapper with prompt and history support.</div>
                    </div>
                    <div class="card">
                        <div class="method">GET</div>
                        <div class="path">/ai/anime</div>
                        <div class="desc">Anime image generator that returns direct image bytes.</div>
                    </div>
                    <div class="card">
                        <div class="method">GET</div>
                        <div class="path">/ai/pixel</div>
                        <div class="desc">Pixel art generator that returns direct image bytes.</div>
                    </div>
                    <div class="card">
                        <div class="method">GET</div>
                        <div class="path">/ai/cartoon</div>
                        <div class="desc">Image-to-anime/cartoon conversion with anime image URL in JSON.</div>
                    </div>
                    <div class="card">
                        <div class="method">GET</div>
                        <div class="path">/tools/download</div>
                        <div class="desc">Universal downloader for supported platforms like Pinterest and YouTube.</div>
                    </div>
                    <div class="card">
                        <div class="method">GET</div>
                        <div class="path">/tts/hindi</div>
                        <div class="desc">Hindi text-to-speech that returns direct audio.</div>
                    </div>
                </div>

                <div class="footer">
                    The live interactive reference is available at <strong>/redoc</strong>.
                </div>
            </section>
        </div>
    </body>
    </html>
    """


@app.get("/redoc", response_class=HTMLResponse)
def redoc():
    return get_redoc_html(
        openapi_url="/openapi.json",
        title="Yori API Reference"
    )


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


@app.get("/tts/hindi")
def tts_hindi(text: str):
    try:
        r = requests.get(
            "https://apis.prexzyvilla.site/tts/tts-hi",
            params={"text": text},
            timeout=120
        )
        r.raise_for_status()

        return Response(
            content=r.content,
            media_type="audio/mpeg"
        )

    except requests.RequestException as e:
        raise HTTPException(status_code=502, detail=f"Upstream error: {str(e)}")