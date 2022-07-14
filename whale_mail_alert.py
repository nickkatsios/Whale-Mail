import requests
import smtplib
from email.message import EmailMessage
import time
import schedule
import os

# Get environment variable values. 
key = os.environ.get("WHALE_ALERT_API_KEY")
app_password = os.environ.get("WHALE_MAIL_APP_PASSWORD")

# List all recipients of whale mail. 
# Add any e-mail adress by appending it to the list.  
recipients = ["whale.mail.alert@gmail.com"]

# Interval between excecutions in seconds.
interval = 120

# Call Whale Alert API to list all large tranactions (>500.000$) at a set interval time. 
# Transaction log starts from x (interval) secs ago and ends the moment we call the API (now)
# in order to achieve live tranaction monitoring. 
def api_call():

    # Parameters to add to request URL. 
    payload = {
    "api_key" : key,
    "start" : int(time.time()) - interval,
    "end" : int(time.time()) 
    }

    print("Time Start: " + str(payload["start"]))
    print("Time End: " + str(payload["end"]))
    print()
    # API call
    r = requests.get("https://api.whale-alert.io/v1/transactions" , params = payload)
    r_dict = r.json()

    # Extract wantedd info from .json response 
    if int(r_dict["count"]) > 0:
        for transaction in r_dict["transactions"]:
            blockchain = transaction["blockchain"]
            usd_value = int(transaction["amount_usd"])
            hash = transaction["hash"]
            print(blockchain + ": " + str(usd_value) + " hash " + hash )
            # Mail-Alert Recipients
            send_mail_alert(blockchain , usd_value , hash)


# Implement e-mail sending using smtp lib
def send_mail_alert(blockchain , usd_value , hash):
    
    mail = EmailMessage()
    mail["Subject"] = "Alert!"
    mail["From"] = "whale.mail.alert@gmail.com"
    mail["To"] = ", ".join(recipients)

    mail.set_content("Large transaction on " + blockchain + " blockchain." + "USD value: " + str(usd_value))
    
    """ HTML MAIL TO BE IMPLEMENTED """
    # mail.add_alternative("""\
    # <!DOCTYPE html>
    # <html>
    #     <body>
    #         <h1>Alert!</h1>
    #         <img src="" alt="">
    #     </body>
    # </html>
    # """ , subtype = 'html')

    with smtplib.SMTP_SSL("smtp.gmail.com" , 465) as smtp:
        smtp.login("whale.mail.alert@gmail.com" , app_password)
        smtp.send_message(mail)
        print("Mail Sent!")
        print()

# Run the script at set intervals 
schedule.every(interval).seconds.do(api_call)

while True:
    schedule.run_pending()