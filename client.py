from fastapi import FastAPI
from starlette.responses import PlainTextResponse, RedirectResponse

from src.client import api, chat, configs

config = configs.config.fastapi

app = FastAPI(**config)

# API Routers
app.include_router(router=api.router)
app.include_router(router=chat.router)


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


if __name__ == "__main__":
    import uvicorn

    config = configs.config.uvicorn

    uvicorn.run(
        # app="client:app",
        # reload=True,
        app=app,
        host=config.host,
        port=config.port,
        log_config=r"src/client/resources/log.ini",
    )
