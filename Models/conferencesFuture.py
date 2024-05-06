from Models.Base import *

class conferencesFutureModel(Base):
    __tablename__ = "conferencesFuture"

    id=Column(Integer, primary_key=True, autoincrement=True)
    conferenceId=Column(String(10), nullable=False)
    city=Column(String(100), nullable=False)
    date=Column(String(100), nullable=True)
    notification=Column(String(100), nullable=True)
    finalVersion=Column(String(1000), nullable=True)    
    earlyRegistration=Column(String(100), nullable=True)
    remarks=Column(String(100), nullable=True)

    def __init__(self, conferenceId, city, date, notification, finalVersion, earlyRegistration, remarks):
        self.conferenceId=conferenceId
        self.city=city
        self.date=date
        self.notification=notification
        self.finalVersion=finalVersion
        self.earlyRegistration=earlyRegistration
        self.remarks=remarks