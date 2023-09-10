# app.py
from google.cloud import bigquery

from fastapi import FastAPI
import os
from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()
biqQueryClient = bigquery.Client()

account_sid = os.getenv('account_sid')
auth_token = os.getenv('auth_token')
client = Client(account_sid, auth_token)

app = FastAPI()

@app.get("/transactions")
async def get_transactions(card_number : str):
    QUERY = (
        'SELECT * FROM `stalwart-realm-339201.starter.data` '
        'WHERE credit_card_number = "' + card_number + '"')
    query_job = biqQueryClient.query(QUERY)  # API request
    rows = query_job.result()  # Waits for query to finish

    for row in rows:
        print(row.name)
        return card_number


@app.post("/fraud", status_code=201)
async def send_fraud(phone_number, message : str):
    message = client.messages.create(
        from_='+18447813048',
        body=message,
        to=phone_number
    )
    return 'success'