from fastapi import FastAPI
from starlette.responses import PlainTextResponse, RedirectResponse

from src.server import api, configs, exception

config = configs.config.fastapi

app = FastAPI(
    title=config.title,
    version=config.version,
    contact={
        "name": config.contact.name,
        "url": config.contact.url,
        "email": config.contact.email,
    },
    license_info={
        "name": config.license.name,
        "url": config.license.url,
    },
    description=configs.description,
    openapi_tags=config.tags,
)

# API Routers
app.include_router(router=api.router)

# Exception Handler
exception.add_exception_handlers(app=app)


# default APIs
@app.get("/robots.txt", response_class=PlainTextResponse)
async def robots():
    return "User-agent: *\nDisallow: /"


@app.get("/", response_class=RedirectResponse)
async def root():  # temporal index page redirect to swagger
    return "/docs"


@app.get("/health")
async def helath():
    return 1


@app.get("/ping", response_class=PlainTextResponse)
async def ping():
    return "pong"


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        # app="main:app",
        # reload=True,
        app=app,
        host=configs.config.uvicorn.host,
        port=configs.config.uvicorn.port,
        log_config="src/server/resources/log.ini",
    )
