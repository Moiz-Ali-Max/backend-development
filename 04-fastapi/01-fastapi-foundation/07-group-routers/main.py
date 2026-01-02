from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def server_check():
    return {
        "message": "server is runnign"
    }
