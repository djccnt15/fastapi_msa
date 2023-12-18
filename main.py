from fastapi import FastAPI
from starlette.responses import PlainTextResponse, RedirectResponse

from src.server import config

app = FastAPI(
    title=config.configs("title"),
    version=config.configs("version"),
    contact={
        "name": config.configs("name"),
        "url": config.configs("url"),
        "email": config.configs("email"),
    },
    license_info={
        "name": config.configs("license_name"),
        "url": config.configs("license_url"),
    },
    description=config.description,
    openapi_tags=config.tags_metadata,
)


# default APIs
@app.get("/robots.txt", response_class=PlainTextResponse)
def robots():
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
        app="main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
