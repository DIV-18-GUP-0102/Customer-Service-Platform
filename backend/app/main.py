from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title = "Customer Service Platform")


@app.get("/")
async def root():
    return {"message": "This is a Custoer Service Platform in making"}