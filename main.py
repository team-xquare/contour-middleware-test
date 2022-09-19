from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/contour-middleware-test/header")
async def test_header(request: Request):
    return request.headers