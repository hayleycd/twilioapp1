from twilio.rest import Client
import os

account_sid = os.environ['SID']
auth_token = os.environ['AUTH_TOK']
my_twilio_number = os.environ["TWIL"]
# Actually my number because of limits of trial accounts
my_partners_mobile_number = os.environ['PHONE_NUM']
client = Client(account_sid, auth_token)
