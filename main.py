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


@app.get("/health")
def health_check():
    """
    Lightweight health-check endpoint.
    Use this URL in UptimeRobot / cron monitors to check if the API is alive.
    It does not call any upstream API, so it responds fast and avoids extra load.
    """
    return {
        "status": True,
        "message": "Yori API is healthy",
        "service": "Yori API",
        "version": "1.0.0"
    }


@app.get("/healthz")
def healthz():
    """Alias for /health."""
    return health_check()


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
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover" />
<title>Yori API — Documentation</title>
<style>
:root{
  --bg:#070d17;--bg2:#0a1220;--surface:#0d1525;--card:#111a2c;
  --border:rgba(255,255,255,.10);--border2:rgba(255,255,255,.16);
  --text:#e8edf6;--muted:#93a1b6;--accent:#38bdf8;--green:#22c55e;
  --red:#ef4444;--shadow:0 18px 50px rgba(0,0,0,.28);
  --mono:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono",monospace;
  --sans:Inter,system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Arial,sans-serif;
}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{
  min-height:100vh;font-family:var(--sans);color:var(--text);background:
  radial-gradient(circle at 15% 0%,rgba(56,189,248,.08),transparent 35%),
  radial-gradient(circle at 85% 20%,rgba(34,197,94,.05),transparent 30%),
  linear-gradient(180deg,var(--bg),#080d19 65%,#070b14);
  overflow-x:hidden;
}
a{color:inherit}.topbar{position:sticky;top:0;z-index:10;background:rgba(7,13,23,.88);backdrop-filter:blur(16px);border-bottom:1px solid var(--border)}
.topbar-inner{max-width:1120px;margin:auto;padding:16px 18px;display:flex;align-items:center;gap:14px}
.brand{display:flex;align-items:center;gap:10px;font-weight:850;font-size:1.08rem;white-space:nowrap}.dot{width:10px;height:10px;border-radius:999px;background:var(--green);box-shadow:0 0 18px rgba(34,197,94,.8)}
.nav{margin-left:auto;display:flex;gap:8px}.nav a{text-decoration:none;color:var(--muted);font-size:14px;font-weight:700;padding:9px 12px;border-radius:999px}.nav a:hover{background:rgba(255,255,255,.06);color:var(--text)}
.wrap{max-width:1120px;margin:auto;padding:24px 18px 56px}.base-card,.stat,.endpoint{background:rgba(17,26,44,.78);border:1px solid var(--border);border-radius:22px;box-shadow:var(--shadow)}
.base-card{display:grid;grid-template-columns:auto minmax(0,1fr) auto;gap:16px;align-items:center;padding:22px;margin-bottom:18px}.label{color:var(--muted);font-size:12px;font-weight:850;letter-spacing:.08em;text-transform:uppercase;white-space:nowrap}.base-url{font-family:var(--mono);font-size:clamp(.86rem,2.7vw,1rem);line-height:1.55;background:rgba(0,0,0,.28);border:1px solid rgba(255,255,255,.08);border-radius:15px;padding:13px 15px;overflow-wrap:anywhere;word-break:break-word;color:#dbe5f4}.copy{border:1px solid var(--border2);background:rgba(255,255,255,.04);color:var(--text);border-radius:14px;padding:12px 15px;font-weight:800;cursor:pointer;white-space:nowrap}.copy:hover{background:rgba(255,255,255,.08)}
.stats{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px;margin:18px 0 22px}.stat{display:flex;gap:14px;align-items:center;padding:18px}.icon{font-size:2rem}.stat-k{color:var(--muted);font-size:12px;font-weight:850;text-transform:uppercase;letter-spacing:.08em}.stat-v{font-size:1.1rem;font-weight:850;margin-top:2px}
.section-title{font-size:1.35rem;margin:26px 0 14px;letter-spacing:-.02em}.endpoint{overflow:hidden;margin-bottom:18px}.ep-head{display:flex;align-items:flex-start;gap:12px;padding:20px 22px;border-bottom:1px solid rgba(255,255,255,.06)}.method{font-family:var(--mono);font-size:12px;font-weight:900;color:#06101c;background:linear-gradient(135deg,#7dd3fc,#38bdf8);padding:7px 11px;border-radius:999px}.path{font-family:var(--mono);font-weight:850;font-size:1.05rem;overflow-wrap:anywhere}.desc{margin-left:auto;max-width:430px;color:var(--muted);font-size:14px;line-height:1.55;text-align:right}.ep-body{padding:20px 22px}.sub{font-size:12px;font-weight:900;text-transform:uppercase;letter-spacing:.08em;color:var(--muted);margin-bottom:10px}
.table-wrap{width:100%;overflow-x:auto;border:1px solid rgba(255,255,255,.07);border-radius:14px;margin-bottom:16px}table{width:100%;border-collapse:collapse;min-width:620px}th,td{text-align:left;padding:11px 13px;border-bottom:1px solid rgba(255,255,255,.06);font-size:13px;vertical-align:top}th{color:var(--muted);font-size:11px;text-transform:uppercase;letter-spacing:.07em;background:rgba(255,255,255,.025)}td:first-child{font-family:var(--mono);font-weight:800}.req{color:#f87171;font-weight:850}.opt{color:var(--muted)}
.code-tabs{display:flex;gap:6px;align-items:center;background:rgba(0,0,0,.22);border:1px solid rgba(255,255,255,.08);border-bottom:0;border-radius:14px 14px 0 0;padding:6px;overflow-x:auto}.tab{border:0;border-radius:10px;background:transparent;color:var(--muted);padding:9px 13px;font-weight:800;cursor:pointer}.tab.active{background:var(--accent);color:#06101c}.copy-code{margin-left:auto;border:1px solid rgba(255,255,255,.12);background:transparent;color:var(--muted);border-radius:10px;padding:8px 12px;font-weight:800;cursor:pointer;white-space:nowrap}.codebox{background:#020617;border:1px solid rgba(255,255,255,.08);border-radius:0 0 14px 14px;padding:15px;overflow:auto;max-height:330px;margin-bottom:14px}pre{font-family:var(--mono);font-size:12.5px;line-height:1.7;white-space:pre;color:#d4deee}.panel{display:none}.panel.active{display:block}.try{border:1px solid var(--border2);background:rgba(56,189,248,.06);color:var(--text);border-radius:13px;padding:11px 16px;font-weight:900;cursor:pointer}.try:hover{border-color:rgba(56,189,248,.38);color:#7dd3fc}.try-panel{display:none;margin-top:14px;background:rgba(0,0,0,.20);border:1px solid rgba(255,255,255,.08);border-radius:16px;padding:16px}.try-panel.open{display:block}.field{margin-bottom:12px}.field label{display:block;color:var(--muted);font-size:12px;text-transform:uppercase;letter-spacing:.07em;font-weight:850;margin-bottom:6px}input,textarea{width:100%;background:rgba(0,0,0,.35);border:1px solid rgba(255,255,255,.12);border-radius:12px;color:var(--text);padding:12px;font-family:var(--mono);outline:0}textarea{min-height:70px;resize:vertical}input:focus,textarea:focus{border-color:var(--accent)}.send{background:linear-gradient(135deg,#38bdf8,#0ea5e9);color:#00111f;border:0;border-radius:12px;padding:12px 18px;font-weight:950;cursor:pointer}.response{display:none;margin-top:14px}.response-box{background:#020617;border:1px solid rgba(255,255,255,.08);border-radius:14px;padding:14px;min-height:48px;max-height:360px;overflow:auto;font-family:var(--mono);font-size:13px;line-height:1.65;white-space:pre-wrap;overflow-wrap:anywhere}.response-box img{max-width:100%;border-radius:12px}.response-box audio{width:100%}.footer{text-align:center;color:var(--muted);border-top:1px solid var(--border);padding:25px 18px;font-size:13px}
@media(max-width:760px){.topbar-inner{padding:15px 14px}.brand{font-size:1rem}.nav a{font-size:13px;padding:8px 9px}.wrap{padding:18px 14px 42px}.base-card{grid-template-columns:1fr;gap:10px;padding:18px}.copy{width:100%}.stats{grid-template-columns:1fr}.stat{padding:17px}.ep-head{display:block;padding:18px}.method{display:inline-block;margin-bottom:10px}.path{display:block;font-size:1rem;margin-bottom:8px}.desc{margin:0;max-width:none;text-align:left}.ep-body{padding:16px}.code-tabs{gap:4px}.tab{padding:8px 11px}.copy-code{margin-left:0}.section-title{font-size:1.18rem}pre{font-size:12px}.footer{font-size:12px}}
</style>
</head>
<body>
<nav class="topbar"><div class="topbar-inner"><div class="brand"><span class="dot"></span>Yori API Docs</div><div class="nav"><a href="/">Home</a><a href="/openapi.json">OpenAPI JSON</a></div></div></nav>
<main class="wrap">
  <section class="base-card"><div class="label">Base URL</div><code class="base-url" id="baseUrl">https://yori-api.onrender.com</code><button class="copy" onclick="copyText('https://yori-api.onrender.com',this)">📋 Copy</button></section>
  <section class="stats"><div class="stat"><div class="icon">🚀</div><div><div class="stat-k">Status</div><div class="stat-v">Online</div></div></div><div class="stat"><div class="icon">📦</div><div><div class="stat-k">Version</div><div class="stat-v">1.0.0</div></div></div><div class="stat"><div class="icon">🔗</div><div><div class="stat-k">Endpoints</div><div class="stat-v">6 Available</div></div></div></section>
  <h1 class="section-title">Available Endpoints</h1>
  <div id="endpointList">
    <section class="endpoint" id="code"><div class="ep-head"><span class="method">GET</span><div class="path">/ai/code</div><div class="desc">AI coding assistant. Send a prompt and optional conversation history.</div></div><div class="ep-body"><div class="sub">Parameters</div><div class="table-wrap"><table><tr><th>Name</th><th>Type</th><th>Required</th><th>Description</th></tr><tr><td>prompt</td><td>string</td><td class="req">Yes</td><td>Your coding question or instruction.</td></tr><tr><td>history</td><td>string</td><td class="opt">No</td><td>Previous conversation context.</td></tr></table></div><div class="code-tabs"><button class="tab active" onclick="showTab('code','python',this)">Python</button><button class="tab" onclick="showTab('code','node',this)">Node.js</button><button class="tab" onclick="showTab('code','curl',this)">cURL</button><button class="copy-code" onclick="copyActive('code',this)">Copy</button></div><div class="codebox"><div class="panel active" data-lang="python"><pre>import requests

url = "https://yori-api.onrender.com/ai/code"
params = {"prompt": "Write a Python function to sort a list", "history": ""}

resp = requests.get(url, params=params)
print(resp.json()["response"])</pre></div><div class="panel" data-lang="node"><pre>const axios = require("axios");

axios.get("https://yori-api.onrender.com/ai/code", {
  params: { prompt: "Write a Python function to sort a list", history: "" }
}).then(res => console.log(res.data.response));</pre></div><div class="panel" data-lang="curl"><pre>curl "https://yori-api.onrender.com/ai/code?prompt=Write+a+Python+function+to+sort+a+list"</pre></div></div><button class="try" onclick="toggleTry('code')">⚡ Try Now</button><div class="try-panel" id="try-code"><div class="field"><label>prompt *</label><input id="inp-code-prompt" placeholder="Your coding prompt"></div><div class="field"><label>history optional</label><textarea id="inp-code-history" placeholder="Previous conversation"></textarea></div><button class="send" onclick="sendReq('code')">Send Request</button><div class="response" id="resp-code"><div class="sub">Response</div><div class="response-box"></div></div></div></div></section>
    <section class="endpoint" id="anime"><div class="ep-head"><span class="method">GET</span><div class="path">/ai/anime</div><div class="desc">Generate anime-style artwork from a text prompt. Returns PNG image.</div></div><div class="ep-body"><div class="sub">Parameters</div><div class="table-wrap"><table><tr><th>Name</th><th>Type</th><th>Required</th><th>Description</th></tr><tr><td>prompt</td><td>string</td><td class="req">Yes</td><td>Describe the anime scene.</td></tr><tr><td>negative_prompt</td><td>string</td><td class="opt">No</td><td>Things to avoid.</td></tr></table></div><div class="code-tabs"><button class="tab active" onclick="showTab('anime','python',this)">Python</button><button class="tab" onclick="showTab('anime','node',this)">Node.js</button><button class="tab" onclick="showTab('anime','curl',this)">cURL</button><button class="copy-code" onclick="copyActive('anime',this)">Copy</button></div><div class="codebox"><div class="panel active" data-lang="python"><pre>import requests

resp = requests.get("https://yori-api.onrender.com/ai/anime", params={"prompt":"a beautiful sunset over Tokyo, anime style"})
open("anime.png", "wb").write(resp.content)</pre></div><div class="panel" data-lang="node"><pre>const axios = require("axios");
const fs = require("fs");

axios.get("https://yori-api.onrender.com/ai/anime", { params:{prompt:"a beautiful sunset over Tokyo, anime style"}, responseType:"arraybuffer" })
.then(res => fs.writeFileSync("anime.png", res.data));</pre></div><div class="panel" data-lang="curl"><pre>curl "https://yori-api.onrender.com/ai/anime?prompt=a+beautiful+sunset+over+Tokyo" -o anime.png</pre></div></div><button class="try" onclick="toggleTry('anime')">⚡ Try Now</button><div class="try-panel" id="try-anime"><div class="field"><label>prompt *</label><input id="inp-anime-prompt" placeholder="Anime prompt"></div><div class="field"><label>negative_prompt optional</label><textarea id="inp-anime-negative_prompt"></textarea></div><button class="send" onclick="sendReq('anime')">Send Request</button><div class="response" id="resp-anime"><div class="sub">Response</div><div class="response-box"></div></div></div></div></section>
    <section class="endpoint" id="pixel"><div class="ep-head"><span class="method">GET</span><div class="path">/ai/pixel</div><div class="desc">Create retro pixel-art images from text descriptions.</div></div><div class="ep-body"><div class="sub">Parameters</div><div class="table-wrap"><table><tr><th>Name</th><th>Type</th><th>Required</th><th>Description</th></tr><tr><td>prompt</td><td>string</td><td class="req">Yes</td><td>Describe the pixel art.</td></tr><tr><td>negative_prompt</td><td>string</td><td class="opt">No</td><td>Things to avoid.</td></tr></table></div><div class="code-tabs"><button class="tab active" onclick="showTab('pixel','python',this)">Python</button><button class="tab" onclick="showTab('pixel','node',this)">Node.js</button><button class="tab" onclick="showTab('pixel','curl',this)">cURL</button><button class="copy-code" onclick="copyActive('pixel',this)">Copy</button></div><div class="codebox"><div class="panel active" data-lang="python"><pre>import requests

resp = requests.get("https://yori-api.onrender.com/ai/pixel", params={"prompt":"a cute cat in 16-bit pixel art style"})
open("pixel.png", "wb").write(resp.content)</pre></div><div class="panel" data-lang="node"><pre>const axios = require("axios");
const fs = require("fs");

axios.get("https://yori-api.onrender.com/ai/pixel", { params:{prompt:"a cute cat in 16-bit pixel art style"}, responseType:"arraybuffer" })
.then(res => fs.writeFileSync("pixel.png", res.data));</pre></div><div class="panel" data-lang="curl"><pre>curl "https://yori-api.onrender.com/ai/pixel?prompt=a+cute+cat+in+16-bit+pixel+art+style" -o pixel.png</pre></div></div><button class="try" onclick="toggleTry('pixel')">⚡ Try Now</button><div class="try-panel" id="try-pixel"><div class="field"><label>prompt *</label><input id="inp-pixel-prompt" placeholder="Pixel art prompt"></div><div class="field"><label>negative_prompt optional</label><textarea id="inp-pixel-negative_prompt"></textarea></div><button class="send" onclick="sendReq('pixel')">Send Request</button><div class="response" id="resp-pixel"><div class="sub">Response</div><div class="response-box"></div></div></div></div></section>
    <section class="endpoint" id="cartoon"><div class="ep-head"><span class="method">GET</span><div class="path">/ai/cartoon</div><div class="desc">Transform a photo URL into a cartoon/anime-style image.</div></div><div class="ep-body"><div class="sub">Parameters</div><div class="table-wrap"><table><tr><th>Name</th><th>Type</th><th>Required</th><th>Description</th></tr><tr><td>imageurl</td><td>string</td><td class="req">Yes</td><td>URL of the image to cartoonize.</td></tr></table></div><div class="code-tabs"><button class="tab active" onclick="showTab('cartoon','python',this)">Python</button><button class="tab" onclick="showTab('cartoon','node',this)">Node.js</button><button class="tab" onclick="showTab('cartoon','curl',this)">cURL</button><button class="copy-code" onclick="copyActive('cartoon',this)">Copy</button></div><div class="codebox"><div class="panel active" data-lang="python"><pre>import requests

resp = requests.get("https://yori-api.onrender.com/ai/cartoon", params={"imageurl":"https://example.com/photo.jpg"})
print(resp.json()["anime_image"])</pre></div><div class="panel" data-lang="node"><pre>const axios = require("axios");

axios.get("https://yori-api.onrender.com/ai/cartoon", { params:{imageurl:"https://example.com/photo.jpg"} })
.then(res => console.log(res.data.anime_image));</pre></div><div class="panel" data-lang="curl"><pre>curl "https://yori-api.onrender.com/ai/cartoon?imageurl=https://example.com/photo.jpg"</pre></div></div><button class="try" onclick="toggleTry('cartoon')">⚡ Try Now</button><div class="try-panel" id="try-cartoon"><div class="field"><label>imageurl *</label><input id="inp-cartoon-imageurl" placeholder="https://example.com/photo.jpg"></div><button class="send" onclick="sendReq('cartoon')">Send Request</button><div class="response" id="resp-cartoon"><div class="sub">Response</div><div class="response-box"></div></div></div></div></section>
    <section class="endpoint" id="download"><div class="ep-head"><span class="method">GET</span><div class="path">/tools/download</div><div class="desc">Universal media downloader for supported public media URLs.</div></div><div class="ep-body"><div class="sub">Parameters</div><div class="table-wrap"><table><tr><th>Name</th><th>Type</th><th>Required</th><th>Description</th></tr><tr><td>url</td><td>string</td><td class="req">Yes</td><td>Media page URL.</td></tr></table></div><div class="code-tabs"><button class="tab active" onclick="showTab('download','python',this)">Python</button><button class="tab" onclick="showTab('download','node',this)">Node.js</button><button class="tab" onclick="showTab('download','curl',this)">cURL</button><button class="copy-code" onclick="copyActive('download',this)">Copy</button></div><div class="codebox"><div class="panel active" data-lang="python"><pre>import requests

resp = requests.get("https://yori-api.onrender.com/tools/download", params={"url":"https://youtube.com/watch?v=dQw4w9WgXcQ"})
print(resp.json())</pre></div><div class="panel" data-lang="node"><pre>const axios = require("axios");

axios.get("https://yori-api.onrender.com/tools/download", { params:{url:"https://youtube.com/watch?v=dQw4w9WgXcQ"} })
.then(res => console.log(res.data));</pre></div><div class="panel" data-lang="curl"><pre>curl "https://yori-api.onrender.com/tools/download?url=https://youtube.com/watch?v=dQw4w9WgXcQ"</pre></div></div><button class="try" onclick="toggleTry('download')">⚡ Try Now</button><div class="try-panel" id="try-download"><div class="field"><label>url *</label><input id="inp-download-url" placeholder="https://..."></div><button class="send" onclick="sendReq('download')">Send Request</button><div class="response" id="resp-download"><div class="sub">Response</div><div class="response-box"></div></div></div></div></section>
    <section class="endpoint" id="tts"><div class="ep-head"><span class="method">GET</span><div class="path">/tts/hindi</div><div class="desc">Convert Hindi text into natural-sounding speech. Returns MP3 audio.</div></div><div class="ep-body"><div class="sub">Parameters</div><div class="table-wrap"><table><tr><th>Name</th><th>Type</th><th>Required</th><th>Description</th></tr><tr><td>text</td><td>string</td><td class="req">Yes</td><td>Hindi text to convert to speech.</td></tr></table></div><div class="code-tabs"><button class="tab active" onclick="showTab('tts','python',this)">Python</button><button class="tab" onclick="showTab('tts','node',this)">Node.js</button><button class="tab" onclick="showTab('tts','curl',this)">cURL</button><button class="copy-code" onclick="copyActive('tts',this)">Copy</button></div><div class="codebox"><div class="panel active" data-lang="python"><pre>import requests

resp = requests.get("https://yori-api.onrender.com/tts/hindi", params={"text":"नमस्ते दुनिया"})
open("speech.mp3", "wb").write(resp.content)</pre></div><div class="panel" data-lang="node"><pre>const axios = require("axios");
const fs = require("fs");

axios.get("https://yori-api.onrender.com/tts/hindi", { params:{text:"नमस्ते दुनिया"}, responseType:"arraybuffer" })
.then(res => fs.writeFileSync("speech.mp3", res.data));</pre></div><div class="panel" data-lang="curl"><pre>curl "https://yori-api.onrender.com/tts/hindi?text=%E0%A4%A8%E0%A4%AE%E0%A4%B8%E0%A5%8D%E0%A4%A4%E0%A5%87" -o speech.mp3</pre></div></div><button class="try" onclick="toggleTry('tts')">⚡ Try Now</button><div class="try-panel" id="try-tts"><div class="field"><label>text *</label><textarea id="inp-tts-text" placeholder="नमस्ते दुनिया"></textarea></div><button class="send" onclick="sendReq('tts')">Send Request</button><div class="response" id="resp-tts"><div class="sub">Response</div><div class="response-box"></div></div></div></div></section>
  </div>
</main>
<footer class="footer">Yori API © 2026 — Built for speed, bots, and fast integrations.</footer>
<script>
const BASE = "https://yori-api.onrender.com";
const config = {
  code:{path:"/ai/code", type:"json", fields:["prompt","history"]}, anime:{path:"/ai/anime", type:"image", fields:["prompt","negative_prompt"]}, pixel:{path:"/ai/pixel", type:"image", fields:["prompt","negative_prompt"]}, cartoon:{path:"/ai/cartoon", type:"json", fields:["imageurl"]}, download:{path:"/tools/download", type:"json", fields:["url"]}, tts:{path:"/tts/hindi", type:"audio", fields:["text"]}
};
function copyText(text,btn){navigator.clipboard&&navigator.clipboard.writeText?navigator.clipboard.writeText(text):fallbackCopy(text);let old=btn.textContent;btn.textContent="✓ Copied";setTimeout(()=>btn.textContent=old,1600)}
function fallbackCopy(text){let t=document.createElement('textarea');t.value=text;document.body.appendChild(t);t.select();document.execCommand('copy');t.remove()}
function showTab(id,lang,btn){let card=document.getElementById(id);card.querySelectorAll('.panel').forEach(p=>p.classList.toggle('active',p.dataset.lang===lang));btn.parentElement.querySelectorAll('.tab').forEach(b=>b.classList.remove('active'));btn.classList.add('active')}
function copyActive(id,btn){let panel=document.querySelector('#'+id+' .panel.active pre');copyText(panel.innerText,btn)}
function toggleTry(id){document.getElementById('try-'+id).classList.toggle('open')}
function sendReq(id){let c=config[id], params=new URLSearchParams(), missing=false;c.fields.forEach(f=>{let el=document.getElementById('inp-'+id+'-'+f);let v=(el&&el.value||'').trim();if((f==='prompt'||f==='imageurl'||f==='url'||f==='text')&&!v){missing=true;if(el)el.style.borderColor='var(--red)'}else if(el){el.style.borderColor=''}if(v)params.append(f,v)});if(missing)return;let url=BASE+c.path+'?'+params.toString();let resp=document.getElementById('resp-'+id), box=resp.querySelector('.response-box');resp.style.display='block';box.textContent='Loading...';if(c.type==='image'){box.innerHTML='';let img=new Image();img.onload=()=>{box.innerHTML='';box.appendChild(img)};img.onerror=()=>box.textContent='Failed to load image.';img.src=url}else if(c.type==='audio'){box.innerHTML='';let a=document.createElement('audio');a.controls=true;a.src=url;box.appendChild(a)}else{fetch(url).then(r=>r.json()).then(d=>box.textContent=JSON.stringify(d,null,2)).catch(e=>box.textContent='Request failed: '+e.message)}}
</script>
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