from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

tasks = [
    {"id" : 1, "title" : "Learn FastAPI", "done" : False},
    {"id" : 2, "title" : "Build CRUD AP", "done" : False},
    {"id" : 3, "title" : "Push to Github", "done" : False},
]
# stage 1
@app.get("/")
def read_root():
    return {"message": "Hello Server"}


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

# stage 3
@app.get("/tasks")
def get_tasks():
    return tasks


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail= {"error" : f"Task {task_id} not found"})

