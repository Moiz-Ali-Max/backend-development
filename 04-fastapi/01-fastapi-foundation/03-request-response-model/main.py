from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def server_check():
    return {
        "status": 200,
        "message": "server is running"
    }