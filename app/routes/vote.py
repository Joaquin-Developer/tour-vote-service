import logging
from typing import List
from fastapi import APIRouter, HTTPException, Query

from app.db.database import get_session
from app.models.models import Vote, TourEventSongsList


router = APIRouter()


@router.post("/vote")
def vote(mail: str, ticket_id: str, tour_id: str, songs_voted: List[int] = Query(None)):
    """
    Vote for songs in a event
    """

    # Verify if user has alredy voted for event.
    with get_session() as session:
        existing_vote = session.query(Vote).filter_by(
            mail=mail, ticket_id=ticket_id, tour_id=tour_id
        ).first()

        if existing_vote:
            message = f"User {mail} has alredy voted for song-id/event-id keys"
            logging.warning(message)
            raise HTTPException(status_code=400, detail=message)

    # Insert votes

    # Verify if selected songs are relationed in TOUR_EVENT_SONGS_LIST
    with get_session() as session:
        valid_songs = session.query(TourEventSongsList).filter(
            TourEventSongsList.tour_id.in_(tour_id),
            TourEventSongsList.song_id.in_(songs_voted)
        ).all()

        for _vote in valid_songs:
            pass
