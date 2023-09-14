from email.message import EmailMessage
from emailapp import password
import ssl
import smtplib

email_sender = 'alapanelly@gmail.com'
email_reciever = ''
password = password

subject = "God is all it takes"
body = """
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
"""

# Create the instance of EmailMessage
em = EmailMessage
em['From'] = email_sender
em['To'] = email_reciever
em['subject'] = subject
em.set_content(body)

