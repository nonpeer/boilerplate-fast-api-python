from fastapi import FastAPI

from boilerplate_fastapi.infrastructure.router import health_check_route

app = FastAPI()
app.include_router(health_check_route.router)
