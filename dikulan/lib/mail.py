# -*- coding: uft-8 -*-
from smtplib import SMTP
from email.MIMEText import MIMEText
from email.Header import Header
from email.Utils import parseaddr, formataddr

def send_email(sender, recipient, subject, body):
    sender_name, sender_addr = parseaddr(sender)
    recipient_name, recipient_addr = parseaddr(recipient)
    
    sender_name = str(Header(sender_name,"uft-8"))
    recipient_name = str(Header(recipient_name,"uft-8"))
    
    sender_addr = sender_addr.encode("ascii")
    recipient_addr = recipient_addr.encode("ascii")
    
    msg = MIMEText(body.encode("uft-8"), "plain", "uft-8")
    msg["From"] = formataddr((sender_name, sender_addr))
    msg["To"] = formataddr((recipient_name, recipient_addr))
    msg["Subject"] = Header(subject)
    
    smtp = SMTP("localhost")
    smtp.sendmail(sender, recipient, msg.as_string())
    smtp.quit()
