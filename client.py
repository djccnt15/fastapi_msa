from fastapi import FastAPI

from src.client import configs
from src.client.route import api, chat, default

config = configs.config.fastapi

app = FastAPI(**config)

# API Routers
app.include_router(router=default.router)
app.include_router(router=api.router)
app.include_router(router=chat.router)


if __name__ == "__main__":
    import uvicorn

    uvicorn_config = configs.config.uvicorn

    uvicorn.run(
        # app="client:app",  # use this line when reload config is true
        app=app,
        **uvicorn_config
    )
