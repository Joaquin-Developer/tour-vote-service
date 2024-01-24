import logging
from typing import List
from fastapi import APIRouter, HTTPException, Query

from app.db.database import get_session
from app.models.models import Vote, TourEventSongsList


router = APIRouter()


@router.post("/vote")
def vote(mail: str, ticket_id: str, tour_id: str, songs_voted: List[int] = Query(None)):
    """
    Vote for songs in an event
    """

    # Verify if user has already voted for event.
    with get_session() as session:
        existing_vote = session.query(Vote).filter_by(
            mail=mail, ticket_id=ticket_id, tour_id=tour_id
        ).first()

        if existing_vote:
            message = f"User {mail} has alredy voted for song-id/event-id keys"
            logging.warning(message)
            raise HTTPException(status_code=400, detail=message)

        # Insert votes
        # Verify if selected songs are relation in TOUR_EVENT_SONGS_LIST
        valid_songs = session.query(TourEventSongsList).filter(
            TourEventSongsList.tour_id.in_(tour_id),
            TourEventSongsList.song_id.in_(songs_voted)
        ).all()

        valid_song_ids = [song.song_id for song in valid_songs if song.song_id in songs_voted]

        for song_id in valid_song_ids:
            session.add(
                Vote(tour_id=tour_id, son_id=song_id, mail=mail, ticket_id=ticket_id)
            )
        session.commit()
        return {"message": "OK. Votes were recorded"}
