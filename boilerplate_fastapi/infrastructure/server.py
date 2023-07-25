from uvicorn import run
from decouple import config


def start_server():
    host = config("HOST", "localhost")
    port = config("PORT", 8080, cast=int)
    run(
        "config.fastapi.config_fastapi:app",
        host=host,
        port=port,
        reload=True,
    )


if __name__ == '__main__':
    start_server()
