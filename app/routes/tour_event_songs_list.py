from fastapi import APIRouter, HTTPException

from app.db.database import get_session
from app.models.models import TourEventSongsList
from app.models.models import Song

router = APIRouter()


@router.post("/add")
def add(tour_id: int, song_id: int):
    """
    Add a new tour event song to the database
    """
    with get_session() as session:
        # verify if relationship exists
        existing_relation = session.query(TourEventSongsList).filter_by(
            tour_id=tour_id,
            song_id=song_id
        ).first()

        if existing_relation:
            raise HTTPException(status_code=400, detail="The relationship alredy exists.")

        # create new relation and insert in db
        new_relation = TourEventSongsList(
            tour_id=tour_id,
            song_id=song_id
        )
        session.add(new_relation)
        session.commit()

    return {"message": "OK. Data added successfully"}


@router.post("/enable-all")
def enable_all_songs_for_event(tour_id: int):
    """
    Enable all songs for a specific event by adding them to TOUR_EVENT_SONGS_LIST
    """
    with get_session() as session:
        all_songs = session.query(Song).all()

        for song in all_songs:
            # verify if relationship alredy exists
            existing_relation = session.query(TourEventSongsList).filter_by(
                tour_id=tour_id,
                song_id=song.song_id
            ).first()

            if not existing_relation:
                new_relation = TourEventSongsList(
                    tour_id=tour_id,
                    song_id=song.song_id
                )
                session.add(new_relation)

        session.commit()

    return {"message": "OK. All songs are enabled."}


@router.post("/disable-all")
def disable_all_songs_for_event(tour_id: int):
    """
    Disable all songs for a specific event by removing them from TOUR_EVENT_SONGS_LIST
    """
    with get_session() as session:
        # Get all songs from tour_id
        relations_to_delete = session.query(TourEventSongsList).filter_by(
            tour_id=tour_id
        ).all()

        for relation in relations_to_delete:
            session.delete(relation)

        session.commit()

    return {"message": "OK. All songs are disabled."}
