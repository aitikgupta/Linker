import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def send_it(messagetxt):
    print("this is the message:  ", messagetxt)
    message = Mail(
        from_email='mayra.pastor@estudiantat.upc.edu',
        to_emails='pastorvaldivia.m@gmail.com',
        subject='Sending with Twilio SendGrid is Fun',
        html_content=messagetxt)        

    #Using os won't work for Chrome extension...
    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sg.send(message)
    print(response.status_code, response.body, response.headers)
