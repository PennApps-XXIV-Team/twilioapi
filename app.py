# app.py
from google.cloud import bigquery
import os

from fastapi import FastAPI
from dotenv import load_dotenv
load_dotenv()
biqQueryClient = bigquery.Client()

app = FastAPI()

@app.get("/transactions")
async def get_transactions(card_number : str):
    QUERY = (
        'SELECT * FROM `stalwart-realm-339201.demo.flagged_transaction`'
        'WHERE cardnumber = "' + card_number + '"')
    query_job = biqQueryClient.query(QUERY)  # API request
    rows = query_job.result()  # Waits for query to finish

    for row in rows:
        print(row.name)