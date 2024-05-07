from Models.Base import *

class conferencesCCFModel(Base):
    __tablename__ = "conferencesCCF"

    id=Column(Integer, primary_key=True, autoincrement=True)
    conferenceId=Column(String(10), nullable=False)
    description=Column(String(1000), nullable=True)
    place=Column(String(1000), nullable=True)
    year=Column(String(10), nullable=True)
    date=Column(String(100), nullable=True)
    deadline=Column(String(100), nullable=True)
    timezone=Column(String(10), nullable=True)
    website=Column(String(1000), nullable=True)
    note=Column(String(1000), nullable=True) # abstact deadline or comment 

    def __init__(self, 
                 conferenceId, 
                 description, 
                 place, 
                 year, 
                 date, 
                 deadline, 
                 timezone, 
                 website, 
                 note):
        self.conferenceId=conferenceId
        self.description=description
        self.place=place
        self.year=year
        self.date=date
        self.deadline=deadline
        self.timezone=timezone
        self.website=website
        self.note=note