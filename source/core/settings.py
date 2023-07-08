from decouple import config
# from fastapi_mail import ConnectionConfig


class Settings:
    POSTGRES_USER = config('POSTGRES_USER')
    POSTGRES_PASSWORD = config('POSTGRES_PASSWORD')
    POSTGRES_HOST = config('POSTGRES_HOST')
    POSTGRES_DB_NAME = config('POSTGRES_DB_NAME')
    POSTGRES_PORT = config('POSTGRES_PORT')

    DATABASE_URL = \
        f'postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB_NAME}'

    HOST = config('HOST')
    # conf = ConnectionConfig(
    #     MAIL_USERNAME=config('MAIL_USERNAME'),
    #     MAIL_PASSWORD=config('MAIL_PASSWORD'),
    #     MAIL_FROM=config('MAIL_USERNAME'),
    #     MAIL_PORT=587,
    #     MAIL_SERVER=config('EMAIL_SERVER'),
    #     MAIL_STARTTLS=True,
    #     MAIL_SSL_TLS=False,
    #     # USE_CREDENTIALS=Fa,
    #     # TEMPLATE_FOLDER='./templates/email'
    # )


settings = Settings()

