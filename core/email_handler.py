# core/email_handler.py
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import imaplib
import email

class EmailSender:
    def __init__(self, smtp_server, port, email, password):
        self.smtp = smtplib.SMTP(smtp_server, port)
        self.smtp.starttls()
        self.smtp.login(email, password)
        self.email = email  # Armazena o e-mail do remetente

    def send(self, to, subject, body):
        msg = MIMEMultipart()
        msg['From'] = self.email
        msg['To'] = to
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        self.smtp.send_message(msg)
        print("E-mail enviado!")

class EmailReader:
    def __init__(self, imap_server, email, password):
        self.mail = imaplib.IMAP4_SSL(imap_server)
        self.mail.login(email, password)
    
    def get_unread(self, limit=5):
        self.mail.select("inbox")
        _, msgnums = self.mail.search(None, "UNSEEN")
        emails = []
        for num in msgnums[0].split()[:limit]:
            _, data = self.mail.fetch(num, "(RFC822)")
            raw_email = data[0][1]
            msg = email.message_from_bytes(raw_email)
            emails.append({
                "subject": msg["subject"],
                "from": msg["from"]
            })
        return emails
