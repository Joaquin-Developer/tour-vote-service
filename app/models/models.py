from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class Tour(Base):
    __tablename__ = "TOUR"

    tour_id = Column(Integer, primary_key=True, index=True)
    tour_show = Column(String(250), index=True)
    scenery = Column(String(250), index=True)
    place = Column(String(150), index=True)
    show_date = Column(String, index=True)

    songs = relationship("TourEventSongsList", back_populates="tour")


class Song(Base):
    __tablename__ = "ALL_SONGS"

    song_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), index=True)
    album = Column(String(200))
    description = Column(String(300))

    tour_songs = relationship("TourEventSongsList", back_populates="song")
    # votes = relationship("Vote", back_populates="song")


class TourEventSongsList(Base):
    __tablename__ = "TOUR_EVENT_SONGS_LIST"

    tour_id = Column(Integer, ForeignKey("TOUR.tour_id"), primary_key=True, index=True)
    song_id = Column(Integer, ForeignKey("ALL_SONGS.song_id"), primary_key=True, index=True)

    tour = relationship("Tour", back_populates="songs")
    song = relationship("Song", back_populates="tour_songs")


class Vote(Base):
    __tablename__ = "VOTES"

    vote_id = Column(Integer, primary_key=True, index=True)
    tour_id = Column(Integer, ForeignKey("TOUR.tour_id"), index=True)
    song_id = Column(Integer, ForeignKey("ALL_SONGS.song_id"), index=True)
    mail = Column(String(100), index=True)
    ticket_id = Column(String(100), index=True)

    # tour = relationship("Tour", back_populates="votes")
    # song = relationship("Song", back_populates="votes")
