from twilio.rest import Client

account_sid = 'AC52ba8b64d5f9544d1a306e51da73df87'
auth_token = '5890dd07bd7e35d2784dec141a80d210'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+18447813048',
  body='test',
  to='+12254543021'
)

print(message.sid)