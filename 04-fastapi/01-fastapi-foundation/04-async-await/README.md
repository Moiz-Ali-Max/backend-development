# Async / Await
Async/Await tells fastapi to wait without blocking the server
- It means when we making a async functions so it runs parallel, means multiple functions execute simultaneously.
- And awai tells that let this data comes, but don't block the server
- Simple we say that:
    - async: function is async
    - await: wait withotu blocking

Now see this example:
```
def user(): #simple sync function
    ... #if it's wait, then the whole server will wait

#But when we use async
async def user():
    ... #if it's wait then whole server is not block, all other request conitnue running
```

### Why fastapi uses async?
Fastapi builds to high performance async server
- API Call
- Database Call
- LLM / OpenAI / File (Read, Write)

### Example of Request + Response + Async Await
```
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import asyncio

app = FastAPI()

class LoginRequest(BaseMmodel):
    email: str
    password: str

class LoginResponse(BaseModel):
    message: str


@app.post("/login-checl", response_model= LoginResponse)
async def login_check(request: LoginRequest):
    if request.email == "admin123@gmail.com" and request.password == "admin123":
        asyncio.sleep(3) #wait for 3 seconds -> fake DB Call
        return LoginResponse(message= "Authenticated: Async Func gives access")

    else:
        raise HTTPException("Unauthorized: Invalid")
```
