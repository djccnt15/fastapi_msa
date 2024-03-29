from fastapi import FastAPI

from src.server import configs
from src.server.common.exception import handlers as exception_handler
from src.server.route import api as api_router
from src.server.route import default as default_router

config = configs.config.fastapi

app = FastAPI(**config)

# API Routers
app.include_router(router=default_router.router)
app.include_router(router=api_router.router)

# Exception Handler
exception_handler.add_handlers(app=app)

if __name__ == "__main__":
    import uvicorn

    config = configs.config.uvicorn

    uvicorn.run(
        # app="main:app",
        # reload=True,
        app=app,
        host=config.host,
        port=config.port,
        log_config=r"src/server/resources/log.ini",
    )
