from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def server_check():
    return {
        "message": "server is running"
    } #status code 200 by default


@app.get("/get-message-json-response") #custom JSON Response
def get_message_json_response():
    return JSONResponse(
        status_code= 201,
        content = {
            "message": "This is a JSON Response with custom status code"
        },
        headers= {"custom-header": "custom-header-value"}
    ) 