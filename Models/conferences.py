from Models.Base import *

class conferencesModel(Base):
    __tablename__ = "conferences"

    id=Column(Integer, primary_key=True, autoincrement=True)
    conferenceId=Column(String(10), nullable=False)
    city=Column(String(100), nullable=False)
    deadline=Column(String(100), nullable=False)
    date=Column(String(100), nullable=False)
    notification=Column(String(100), nullable=False)
    submission=Column(String(1000), nullable=False)    

    def __init__(self, conferenceId, city, deadline, date, notification, submission):
        self.conferenceId=conferenceId
        self.city=city
        self.deadline=deadline
        self.date=date
        self.notification=notification
        self.submission=submission
