from fastapi_login import LoginManager

secret = "secret"

class NotAuthenticatedException(Exception):
	pass

manager = LoginManager(
	secret,
	"/login",
	use_cookie=True,
	use_header=False,
	custom_exception=NotAuthenticatedException,
)
