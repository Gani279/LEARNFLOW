# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 21:01:37 2024

@author: User
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from getpass import getpass

def send_email(sender_email, sender_password, to_email, subject, message):
    # Set up the MIME
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach the message
    msg.attach(MIMEText(message, 'plain'))

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)

        # Send the email
        server.sendmail(sender_email, to_email, msg.as_string())

if __name__ == "__main__":
    print("Automated Email Sender")

    # Input sender's email and password
    sender_email = input("Enter your email: ")
    sender_password = getpass("Enter your email password (or app password): ")

    # Input recipient's email
    to_email = input("Enter recipient's email: ")

    # Input email subject and message
    subject = input("Enter email subject: ")
    message = input("Enter your message: ")

    # Send the email
    send_email(sender_email, sender_password, to_email, subject, message)

    print("Email sent successfully!")
