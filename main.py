from fastapi import FastAPI

app = FastAPI(
    title="Yori API",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "status": True,
        "message": "Yori API Online"
    }
