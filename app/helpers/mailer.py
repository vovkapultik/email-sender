import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from app.core.config import settings
from app.helpers.logger import log


def send(subject: str, to: str, html: str):
    content = MIMEText(html, 'html')

    message = MIMEMultipart()
    message['From'] = settings.SENDER_EMAIL_ADDRESS
    message['To'] = to
    message['Subject'] = subject

    message.attach(content)

    session = smtplib.SMTP(settings.SMTP_SERVER_HOST, settings.SMTP_SERVER_PORT)
    session.starttls()
    session.login(settings.SENDER_EMAIL_ADDRESS, settings.SENDER_EMAIL_PASSWORD)

    session.sendmail(settings.SENDER_EMAIL_ADDRESS, to, message.as_string())
    session.quit()
    
    log.info(f'e-mail to {to} sent')
