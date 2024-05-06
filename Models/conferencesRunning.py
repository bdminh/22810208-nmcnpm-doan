from Models.Base import *

class conferencesRunningModel(Base):
    __tablename__ = "conferencesRunning"

    id=Column(Integer, primary_key=True, autoincrement=True)
    conferenceId=Column(String(10), nullable=False)
    city=Column(String(100), nullable=False)
    date=Column(String(100), nullable=False)
    remarks=Column(String(100), nullable=False) 

    def __init__(self, conferenceId, city, date, remarks):
        self.conferenceId=conferenceId
        self.city=city
        self.date=date
        self.remarks=remarks