from fastapi import FastAPI

from src.server import configs
from src.server.core.exception import handlers as exception_handler
from src.server.route import api, default

config = configs.config.fastapi

app = FastAPI(**config)

# API Routers
app.include_router(router=default.router)
app.include_router(router=api.router)

# Exception Handler
exception_handler.add_handlers(app=app)

if __name__ == "__main__":
    import uvicorn

    uvicorn_config = configs.config.uvicorn

    uvicorn.run(
        # app="main:app",  # use this line when reload config is true
        app=app,
        **uvicorn_config
    )
