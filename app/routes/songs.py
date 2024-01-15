from fastapi import APIRouter

from app.db.database import get_session
from app.models.models import Song

router = APIRouter()


@router.get("/")
def get_all_songs():
    """
    Get all songs
    """
    with get_session() as session:
        results = session.query(Song)

    return [
        dict(zip(row._mapping.keys(), row))
        for row in results
    ]
