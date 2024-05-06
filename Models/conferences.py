from Models.Base import *

class conferencesModel(Base):
    __tablename__ = "conferences"

    id=Column(Integer, primary_key=True, autoincrement=True)
    conferenceId=Column(String(10), nullable=False)
    city=Column(String(100), nullable=False)
    deadline=Column(String(100), nullable=True)
    date=Column(String(100), nullable=True)
    notification=Column(String(100), nullable=True)
    submission=Column(String(1000), nullable=True)

    def __init__(self, conferenceId, city, deadline, date, notification, submission):
        self.conferenceId=conferenceId
        self.city=city
        self.deadline=deadline
        self.date=date
        self.notification=notification
        self.submission=submission
