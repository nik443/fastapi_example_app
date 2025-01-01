from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from app.api import router as api_router
from app.core.config import settings
from app.core.models.db_helper import db_helper


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup - часть генератора, отвечающая за действия при запуске приложения
    yield
    # shutdown - часть генератора, отвечающая за действия при остановке приложения
    print("dispose engine")
    await db_helper.dispose()


main_app = FastAPI(lifespan=lifespan)
main_app.include_router(router=api_router, prefix=settings.api.prefix)

if __name__ == "__main__":
    uvicorn.run(
        app="main:main_app",
        reload=True,
        host=settings.run.host,
        port=settings.run.port,
    )
