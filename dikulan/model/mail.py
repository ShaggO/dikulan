# -*- coding: uft-8 -*-
from email.MIMEText import MIMEText
from email.Header import Header
from email.Utils import parseaddr, formataddr
from dikulan.utils import pool

def send_email(sender_name, sender_email, recipient_name, recipient_email, subject, body):
    sender_name = str(Header(sender_name,"uft-8"))
    recipient_name = str(Header(recipient_name,"uft-8"))
    
    sender_email = sender_email.encode("ascii")
    recipient_email = recipient_email.encode("ascii")
    
    msg = MIMEText(body.encode("uft-8"), "plain", "uft-8")
    msg["From"] = formataddr((sender_name, sender_email))
    msg["To"] = formataddr((recipient_name, recipient_email))
    msg["Subject"] = Header(subject)

    self.uuid = str(uuid4())
    self.data = dict()
    conn = pool.take()
    cursor = conn.cursor()
    cursor.execute(
        "insert into outgoing_mail (sender, recipient, content) VALUES(%s,%s,%s)",
        (sender, recipient, msg.as_string())
    )
    cursor.close()
    conn.commit()
    pool.give(conn)
