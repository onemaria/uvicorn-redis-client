import json
from fastapi import HTTPException
import redis
from utils import transcribe_dna_to_rna, translate_mrna_to_amino_acids, get_mrna_from_rna


def redis_instance():
    return redis.Redis(host="localhost", port=6379, db=0)


def add_gene_data(gene: str, dna_sequence: str):
    redis_client = redis_instance()
    rna_sequence = transcribe_dna_to_rna(dna_sequence)
    mrna_sequence = get_mrna_from_rna(rna_sequence)
    protein = translate_mrna_to_amino_acids(mrna_sequence)
    value = {
        "DNA": dna_sequence,
        "RNA": rna_sequence,
        "protein": protein
    }
    value = json.dumps(value)
    print(f"gene: {gene}, DNA sequence: {dna_sequence}, RNA sequence: {rna_sequence}, mRNA sequence: {mrna_sequence}, protein: {protein}")
    response = redis_client.set(gene, value)
    if response:
        return
    else:
        raise HTTPException(detail=f'Gene data was not saved')

def set_key(key: str, value: str):
    redis_client = redis_instance()
    response = redis_client.set(key, value)
    if response:
        return
    else:
        raise HTTPException(detail=f'Key-Value pair was not saved')


def get_key(key: str):
    redis_client = redis_instance()
    value = redis_client.get(key)
    if value:
        return value
    else:
        raise HTTPException(detail=f'Gene was not found')


def delete_key(key: str):
    redis_client = redis_instance()
    response = redis_client.delete(key)
    if response:
        return
    else:
        raise HTTPException(detail=f'Gene data was not deleted')
