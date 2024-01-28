from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.routes.songs import router as songs_router
from app.routes.tour_event_songs_list import router as TESL_router
from app.routes.vote import router as vote_router
from app import utils


app = FastAPI(title=settings.APP_NAME)


app.add_middleware(
    CORSMiddleware,
    # allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


utils.set_logging()

app.include_router(songs_router, prefix=settings.API_V1_STR + "/all_songs")
app.include_router(TESL_router, prefix=settings.API_V1_STR + "/event_songs_list")
app.include_router(vote_router, prefix=settings.API_V1_STR + "/vote")
