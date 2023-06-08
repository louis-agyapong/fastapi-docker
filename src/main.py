from typing import Union

from fastapi import FastAPI
import redis
import debugpy

r = redis.Redis(host="redis", port=6379)

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "Zion K Agyapong"} 


@app.get("/hits")
def read_root():
    r.incr("hits")
    return {"number of hits": r.get("hits")}
