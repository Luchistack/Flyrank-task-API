from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

tasks = [
    {"id" : 1, "title" : "Learn FastAPI", "done" : False},
    {"id" : 2, "title" : "Build CRUD AP", "done" : False},
    {"id" : 3, "title" : "Push to Github", "done" : False},
]
# stage 1
# @app.get("/")
# def read_root():
#     return {"message": "Hello Server"}


# stage 2
@app.get("/")
def read_root():
    return {"name" : "Task API",
            "version" : "1.0",
            "endpoints" : ["/tasks"]
            }

@app.get("/health")
def health_check():
    return {"status" : "ok"}

#
