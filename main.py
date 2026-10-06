from fastapi import FastAPI

app = FastAPI(title="MBC Matrix Panel")

@app.get("/")
def home():
    return {
        "status": "online",
        "message": "MBC Matrix Backend is running"
    }
