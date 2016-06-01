from twilio.rest import TwilioRestClient
 
# Find these values at https://twilio.com/user/account
account_sid = "AC849d391e0b8b8c9c0affa794f5493840"
auth_token = "391df24967a15463ee4d2351d1002b47"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(to="+48601802600", from_="+48223070660",
                                     body="zaraz pojdziemy myszko!")