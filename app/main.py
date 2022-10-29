from fastapi import FastAPI, Request, Response

app = FastAPI()

@app.get("/contour-middleware-test/header")
async def test_header(request: Request, response: Response, allow_credential: bool = True):
    if allow_credential:
        response.headers["Access-Control-Allow-Credentials"] = "true"

    return request.headers
