from fastapi import FastAPI
from routers import users, faculty

app = FastAPI()

@app.get("/")
def server_check():
    return {
        "message": "server is runnign"
    }

app.include_router(users.router, prefix= "/users", tags=['User Routers'])
app.include_router(faculty.router, prefix= "/faculty", tags= ['Faculty Routers'])

