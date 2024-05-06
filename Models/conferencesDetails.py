from Models.Base import *

class conferencesDetailsModel(Base):
    __tablename__ = "conferencesDetails"

    id=Column(Integer, primary_key=True, autoincrement=True)
    conferenceId=Column(String(10), nullable=False)
    name=Column(String(100), nullable=False)
    website=Column(String(100), nullable=False)

    def __init__(self, conferenceId, name, website):
        self.conferenceId=conferenceId
        self.name=name
        self.website=website