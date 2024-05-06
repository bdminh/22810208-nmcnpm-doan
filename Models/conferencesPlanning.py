from Models.Base import *

class conferencesPlanningModel(Base):
    __tablename__ = "conferencesPlanning"

    id=Column(Integer, primary_key=True, autoincrement=True)
    conferenceId=Column(String(10), nullable=False)
    Year=Column(Integer, nullable=False)
    city=Column(String(100), nullable=False)
    startingDate=Column(String(100), nullable=True)
    endingDate=Column(String(100), nullable=True)
    remarks=Column(String(100), nullable=True)

    def __init__(self, conferenceId, Year, city, startingDate, endingDate, remarks):
        self.conferenceId=conferenceId
        self.Year=Year
        self.city=city
        self.startingDate=startingDate
        self.endingDate=endingDate
        self.remarks=remarks