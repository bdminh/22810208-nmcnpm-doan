from Models.conferences import *
from Models.conferencesDetails import *
from Models.conferencesFuture import *
from Models.conferencesPlanning import *
from Models.conferencesRunning import *

# Create the engine and session 
engine = create_engine('sqlite:///Models/qldh.sqlite') 
Session = sessionmaker(bind=engine)
session = Session()

# result = session.query(conferencesModel).all()
# for row in result:
#    print ("ID: ",row.id, "City:",row.city, "Date:",row.date)

class conferences():
   def getAll(self):
      return session.query(conferencesModel).all()
   
   def insert(self, conferenceId, city, deadline, date, notification, submission):
      record = conferencesModel(conferenceId, city, deadline, date, notification, submission)
      result = session.add(record)
      session.commit()
      return result

   def update(self):
      pass

   def delete(self):
      pass

class conferencesDetails():
   def getAll(self):
      return session.query(conferencesDetailsModel).all()
   
   def insert(self, conferenceId, name, website):
      record = conferencesDetailsModel(conferenceId, name, website)
      result = session.add(record)
      session.commit()
      return result

   def update(self):
      pass

   def delete(self):
      pass

class conferencesFutute():
   def getAll(self):
      return session.query(conferencesFutureModel).all()
   
   def insert(self, conferenceId, city, date, notification, finalVersion, earlyRegistration, remarks):
      record = conferencesFutureModel(conferenceId, city, date, notification, finalVersion, earlyRegistration, remarks)
      result = session.add(record)
      session.commit()
      return result

   def update(self):
      pass

   def delete(self):
      pass

class conferencesPlanning():
   def getAll(self):
      return session.query(conferencesPlanningModel).all()
   
   def insert(self, conferenceId, Year, city, startingDate, endingDate, remarks):
      record = conferencesPlanningModel(conferenceId, Year, city, startingDate, endingDate, remarks)
      result = session.add(record)
      session.commit()
      return result

   def update(self):
      pass

   def delete(self):
      pass
   
class conferencesRunnning():
   def getAll(self):
      return session.query(conferencesRunningModel).all()
   
   def insert(self, conferenceId, city, date, remarks):
      record = conferencesRunningModel(conferenceId, city, date, remarks)
      result = session.add(record)
      session.commit()
      return result

   def update(self):
      pass

   def delete(self):
      pass

class Dbcontext():
   conferences=conferences()
   conferencesDetails=conferencesDetails()
   conferencesFutute=conferencesFutute()
   conferencesPlanning=conferencesPlanning()
   conferencesRunnning=conferencesRunnning()

context=Dbcontext()

# result=context.conferences.insert('ICLP', 'Dallas, Texas, USA', 
#                                   '29 April / 6 May 2024 8 July 2024', 
#                                   '11-17 October 2024', 
#                                   '19 June 2024 22 July 2024', 
#                                   'PLP, 14 pages regular; EPTCS, 7 pages short, 3 pages recently published, 3 pages system demonstrations, 3 pages birds of a feather')
# print(result)

# result=context.conferences.getAll()
# for row in result:
#    print ("ID: ",row.id, "City:",row.city, "Date:",row.date)