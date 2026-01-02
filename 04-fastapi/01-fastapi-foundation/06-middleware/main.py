from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import time

app = FastAPI()

#CORS Middleware Example
origins = [
    "http://localhost:3000",   # Frontend URL
    "http://127.0.0.1:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,           # Which domains allow
    allow_credentials=True,
    allow_methods=["*"],             # GET, POST, etc allow
    allow_headers=["*"],             # Headers allow
)


@app.middleware("http") #runs for every request
async def add_process_time_header(request: Request, call_next):
    #request-> object of incoming request
    #call_next-> to forwar the request to the actual path operation function

    start_time = time.time() #beforoe processing the request
    response = await call_next(request) #forward the request to the actual path operation function
    process_time = time.time() - start_time #time taken to process the request
    response.headers['X-Process-Time'] = str(process_time) #adding custom header to the response

    return response #returning the response to the client

@app.get("/")
def server_check():
    return {
        "status": 200,
        "message": "server is running"
    }

