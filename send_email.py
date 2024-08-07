sender_email = "Your email"
receiver_email = "receiver email"
password = "your password"

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

def send_email():
    msg = MIMEMultipart('related')
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "Test email"

    with open("sphere_email.html", "r") as file:
        html_content = file.read()

    msg.attach(MIMEText(html_content, 'html')) 

    fp = open('sphere.png', 'rb')
    image1 = MIMEImage(fp.read())
    fp.close()

    image1.add_header('Content-ID', '<image1>')
    msg.attach(image1)

    fp = open('bnr360.png', 'rb')
    image2 = MIMEImage(fp.read())
    fp.close()

    image2.add_header('Content-ID', '<image2>')
    msg.attach(image2)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
    
    print("Email Sent")

try:
    send_email()
except TypeError as e:
    print(e)
