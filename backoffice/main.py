from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles

from backoffice.routes import user
from backoffice.routes import auth
from backoffice.core.manager import manager, NotAuthenticatedException


api = FastAPI(
    title="Bank",
    description="Bank helps you do awesome stuff.",
    version="0.0.1",
    terms_of_service="http://example.com/",
    contact={
        "name": "Bank",
        "url": "http://example.com/",
        "email": "dp@x-force.example.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
	redoc_url=None,
)

api.include_router(user.router)
api.include_router(auth.router)

api.mount("/static", StaticFiles(directory="backoffice/static"), name="static")

@api.exception_handler(NotAuthenticatedException)
def auth_exception_handler(request: Request, exc: NotAuthenticatedException):
    """
    Redirect the user to the login page if not logged in
    """
    return RedirectResponse(url='/')

manager.useRequest(api)
