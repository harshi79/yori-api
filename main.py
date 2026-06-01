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
        <title>Yori API — Documentation</title>
        <style>
            :root {
                --bg: #070d17;
                --surface: #0d1525;
                --card: rgba(255,255,255,0.03);
                --border: rgba(255,255,255,0.08);
                --text: #e4e7ec;
                --muted: #8896ab;
                --accent: #38bdf8;
                --accent-glow: rgba(56,189,248,0.18);
                --green: #22c55e;
                --green-glow: rgba(34,197,94,0.16);
                --red: #ef4444;
                --radius: 18px;
                --font-mono: 'JetBrains Mono', 'Fira Code', 'Cascadia Code', 'SF Mono', Consolas, monospace;
            }

            * { box-sizing: border-box; margin: 0; padding: 0; }

            body {
                font-family: 'Inter', system-ui, -apple-system, sans-serif;
                background: var(--bg);
                color: var(--text);
                min-height: 100vh;
                background-image:
                    radial-gradient(ellipse at 20% 0%, rgba(56,189,248,0.06) 0%, transparent 60%),
                    radial-gradient(ellipse at 80% 100%, rgba(167,139,250,0.05) 0%, transparent 60%);
            }

            /* ── HEADER ─────────────────────────── */
            .topbar {
                position: sticky; top: 0; z-index: 50;
                background: rgba(7,13,23,0.82);
                backdrop-filter: blur(18px);
                -webkit-backdrop-filter: blur(18px);
                border-bottom: 1px solid var(--border);
                padding: 0 32px;
            }
            .topbar-inner {
                max-width: 1100px; margin: 0 auto;
                display: flex; align-items: center; flex-wrap: wrap;
                gap: 16px; padding: 18px 0;
            }
            .topbar-brand {
                display: flex; align-items: center; gap: 10px;
                font-weight: 800; font-size: 1.15rem; letter-spacing: -0.01em;
            }
            .topbar-dot { width: 9px; height: 9px; border-radius: 50%; background: var(--green); box-shadow: 0 0 10px var(--green-glow); }
            .topbar-nav { display: flex; gap: 6px; margin-left: auto; }
            .topbar-nav a {
                text-decoration: none; color: var(--muted); font-size: 14px;
                padding: 8px 16px; border-radius: 999px; font-weight: 600;
                transition: all 0.2s;
            }
            .topbar-nav a:hover { color: var(--text); background: rgba(255,255,255,0.06); }

            /* ── BASE URL BAR ──────────────────── */
            .baseurl-section {
                max-width: 1100px; margin: 28px auto 0; padding: 0 32px;
            }
            .baseurl-card {
                background: var(--surface);
                border: 1px solid var(--border);
                border-radius: var(--radius);
                padding: 22px 28px;
                display: flex; align-items: center; flex-wrap: wrap;
                gap: 16px;
                box-shadow: 0 8px 32px rgba(0,0,0,0.25);
            }
            .baseurl-label {
                font-size: 12px; text-transform: uppercase; letter-spacing: 0.08em;
                color: var(--muted); font-weight: 700;
            }
            .baseurl-value {
                flex: 1; min-width: 220px;
                font-family: var(--font-mono); font-size: 0.95rem;
                color: #cbd5e1; background: rgba(0,0,0,0.35);
                padding: 12px 16px; border-radius: 12px; border: 1px solid rgba(255,255,255,0.06);
                word-break: break-all;
            }
            .btn-copy {
                display: inline-flex; align-items: center; gap: 7px;
                padding: 11px 18px; border-radius: 12px; border: 1px solid rgba(255,255,255,0.14);
                background: rgba(255,255,255,0.04); color: var(--text);
                font-size: 13px; font-weight: 600; cursor: pointer;
                transition: all 0.2s; white-space: nowrap;
            }
            .btn-copy:hover { background: rgba(255,255,255,0.1); border-color: rgba(255,255,255,0.25); }
            .btn-copy.copied { background: rgba(34,197,94,0.14); border-color: rgba(34,197,94,0.35); color: var(--green); }

            /* ── MAIN CONTENT ──────────────────── */
            .container { max-width: 1100px; margin: 28px auto 60px; padding: 0 32px; }

            /* ── STATS ROW ─────────────────────── */
            .stats-row {
                display: grid; grid-template-columns: repeat(3, 1fr); gap: 14px; margin-bottom: 28px;
            }
            .stat-pill {
                background: var(--card); border: 1px solid var(--border); border-radius: 16px;
                padding: 16px 20px; display: flex; align-items: center; gap: 12px;
            }
            .stat-icon { font-size: 1.4rem; }
            .stat-info .stat-k { font-size: 11px; text-transform: uppercase; letter-spacing: 0.08em; color: var(--muted); font-weight: 700; }
            .stat-info .stat-v { font-size: 1.1rem; font-weight: 800; }

            /* ── ENDPOINT CARD ─────────────────── */
            .endpoint-card {
                background: var(--surface);
                border: 1px solid var(--border);
                border-radius: var(--radius);
                margin-bottom: 20px;
                overflow: hidden;
                box-shadow: 0 4px 24px rgba(0,0,0,0.2);
                transition: border-color 0.25s;
            }
            .endpoint-card:hover { border-color: rgba(255,255,255,0.16); }

            .ec-header {
                padding: 22px 26px;
                display: flex; align-items: center; flex-wrap: wrap; gap: 14px;
                cursor: default;
            }
            .ec-method {
                padding: 6px 13px; border-radius: 999px; font-size: 12px; font-weight: 800;
                letter-spacing: 0.06em; text-transform: uppercase;
                background: rgba(56,189,248,0.15); color: #7dd3fc;
            }
            .ec-method.post { background: rgba(34,197,94,0.15); color: #4ade80; }
            .ec-path {
                font-family: var(--font-mono); font-size: 1.08rem; font-weight: 700; letter-spacing: -0.01em;
            }
            .ec-desc {
                color: var(--muted); font-size: 14px; line-height: 1.65;
                margin-left: auto; max-width: 340px; text-align: right;
            }

            .ec-body { padding: 0 26px 22px; }

            /* ── PARAM TABLE ───────────────────── */
            .ec-params { margin-bottom: 20px; }
            .ec-params h4 {
                font-size: 12px; text-transform: uppercase; letter-spacing: 0.08em;
                color: var(--muted); font-weight: 700; margin-bottom: 10px;
            }
            .param-table {
                width: 100%; border-collapse: collapse;
                font-size: 13px;
            }
            .param-table th {
                text-align: left; padding: 9px 14px;
                background: rgba(255,255,255,0.02);
                font-size: 11px; text-transform: uppercase; letter-spacing: 0.06em;
                color: var(--muted); font-weight: 700;
                border-bottom: 1px solid var(--border);
            }
            .param-table td {
                padding: 10px 14px; border-bottom: 1px solid rgba(255,255,255,0.04);
                color: var(--text);
            }
            .param-table td:first-child { font-family: var(--font-mono); font-weight: 600; }
            .badge-req { color: var(--red); font-weight: 700; font-size: 12px; }
            .badge-opt { color: var(--muted); font-size: 12px; }

            /* ── CODE TABS ─────────────────────── */
            .code-section { position: relative; }
            .code-tabs {
                display: flex; align-items: center; gap: 4px; margin-bottom: 0;
                background: rgba(0,0,0,0.25); padding: 5px; border-radius: 12px 12px 0 0;
                border: 1px solid var(--border); border-bottom: none;
            }
            .code-tab {
                padding: 9px 16px; border-radius: 9px; border: none; cursor: pointer;
                font-size: 13px; font-weight: 600; background: transparent; color: var(--muted);
                transition: all 0.18s; font-family: inherit;
            }
            .code-tab.active { background: var(--accent); color: #000; }
            .code-tab:hover:not(.active) { color: var(--text); background: rgba(255,255,255,0.06); }
            .code-copy-btn {
                margin-left: auto; margin-right: 4px;
                display: inline-flex; align-items: center; gap: 6px;
                padding: 7px 14px; border-radius: 9px; border: 1px solid rgba(255,255,255,0.1);
                background: transparent; color: var(--muted); font-size: 12px; font-weight: 600;
                cursor: pointer; transition: all 0.2s;
            }
            .code-copy-btn:hover { background: rgba(255,255,255,0.08); color: var(--text); }
            .code-copy-btn.copied { background: rgba(34,197,94,0.12); border-color: rgba(34,197,94,0.3); color: var(--green); }

            .code-block {
                background: #020617; border: 1px solid var(--border); border-top: none;
                border-radius: 0 0 12px 12px; padding: 16px; overflow-x: auto;
                font-family: var(--font-mono); font-size: 13px; line-height: 1.75;
                color: #cbd5e1; position: relative; max-height: 400px; overflow-y: auto;
            }
            .code-block pre { margin: 0; white-space: pre; }
            .code-block .kw { color: #c084fc; }
            .code-block .str { color: #4ade80; }
            .code-block .cmt { color: #64748b; font-style: italic; }
            .code-block .fn { color: #7dd3fc; }
            .code-block .num { color: #fb923c; }
            .code-panel { display: none; }
            .code-panel.active { display: block; }

            /* ── TRY NOW ───────────────────────── */
            .try-toggle {
                display: inline-flex; align-items: center; gap: 8px;
                padding: 11px 20px; border-radius: 12px; border: 1px solid rgba(255,255,255,0.14);
                background: rgba(255,255,255,0.03); color: var(--text);
                font-size: 14px; font-weight: 700; cursor: pointer; margin-top: 16px;
                transition: all 0.2s;
            }
            .try-toggle:hover { background: rgba(56,189,248,0.08); border-color: rgba(56,189,248,0.3); color: var(--accent); }
            .try-toggle.open { background: rgba(56,189,248,0.1); border-color: rgba(56,189,248,0.35); color: var(--accent); }

            .try-panel {
                margin-top: 14px; border-radius: var(--radius); overflow: hidden;
                border: 1px solid var(--border);
                max-height: 0; opacity: 0;
                transition: max-height 0.35s ease, opacity 0.25s ease, margin 0.25s ease;
                pointer-events: none;
            }
            .try-panel.expanded {
                max-height: 800px; opacity: 1; pointer-events: all; margin-top: 16px;
            }
            .try-panel-inner {
                background: rgba(0,0,0,0.28); padding: 22px;
            }
            .try-field {
                margin-bottom: 14px;
            }
            .try-field label {
                display: block; font-size: 12px; text-transform: uppercase;
                letter-spacing: 0.06em; color: var(--muted); font-weight: 700;
                margin-bottom: 6px;
            }
            .try-field input, .try-field textarea {
                width: 100%; padding: 11px 14px; border-radius: 10px;
                border: 1px solid rgba(255,255,255,0.12);
                background: rgba(0,0,0,0.4); color: var(--text);
                font-family: var(--font-mono); font-size: 14px;
                transition: border-color 0.2s; outline: none; resize: vertical;
            }
            .try-field input:focus, .try-field textarea:focus { border-color: var(--accent); }
            .try-field textarea { min-height: 60px; }
            .btn-send {
                display: inline-flex; align-items: center; gap: 8px;
                padding: 11px 22px; border-radius: 10px; border: none; cursor: pointer;
                background: linear-gradient(135deg, #38bdf8, #0ea5e9);
                color: #000; font-weight: 700; font-size: 14px;
                transition: all 0.2s;
            }
            .btn-send:hover { box-shadow: 0 6px 22px rgba(56,189,248,0.35); transform: translateY(-1px); }
            .btn-send:disabled { opacity: 0.5; cursor: not-allowed; transform: none; box-shadow: none; }

            .try-response {
                margin-top: 18px;
            }
            .try-response h4 {
                font-size: 11px; text-transform: uppercase; letter-spacing: 0.08em;
                color: var(--muted); font-weight: 700; margin-bottom: 8px;
            }
            .try-response-box {
                background: #020617; border: 1px solid var(--border); border-radius: 12px;
                padding: 18px; max-height: 350px; overflow-y: auto;
                font-family: var(--font-mono); font-size: 13px; line-height: 1.7;
                white-space: pre-wrap; word-break: break-word;
            }
            .try-response-box img { max-width: 100%; border-radius: 8px; }
            .try-response-box audio { width: 100%; margin-top: 8px; }
            .try-response-box .json-key { color: #7dd3fc; }
            .try-response-box .json-str { color: #4ade80; }
            .try-response-box .json-num { color: #fb923c; }
            .try-response-box .json-bool { color: #c084fc; }
            .try-spinner {
                display: none; align-items: center; gap: 8px; padding: 12px 0;
                color: var(--muted); font-size: 13px;
            }
            .try-spinner.active { display: flex; }
            .spinner-dot {
                width: 20px; height: 20px; border: 2px solid rgba(255,255,255,0.1);
                border-top-color: var(--accent); border-radius: 50%;
                animation: spin 0.7s linear infinite;
            }
            @keyframes spin { to { transform: rotate(360deg); } }

            /* ── FOOTER ────────────────────────── */
            .footer {
                text-align: center; padding: 24px; color: var(--muted); font-size: 13px;
                border-top: 1px solid var(--border); margin-top: 40px;
            }

            /* ── RESPONSIVE ────────────────────── */
            @media (max-width: 800px) {
                .topbar-inner { gap: 10px; padding: 14px 0; }
                .ec-header { flex-direction: column; align-items: flex-start; gap: 8px; }
                .ec-desc { margin-left: 0; text-align: left; max-width: 100%; }
                .stats-row { grid-template-columns: 1fr; }
                .baseurl-card { padding: 16px 20px; }
                .container { padding: 0 16px; }
                .baseurl-section { padding: 0 16px; }
                .topbar { padding: 0 16px; }
                .code-tabs { overflow-x: auto; }
                .param-table { font-size: 11px; }
                .param-table td, .param-table th { padding: 8px 10px; }
            }
        </style>
    </head>
    <body>
        <!-- ── TOP BAR ────────────────────────── -->
        <nav class="topbar">
            <div class="topbar-inner">
                <div class="topbar-brand">
                    <span class="topbar-dot"></span> Yori API Docs
                </div>
                <div class="topbar-nav">
                    <a href="/">Home</a>
                    <a href="/openapi.json">OpenAPI JSON</a>
                </div>
            </div>
        </nav>

        <!-- ── BASE URL ───────────────────────── -->
        <div class="baseurl-section">
            <div class="baseurl-card">
                <div>
                    <div class="baseurl-label">Base URL</div>
                </div>
                <code class="baseurl-value" id="baseUrl">https://yori-api.onrender.com</code>
                <button class="btn-copy" onclick="copyBaseUrl()" id="baseCopyBtn">
                    <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
                    Copy
                </button>
            </div>
        </div>

        <!-- ── MAIN ───────────────────────────── -->
        <main class="container">
            <!-- Stats -->
            <div class="stats-row">
                <div class="stat-pill">
                    <span class="stat-icon">🚀</span>
                    <div class="stat-info"><div class="stat-k">Status</div><div class="stat-v">Online</div></div>
                </div>
                <div class="stat-pill">
                    <span class="stat-icon">📦</span>
                    <div class="stat-info"><div class="stat-k">Version</div><div class="stat-v">1.0.0</div></div>
                </div>
                <div class="stat-pill">
                    <span class="stat-icon">🔗</span>
                    <div class="stat-info"><div class="stat-k">Endpoints</div><div class="stat-v">6 Available</div></div>
                </div>
            </div>

            <!-- Endpoints rendered by JS -->
            <div id="endpoints"></div>
        </main>

        <div class="footer">Yori API &copy; 2026 — Built for speed, bots, and fast integrations.</div>

        <script>
        // ═══════════════════════════════════════════
        //  ENDPOINT DATA
        // ═══════════════════════════════════════════
        const BASE = "https://yori-api.onrender.com";

        const endpoints = [
            {
                id: "code",
                method: "GET",
                path: "/ai/code",
                desc: "AI coding assistant — send a prompt and get intelligent code suggestions, explanations, or completions. Supports conversation history.",
                responseType: "json",
                params: [
                    { name: "prompt", type: "string", required: true, desc: "Your coding question or instruction" },
                    { name: "history", type: "string", required: false, desc: "Previous conversation for context" }
                ],
                python: `import requests

url = "${BASE}/ai/code"
params = {
    "prompt": "Write a Python function to sort a list",
    "history": ""
}

resp = requests.get(url, params=params)
data = resp.json()
print(data["response"])`,
                node: `const axios = require("axios");

const url = "${BASE}/ai/code";
const params = {
    prompt: "Write a Python function to sort a list",
    history: ""
};

axios.get(url, { params })
  .then(res => console.log(res.data.response))
  .catch(err => console.error(err));`,
                curl: `curl "${BASE}/ai/code?prompt=Write+a+Python+function+to+sort+a+list"`
            },
            {
                id: "anime",
                method: "GET",
                path: "/ai/anime",
                desc: "Generate stunning anime-style artwork from text prompts. Returns a high-quality PNG image directly.",
                responseType: "image",
                params: [
                    { name: "prompt", type: "string", required: true, desc: "Describe the anime scene you want" },
                    { name: "negative_prompt", type: "string", required: false, desc: "Things to avoid in the generation" }
                ],
                python: `import requests

url = "${BASE}/ai/anime"
params = {
    "prompt": "a beautiful sunset over Tokyo, anime style",
    "negative_prompt": ""
}

resp = requests.get(url, params=params)
with open("anime.png", "wb") as f:
    f.write(resp.content)
print("Saved as anime.png")`,
                node: `const axios = require("axios");
const fs = require("fs");

const url = "${BASE}/ai/anime";
const params = {
    prompt: "a beautiful sunset over Tokyo, anime style",
    negative_prompt: ""
};

axios.get(url, { params, responseType: "arraybuffer" })
  .then(res => {
    fs.writeFileSync("anime.png", res.data);
    console.log("Saved as anime.png");
  })
  .catch(err => console.error(err));`,
                curl: `curl "${BASE}/ai/anime?prompt=a+beautiful+sunset+over+Tokyo%2C+anime+style" -o anime.png`
            },
            {
                id: "pixel",
                method: "GET",
                path: "/ai/pixel",
                desc: "Create retro pixel art images from text descriptions. Perfect for game assets and nostalgic artwork.",
                responseType: "image",
                params: [
                    { name: "prompt", type: "string", required: true, desc: "Describe the pixel art you want" },
                    { name: "negative_prompt", type: "string", required: false, desc: "Things to avoid in the generation" }
                ],
                python: `import requests

url = "${BASE}/ai/pixel"
params = {
    "prompt": "a cute cat in 16-bit pixel art style",
    "negative_prompt": ""
}

resp = requests.get(url, params=params)
with open("pixel.png", "wb") as f:
    f.write(resp.content)
print("Saved as pixel.png")`,
                node: `const axios = require("axios");
const fs = require("fs");

const url = "${BASE}/ai/pixel";
const params = {
    prompt: "a cute cat in 16-bit pixel art style",
    negative_prompt: ""
};

axios.get(url, { params, responseType: "arraybuffer" })
  .then(res => {
    fs.writeFileSync("pixel.png", res.data);
    console.log("Saved as pixel.png");
  })
  .catch(err => console.error(err));`,
                curl: `curl "${BASE}/ai/pixel?prompt=a+cute+cat+in+16-bit+pixel+art+style" -o pixel.png`
            },
            {
                id: "cartoon",
                method: "GET",
                path: "/ai/cartoon",
                desc: "Transform any photo into a cartoon or anime-style image. Provide an image URL and get back the stylized result.",
                responseType: "json",
                params: [
                    { name: "imageurl", type: "string", required: true, desc: "URL of the image to cartoonize" }
                ],
                python: `import requests

url = "${BASE}/ai/cartoon"
params = {"imageurl": "https://example.com/photo.jpg"}

resp = requests.get(url, params=params)
data = resp.json()
print(data["anime_image"])`,
                node: `const axios = require("axios");

const url = "${BASE}/ai/cartoon";
const params = { imageurl: "https://example.com/photo.jpg" };

axios.get(url, { params })
  .then(res => console.log(res.data.anime_image))
  .catch(err => console.error(err));`,
                curl: `curl "${BASE}/ai/cartoon?imageurl=https://example.com/photo.jpg"`
            },
            {
                id: "download",
                method: "GET",
                path: "/tools/download",
                desc: "Universal media downloader supporting YouTube, Pinterest, and more. Extracts images, videos, and audio links.",
                responseType: "json",
                params: [
                    { name: "url", type: "string", required: true, desc: "URL of the media page to download from" }
                ],
                python: `import requests

url = "${BASE}/tools/download"
params = {"url": "https://youtube.com/watch?v=dQw4w9WgXcQ"}

resp = requests.get(url, params=params)
data = resp.json()
for media in data.get("medias", []):
    print(media.get("url"))`,
                node: `const axios = require("axios");

const url = "${BASE}/tools/download";
const params = { url: "https://youtube.com/watch?v=dQw4w9WgXcQ" };

axios.get(url, { params })
  .then(res => {
    res.data.medias.forEach(m => console.log(m.url));
  })
  .catch(err => console.error(err));`,
                curl: `curl "${BASE}/tools/download?url=https://youtube.com/watch?v=dQw4w9WgXcQ"`
            },
            {
                id: "tts",
                method: "GET",
                path: "/tts/hindi",
                desc: "Convert Hindi text into natural-sounding speech. Returns an MP3 audio file ready for playback.",
                responseType: "audio",
                params: [
                    { name: "text", type: "string", required: true, desc: "Hindi text to convert to speech" }
                ],
                python: `import requests

url = "${BASE}/tts/hindi"
params = {"text": "नमस्ते दुनिया, आपका स्वागत है"}

resp = requests.get(url, params=params)
with open("speech.mp3", "wb") as f:
    f.write(resp.content)
print("Saved as speech.mp3")`,
                node: `const axios = require("axios");
const fs = require("fs");

const url = "${BASE}/tts/hindi";
const params = { text: "नमस्ते दुनिया, आपका स्वागत है" };

axios.get(url, { params, responseType: "arraybuffer" })
  .then(res => {
    fs.writeFileSync("speech.mp3", res.data);
    console.log("Saved as speech.mp3");
  })
  .catch(err => console.error(err));`,
                curl: `curl "${BASE}/tts/hindi?text=%E0%A4%A8%E0%A4%AE%E0%A4%B8%E0%A5%8D%E0%A4%A4%E0%A5%87+%E0%A4%A6%E0%A5%81%E0%A4%A8%E0%A4%BF%E0%A4%AF%E0%A4%BE" -o speech.mp3`
            }
        ];

        // ═══════════════════════════════════════════
        //  RENDER CARDS
        // ═══════════════════════════════════════════
        function renderEndpoints() {
            const container = document.getElementById("endpoints");
            let html = "";

            endpoints.forEach((ep, idx) => {
                const reqParams = ep.params.filter(p => p.required);
                const optParams = ep.params.filter(p => !p.required);

                html += `
                <div class="endpoint-card" id="card-${ep.id}">
                    <div class="ec-header">
                        <span class="ec-method">${ep.method}</span>
                        <span class="ec-path">${ep.path}</span>
                        <span class="ec-desc">${ep.desc}</span>
                    </div>
                    <div class="ec-body">
                        <!-- Parameters -->
                        <div class="ec-params">
                            <h4>Parameters</h4>
                            <table class="param-table">
                                <thead>
                                    <tr><th>Name</th><th>Type</th><th>Required</th><th>Description</th></tr>
                                </thead>
                                <tbody>
                                    ${ep.params.map(p => `
                                    <tr>
                                        <td>${p.name}</td>
                                        <td>${p.type}</td>
                                        <td>${p.required ? '<span class="badge-req">Yes</span>' : '<span class="badge-opt">No</span>'}</td>
                                        <td>${p.desc}</td>
                                    </tr>`).join("")}
                                </tbody>
                            </table>
                        </div>

                        <!-- Code Snippets -->
                        <div class="code-section">
                            <div class="code-tabs">
                                <button class="code-tab active" onclick="switchTab('${ep.id}', 'python', this)">Python</button>
                                <button class="code-tab" onclick="switchTab('${ep.id}', 'node', this)">Node.js</button>
                                <button class="code-tab" onclick="switchTab('${ep.id}', 'curl', this)">cURL</button>
                                <button class="code-copy-btn" onclick="copySnippet('${ep.id}')" id="copyBtn-${ep.id}">
                                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
                                    Copy
                                </button>
                            </div>
                            <div class="code-block">
                                <div class="code-panel active" id="code-${ep.id}-python"><pre>${escapeHTML(ep.python)}</pre></div>
                                <div class="code-panel" id="code-${ep.id}-node"><pre>${escapeHTML(ep.node)}</pre></div>
                                <div class="code-panel" id="code-${ep.id}-curl"><pre>${escapeHTML(ep.curl)}</pre></div>
                            </div>
                        </div>

                        <!-- Try Now -->
                        <button class="try-toggle" onclick="toggleTry('${ep.id}')" id="tryBtn-${ep.id}">
                            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polygon points="5 3 19 12 5 21 5 3"/></svg>
                            Try Now
                        </button>

                        <div class="try-panel" id="tryPanel-${ep.id}">
                            <div class="try-panel-inner">
                                ${ep.params.map(p => `
                                <div class="try-field">
                                    <label>${p.name} ${p.required ? '<span style="color:var(--red)">*</span>' : '<span style="color:var(--muted)">(optional)</span>'}</label>
                                    ${p.name === "history" || p.name === "negative_prompt" || p.name === "text"
                                        ? `<textarea id="try-${ep.id}-${p.name}" placeholder="${ep.params[0].name === "text" ? "नमस्ते दुनिया..." : "Enter ${p.name}..."}" rows="2"></textarea>`
                                        : `<input type="text" id="try-${ep.id}-${p.name}" placeholder="${p.desc}" />`
                                    }
                                </div>`).join("")}
                                <button class="btn-send" onclick="sendRequest('${ep.id}')" id="sendBtn-${ep.id}">
                                    ⚡ Send Request
                                </button>
                                <div class="try-spinner" id="spinner-${ep.id}">
                                    <div class="spinner-dot"></div> Waiting for response...
                                </div>
                                <div class="try-response" id="tryResp-${ep.id}" style="display:none;">
                                    <h4>Response</h4>
                                    <div class="try-response-box" id="tryRespBox-${ep.id}"></div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>`;
            });

            container.innerHTML = html;
        }

        function escapeHTML(str) {
            return str.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
        }

        // ═══════════════════════════════════════════
        //  TAB SWITCHING
        // ═══════════════════════════════════════════
        function switchTab(epId, lang, btn) {
            // Update all panels for this endpoint
            ["python", "node", "curl"].forEach(l => {
                document.getElementById(`code-${epId}-${l}`).classList.toggle("active", l === lang);
            });
            // Update tab buttons
            const tabs = btn.parentElement.querySelectorAll(".code-tab");
            tabs.forEach(t => t.classList.remove("active"));
            btn.classList.add("active");
        }

        // ═══════════════════════════════════════════
        //  COPY HELPERS
        // ═══════════════════════════════════════════
        function copyBaseUrl() {
            const btn = document.getElementById("baseCopyBtn");
            navigator.clipboard.writeText(BASE).then(() => {
                btn.classList.add("copied");
                btn.innerHTML = `<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg> Copied!`;
                setTimeout(() => {
                    btn.classList.remove("copied");
                    btn.innerHTML = `<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg> Copy`;
                }, 2000);
            });
        }

        function copySnippet(epId) {
            const ep = endpoints.find(e => e.id === epId);
            // Determine active tab
            const activeTab = document.querySelector(`#card-${epId} .code-tab.active`);
            const lang = activeTab ? activeTab.textContent.toLowerCase().replace(".js", "") : "python";
            const langKey = lang === "node.js" ? "node" : lang;
            const text = ep[langKey];

            const btn = document.getElementById(`copyBtn-${epId}`);
            navigator.clipboard.writeText(text).then(() => {
                btn.classList.add("copied");
                btn.innerHTML = `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg> Copied!`;
                setTimeout(() => {
                    btn.classList.remove("copied");
                    btn.innerHTML = `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg> Copy`;
                }, 2000);
            });
        }

        // ═══════════════════════════════════════════
        //  TRY NOW — TOGGLE
        // ═══════════════════════════════════════════
        function toggleTry(epId) {
            const panel = document.getElementById(`tryPanel-${epId}`);
            const btn = document.getElementById(`tryBtn-${epId}`);
            const isOpen = panel.classList.contains("expanded");

            // Close all other panels
            document.querySelectorAll(".try-panel.expanded").forEach(p => p.classList.remove("expanded"));
            document.querySelectorAll(".try-toggle.open").forEach(b => b.classList.remove("open"));

            if (!isOpen) {
                panel.classList.add("expanded");
                btn.classList.add("open");
                // Hide previous response
                document.getElementById(`tryResp-${epId}`).style.display = "none";
                document.getElementById(`spinner-${epId}`).classList.remove("active");
            }
        }

        // ═══════════════════════════════════════════
        //  TRY NOW — SEND
        // ═══════════════════════════════════════════
        function sendRequest(epId) {
            const ep = endpoints.find(e => e.id === epId);
            const respDiv = document.getElementById(`tryResp-${epId}`);
            const respBox = document.getElementById(`tryRespBox-${epId}`);
            const spinner = document.getElementById(`spinner-${epId}`);
            const sendBtn = document.getElementById(`sendBtn-${epId}`);

            // Build query params
            const params = new URLSearchParams();
            let missing = false;
            ep.params.forEach(p => {
                const el = document.getElementById(`try-${epId}-${p.name}`);
                const val = el ? el.value.trim() : "";
                if (p.required && !val) {
                    el.style.borderColor = "var(--red)";
                    missing = true;
                } else if (el) {
                    el.style.borderColor = "";
                }
                if (val) params.append(p.name, val);
            });
            if (missing) return;

            const url = `${BASE}${ep.path}?${params.toString()}`;

            // Show spinner
            spinner.classList.add("active");
            respDiv.style.display = "none";
            sendBtn.disabled = true;

            if (ep.responseType === "image") {
                // Display image directly
                const img = new Image();
                img.onload = () => {
                    spinner.classList.remove("active");
                    sendBtn.disabled = false;
                    respDiv.style.display = "block";
                    respBox.innerHTML = "";
                    respBox.appendChild(img);
                };
                img.onerror = () => {
                    showError(epId, "Failed to load image. The upstream service may be unavailable.");
                };
                img.src = url;
                img.style.maxWidth = "100%";
                img.style.borderRadius = "8px";
            } else if (ep.responseType === "audio") {
                // Display audio player
                const audio = document.createElement("audio");
                audio.controls = true;
                audio.style.width = "100%";
                audio.onloadedmetadata = () => {
                    spinner.classList.remove("active");
                    sendBtn.disabled = false;
                    respDiv.style.display = "block";
                    respBox.innerHTML = "";
                    respBox.appendChild(audio);
                    respBox.insertAdjacentHTML("beforeend", `<p style="margin-top:10px;color:var(--muted);font-size:12px;">🎧 Audio loaded — press play</p>`);
                };
                audio.onerror = () => {
                    showError(epId, "Failed to load audio. The upstream service may be unavailable.");
                };
                audio.src = url;
                respBox.innerHTML = "";
                respBox.appendChild(audio);
                respDiv.style.display = "block";
                // Fallback: if metadata never fires, show after timeout
                setTimeout(() => {
                    if (spinner.classList.contains("active")) {
                        spinner.classList.remove("active");
                        sendBtn.disabled = false;
                    }
                }, 4000);
            } else {
                // JSON endpoint
                fetch(url)
                    .then(r => {
                        if (!r.ok) throw new Error(`HTTP ${r.status}`);
                        return r.json();
                    })
                    .then(data => {
                        spinner.classList.remove("active");
                        sendBtn.disabled = false;
                        respDiv.style.display = "block";
                        respBox.innerHTML = syntaxHighlight(JSON.stringify(data, null, 2));
                    })
                    .catch(err => {
                        showError(epId, `Request failed: ${err.message}`);
                    });
            }
        }

        function showError(epId, msg) {
            const spinner = document.getElementById(`spinner-${epId}`);
            const respDiv = document.getElementById(`tryResp-${epId}`);
            const respBox = document.getElementById(`tryRespBox-${epId}`);
            const sendBtn = document.getElementById(`sendBtn-${epId}`);
            spinner.classList.remove("active");
            sendBtn.disabled = false;
            respDiv.style.display = "block";
            respBox.innerHTML = `<span style="color:var(--red);">⚠ ${escapeHTML(msg)}</span>`;
        }

        // ═══════════════════════════════════════════
        //  JSON SYNTAX HIGHLIGHT
        // ═══════════════════════════════════════════
        function syntaxHighlight(json) {
            return json.replace(/("(\\u[a-fA-F0-9]{4}|\\[^u]|[^"\\])*"(\\s*:)?|\b(true|false|null)\b|-?\\d+(?:\\.\\d*)?(?:[eE][+\\-]?\\d+)?)/g, function (match) {
                let cls = "json-num";
                if (/^"/.test(match)) {
                    if (/:$/.test(match)) {
                        cls = "json-key";
                    } else {
                        cls = "json-str";
                    }
                } else if (/true|false/.test(match)) {
                    cls = "json-bool";
                } else if (/null/.test(match)) {
                    cls = "json-bool";
                }
                return '<span class="' + cls + '">' + match + '</span>';
            });
        }

        // ═══════════════════════════════════════════
        //  INIT
        // ═══════════════════════════════════════════
        renderEndpoints();
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