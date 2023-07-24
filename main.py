import uvicorn
from fastapi import FastAPI
import client

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post('/set-key', summary='Create key-value pair')
def set_key(key: str, value: str):
    client.set_key(key, value)


@app.get('/get-key', summary='Retrieve value of a given key')
def get_key(key: str):
    return client.get_key(key)


@app.delete('/delete-key', summary='Delete key-value pair')
def delete_key(key: str):
    client.delete_key(key)


if __name__ == "__main__":
    uvicorn.run(app, port=8000)
