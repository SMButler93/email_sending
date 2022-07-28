import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

# Create message:
message = Template(Path("""Path for email text here""").read_text())
# set-up email object:
email = EmailMessage()
email['from'] = """Senders email here"""
email['to'] = """Recipients email here"""
email['subject'] = """Email subject here"""

# set the content of email:
# Second argument 'file type' needed if not text file.
# substitute method allows us to personalise messages like a mail merge would.
email.set_content(message.substitute("""subs"""), """File type""")

# set-up the smtp.
with smtplib.SMTP(host="""host smtp code""", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()  # encode
    smtp.login("""Sender email""", """email password""")
    smtp.send_message(email)

print("Email sent.")
