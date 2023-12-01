from smtplib import SMTP

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(
	to: str,
	subject: str,
	template: str,
	context: dict[str, str]
):
	try:
		message = MIMEMultipart()
		message['From'] = settings.MAIL_USER
		message['To'] = to
		message['Subject'] = subject

		body = MIMEText("Message de test", 'plain')

		message.attach(body)

		with SMTP(settings.MAIL_HOST, settings.MAIL_PORT) as server:
			server.starttls()
			server.login(settings.MAIL_USER, settings.MAIL_PASSWORD)
			server.send_message(message)

	except Exception as e:
		print(e)
