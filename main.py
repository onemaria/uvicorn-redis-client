import uvicorn
from fastapi import FastAPI
from starlette.responses import RedirectResponse
import client

app = FastAPI()
app.title = "Simple tool for DNA to RNA transcription and RNA to protein translation"


@app.get("/", include_in_schema=False)
async def redirect_to_docs():
    return RedirectResponse(url="/docs")


@app.post("/save-gene-data", summary='Please insert the name of the gene as you want it saved in the database and its DNA sequence')
def get_gene_data(gene: str, dna_sequence: str):
    client.add_gene_data(gene, dna_sequence)


@app.post('/set-key', summary='Save data as Key-Value pair')
def set_key(key: str, value: str):
    client.set_key(key, value)


@app.get('/get-gene-data', summary='Get data for a given gene')
def get_key(key: str):
    return client.get_key(key)


@app.delete('/delete-gene-data', summary='Delete gene data from the database by giving the gene name')
def delete_key(key: str):
    client.delete_key(key)


if __name__ == "__main__":
    uvicorn.run(app, port=8000)
