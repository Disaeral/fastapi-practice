from src.api import router
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.core.config import config
from src.infrastructure import ApiAppProvider
from dishka import make_async_container
from dishka.integrations.fastapi import setup_dishka

def init_cors(app: FastAPI) -> None:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

def init_routers(app: FastAPI) -> None:
    app.include_router(router, prefix="/api")

def init_middleware(app: FastAPI) -> None:
    pass

def create_app() -> FastAPI:
    app = FastAPI(
        title="MyApp",
        description="my test api",
        version="1.0.0",
        docs_url=None if config.ENVIRONMENT == "PRODUCTION" else "/docs",
        redoc_url=None if config.ENVIRONMENT == "PRODUCTION" else "/redoc",
        dependencies=[]
    )
    init_routers(app)
    init_cors(app)
    init_middleware(app)
    return app

app = create_app()
container = make_async_container(ApiAppProvider())
setup_dishka(container=container, app=app)

# @app.on_event("shutdown")
# async def shutdown_event():
#     await container.close()