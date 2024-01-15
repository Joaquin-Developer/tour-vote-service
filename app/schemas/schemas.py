from typing import List
from pydantic import BaseModel


class Tour(BaseModel):
    tour_id: int
    tour_show: str
    scenery: str
    place: str
    show_date: str


class Song(BaseModel):
    """Modelo para la tabla all_songs"""
    song_id: int
    name: str
    album: str
    description: str


class EventSong(BaseModel):
    """Modelo para la tabla event_songs"""
    event_id: int
    song_id: int


class Vote(BaseModel):
    """Modelo para la tabla votes"""
    vote_id: int
    event_id: int
    song_id: int
    mail: str
    ticket_id: int


class VoteCreate(BaseModel):
    """Modelo para recibir votos desde los usuarios (en la solicitud)"""
    event_id: int
    song_id: int
    mail: str
    ticket_id: int


# class VoteResponse(BaseModel):
#     """Modelo para la respuesta después de insertar un voto"""
#     vote_id: int


# class TopSongsResponse(BaseModel):
#     """Modelo para la respuesta después de obtener las canciones más votadas"""
#     event_id: int
#     top_songs: List[Song]
