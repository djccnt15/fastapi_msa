from fastapi import FastAPI
from starlette.responses import PlainTextResponse, RedirectResponse

from src.client import api, config

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

# API Routers
app.include_router(router=api.router, prefix="/api")


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


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        # app="client:app",
        # reload=True,
        app=app,
        host="0.0.0.0",
        port=8080,
        log_config="src/client/resources/log.ini",
    )
