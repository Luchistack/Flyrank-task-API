from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# stage 1
@app.get("/")
def read_root():
    return {"message": "Hello Server"}

