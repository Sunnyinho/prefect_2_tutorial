import os
from prefect import flow, task
from pydantic import BaseModel

class Model(BaseModel):
    a: int
    b: float
    c: str

@task
def printer(obj):
    print(f"Received a {type(obj)} with value {obj}")

@flow(version=os.getenv("GIT_COMMIT_SHA"))
def model_validator(model: Model):
    printer(model)

model_validator({"a": 42, "b": 0, "c": 55})
print(os.getenv("GIT_COMMIT_SHA"))