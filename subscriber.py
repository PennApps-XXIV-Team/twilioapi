import os
from dotenv import load_dotenv
from google.cloud import pubsub_v1
from concurrent.futures import TimeoutError
from twilio.rest import Client

load_dotenv()

credentials_path = 'twilioapi-privatekey.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

account_sid = os.getenv('account_sid')
auth_token = os.getenv('auth_token')
client = Client(account_sid, auth_token)

timeout = 5.0

subscriber = pubsub_v1.SubscriberClient()
subscription_path = 'projects/stalwart-realm-339201/subscriptions/fraudulent-sub'

message = client.messages.create(
  from_='+18447813048',
  body='test',
  to='+12254543021'
)

def callback(message):
    print(message.sid)

streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)
print(f'Listening for messages on {subscription_path}')

with subscriber:
    try:
        streaming_pull_future.result()
    except TimeoutError:
        streaming_pull_future.cancel()
        streaming_pull_future.result()