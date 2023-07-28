from pydantic import BaseSettings


class Settings(BaseSettings):
    HOST: str
    PORT: int
    
    ACCESS_TOKEN: str
    
    SENDER_EMAIL_ADDRESS: str
    SENDER_EMAIL_PASSWORD: str

    SMTP_SERVER_HOST: str
    SMTP_SERVER_PORT: int

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()
