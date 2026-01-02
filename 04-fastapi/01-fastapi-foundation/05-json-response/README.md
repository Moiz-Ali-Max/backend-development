# JSON Responses
JSON: JavaScript Object Notation. It's a simple data format like dictionaries in python
- What we do so far it's also an example of JSON
- So when server sends data to the client then it's in the JSON Format.
- But FastAPI also have their own JSON responses

### How FastAPI make json responses?
In FastAPI when we do return like python dict, list, or even pydantic model then fastapi automatically converts it into JSON Format
- No need to do manually json.dumps()

### What is FastAPI it's own JSON Response?
FastAPI internally uses Starlette JSON Response
- JSONResponse is a class which convert python into json and make HTTP responses.
- We can make our own custom JSON response by import json.responses from fastapi.responses

### Fast JSON Responss Vs. Normal Return Dictionary?
| Cheez         | Normal `return dict`   | Using `JSONResponse`                                         |
| ------------- | ---------------------- | ------------------------------------------------------------ |
| Conversion    | Automatic              | Manual call                                                  |
| Customization | Limited                | Full control (headers, status code, etc.)                    |
| Use case      | Simple APIs            | advanced control chahiye                                 |
| Example       | `return {"msg": "Hi"}` | `return JSONResponse(content={"msg":"Hi"}, status_code=201)` |

### When to use which JSON?
##### Simple Use Case:
- When send simply data
- Default status code (like 200 or 500)
So return dict, fastapi automatically makes json responses

##### Advance Use Case:
- Use JSON Response
- when we want to send custom status codes, extra headers, or custom media types

