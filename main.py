import uvicorn
from fastapi import FastAPI
from starlette.responses import RedirectResponse
import client

app = FastAPI()
app.title = "Simple tool Redis Microservice"


@app.get("/", include_in_schema=False)
async def redirect_to_docs():
    return RedirectResponse(url="/docs")


@app.post('/set-key', summary='Save data as Key-Value pair')
def set_key(key: str, value: str):
    client.set_key(key, value)


@app.get('/get-key', summary='Get data for a given key')
def get_key(key: str):
    return client.get_key(key)


@app.delete('/delete-key', summary='Delete key-value from the database by inserting the key')
def delete_key(key: str):
    client.delete_key(key)


if __name__ == "__main__":
    uvicorn.run(app, port=8000)
