
from email.mime.text import MIMEText 
from email.mime.image import MIMEImage 
from email.mime.application import MIMEApplication 
from email.mime.multipart import MIMEMultipart 
import smtplib 
import os

smtp = smtplib.SMTP('smtp.gmail.com', 587) 
smtp.ehlo() 
smtp.starttls() 
smtp.login('YourMail@gmail.com', 'Your Password')


msg = MIMEMultipart() 
msg['Subject'] = subject 
msg.attach(MIMEText(text))