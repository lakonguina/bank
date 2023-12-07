from pathlib import Path

from emails import Message
from emails.template import JinjaTemplate

from fastapi import (
	HTTPException,
	status,
)

from backoffice.core.settings import settings


def send_email(
	to: str,
	subject: str,
	template: str,
	context: dict[str, str]
):
	try:
		message = Message(
			subject=JinjaTemplate(subject),
			html=JinjaTemplate(template),
			mail_from=(settings.MAIL_NAME, settings.MAIL_USER),
		)

		smtp = {
			"host": settings.MAIL_HOST,
			"port": settings.MAIL_PORT,
			"user": settings.MAIL_USER,
			"password": settings.MAIL_PASSWORD,
			"tls": settings.MAIL_TLS,
		}

		response = message.send(to=to, render=context, smtp=smtp)

	except Exception as error:
		print(error)

		raise HTTPException(
			status_code=500,
			detail="An error as occured while sending the email",
		)


def validate_email(
	to: str,
	url: str,
):
	subject = f"{settings.PROJECT_NAME} - Validate your email"

	with open(Path(settings.TEMPLATES_DIR) / "validate_email.html") as f:
		template_str = f.read()

	send_email(
		to=to,
		subject=subject,
		template=template_str,
		context={"project_name": settings.PROJECT_NAME, "url": url},
	)


def reset_password(
	to: str,
	url: str,
):
	subject = f"{settings.PROJECT_NAME} - Reset your password"

	with open(Path(settings.TEMPLATES_DIR) / "reset_password.html") as f:
		template_str = f.read()

	send_email(
		to=to,
		subject=subject,
		template=template_str,
		context={"project_name": settings.PROJECT_NAME, "url": url},
	)
