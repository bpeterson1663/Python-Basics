import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Brady Peterson'
email['to'] = 'bpeterson1663@gmail.com'
email['subject'] = 'You won!'

email.set_content(html.substitute({"name": "Tin Tin"}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('bpeterson1660@gmail.com', '')
    smtp.send_message(email)
    print('all good')
