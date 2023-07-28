import uvicorn

from fastapi import FastAPI
from pydantic import BaseModel, Field

from app.helpers import mailer
from app.core.config import settings

app = FastAPI()


class Email(BaseModel):
    token: str
    subject: str
    to: str
    html: str


@app.post("/send")
def send(email: Email):
    if email.token == settings.ACCESS_TOKEN:
        mailer.send(email.subject, email.to, email.html)

        return {'status': True}

    return {'status': False}


uvicorn.run(app, host=settings.HOST, port=settings.PORT)
