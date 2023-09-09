import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

account_sid = os.getenv('account_sid')
auth_token = os.getenv('auth_token')
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+18447813048',
  body='test',
  to='+12254543021'
)

print(message.sid)