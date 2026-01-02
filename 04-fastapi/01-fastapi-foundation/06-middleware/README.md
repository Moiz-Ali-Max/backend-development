# Middleware
It is that part of code where it runs in between the request and response

Flow of middleware:
- When client sends any request
- It is first go to middleware
- Middleware check based on their deafualt cors or any custom middleware which we defined, if it passes then it the request goes to the response
- Even response moves back from the middleware to send the respone back to client.

FastAPI Middleware:
To use middleware in fastapi we can do multiple things, like:
1. To modify the request
2. To modify the response
3. Do Logging
4. Enable cors (origins, ip's)
5. Check Authentication


#### Simple Middleware Example:
``` 
from fastapi import FastAPI, Request
import time

app = FastAPI()

@app.middleware('http')
async def add_process_time(request: Request, call_next):
    start_time = time.time()
    process_time = time.time() - start_time
    response.headers['X-Process-Time'] = str(pocess_time)

    return response

``` 

Example Explanation:
- app.middleware("http"): Tells middleware runs on eevery http request
- request: Request: Object of incoming request 
- call_next: next function (endpoint or next middleware) 
- start_time = time.time(): time record starts
- response = await call_next(request): Move request to next step and get response 
- process_time = ...: total processing time calculatation
- response.headers["X-Process-Time"] = ...: Add processing time in response headers 
- return response: Send modified response to client

### When to use Middleware?
When
- Implementing Common between request and response
- Logging, analytics, security checks 
- Add Headers 
- Implement Rate limiting 
- Handle CORS

### Difference between middleware and dependency injection
- ##### Middleware: Each request/response -> Global Level
- ##### Dependency Injection: specific endpoints


### Why async in middleware?
Because FastAPI is a async server.
- If middleware sync then server might be slow or even block sometimes
- That's why middleware should be async def


### CORS = Cross-Origin Resource Sharing
When our frontend app (running in brwoser) or different domain sends backend api call, then browser security blocks this request for security reasons 

#### CORS middleware:
- Restricts or allows the browser to which domain have access
- Add headers which tells browser if request allowed or not.

#### Example of Cors Middleware
```
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

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

```

### Custom Middleware
We write based on our logic
- Works on each request/response
- Like logging, authentication check, modify responses
