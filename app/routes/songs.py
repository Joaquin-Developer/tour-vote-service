from fastapi import APIRouter

from app.db.database import get_session
from app.models.models import Song
from app.schemas.schemas import Song as SongSchema

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


@router.post("/add_song")
def add_song(name: str, album: str = None, description: str = None):
    """
    Add a new song to the database
    """
    with get_session() as session:
        new_song = Song(
            name=name,
            album=album,
            description=description
        )

        session.add(new_song)
        session.commit()
    return {"message": "Song added successfully"}
