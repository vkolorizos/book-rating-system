import logging
import sys
import os
import uvicorn
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware
from fastapi.middleware.cors import CORSMiddleware
from uvicorn.config import LOGGING_CONFIG
from settings import config
from routers import books

logger = logging.getLogger(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = FastAPI(title=config.title, version=config.version)


@app.get('/')
async def root():
    return  {
        'name': config.title,
        'version': config.version
    }

app.include_router(books.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=config.origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])


if __name__ == "__main__":
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)
    LOGGING_CONFIG['loggers'] = {'root': {"handlers": ["default"], "level": "INFO"}}

    uvicorn.run("main:app", host="0.0.0.0", port=22000, use_colors=True, reload=True, debug=True, log_level='info',
                log_config=LOGGING_CONFIG)
