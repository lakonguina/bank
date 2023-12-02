from pathlib import Path

from emails import Message
from emails.template import JinjaTemplate

from api.core.settings import settings

def send_email(
	to: str,
	subject: str,
	template: str,
	context: dict[str, str]
):
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
		"tls": False, #TODO: Handle this with env
	}

	response = message.send(to=to, render=context, smtp=smtp)

	print(response)


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
