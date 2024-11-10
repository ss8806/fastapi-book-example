from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()


@app.get("/hello")
async def hello():
    return {"message": "hello world"}
