import os
import pandas as pd

from Models.index import contextModels

class Controller():
    def getDataCCF(self):
        kq=[['Conference', 
            'Description', 
            'Place', 
            'Year', 
            'Date', 
            'Deadline', 
            'Timezone', 
            'Website',
            'Note']]
        
        result=contextModels.conferencesCCF.getAll()
        for record in result:
            kq.append([record.conferenceId, 
                       record.description, 
                       record.place, 
                       record.year, 
                       record.date, 
                       record.deadline, 
                       record.timezone, 
                       record.website, 
                       record.note])
        return kq

    def getDataLixAhead(self):
        kq=[['Conference', 
            'City', 
            'Deadline',
            'Date', 
            'Notification', 
            'Submission'
            ]]
        
        result=contextModels.conferences.getAll()
        for record in result:
            kq.append([record.conferenceId, 
                       record.city, 
                       record.deadline, 
                       record.date, 
                       record.notification, 
                       record.submission
                       ])
        return kq

    def getDataLixFuture(self):
        kq=[['Conference', 
            'City',
            'Date', 
            'Notification', 
            'Final Version',
            'Early Registration',
            'Remarks'
            ]]
        
        result=contextModels.conferencesFutute.getAll()
        for record in result:
            kq.append([record.conferenceId, 
                       record.city,
                       record.date, 
                       record.notification,
                       record.finalVersion,
                       record.earlyRegistration, 
                       record.remarks
                       ])
        return kq

    def getDataLixPlanning(self):
        kq=[['Conference', 
            'Year',
            'City', 
            'Starting Date', 
            'Ending Date',
            'Remarks'
            ]]
        
        result=contextModels.conferencesPlanning.getAll()
        for record in result:
            kq.append([record.conferenceId, 
                       record.Year,
                       record.city, 
                       record.startingDate,
                       record.endingDate, 
                       record.remarks
                       ])
        return kq
    
    def getDataLixRunning(self):
        kq=[['Conference',
            'City', 
            'Date',
            'Remarks'
            ]]
        
        result=contextModels.conferencesRunnning.getAll()
        for record in result:
            kq.append([record.conferenceId,
                       record.city, 
                       record.date,
                       record.remarks
                       ])
        return kq

    def getFullname(self, keyword):
        records=contextModels.conferencesDetails.getAll()
        for record in records:
            if record.conferenceId == keyword:
                return record
        return []

    def searchConference(self, keyword):
        pass

    def updateDataCCF(self):
        # delete database first
        contextModels.conferencesCCF.deleteAll()

        # run command
        cmd = "scrapy crawl ccf-spider"
        returned_value = os.system(cmd)  # returns the exit code in unix
        return returned_value

    def updateDataLix(self):
        # delete database first
        contextModels.conferences.deleteAll()
        contextModels.conferencesDetails.deleteAll()
        contextModels.conferencesFutute.deleteAll()
        contextModels.conferencesPlanning.deleteAll()
        contextModels.conferencesRunnning.deleteAll()

        # run command
        cmd = "scrapy crawl lix-ahead-spider"
        returned_value = os.system(cmd)  # returns the exit code in unix
        
        cmd = "scrapy crawl lix-fullname-spider"
        returned_value = os.system(cmd)  # returns the exit code in unix

        cmd = "scrapy crawl lix-future-spider"
        returned_value = os.system(cmd)  # returns the exit code in unix

        cmd = "scrapy crawl lix-planning-spider"
        returned_value = os.system(cmd)  # returns the exit code in unix

        cmd = "scrapy crawl lix-running-spider"
        returned_value = os.system(cmd)  # returns the exit code in unix
        
        return 'OK'

    def exportDataCCF(self):
        kq={'Conference': [],
            'Description': [],
            'Place': [],
            'Year': [], 
            'Date': [], 
            'Deadline': [], 
            'Timezone': [], 
            'Website': [],
            'Note': []
            }
        
        result=contextModels.conferencesCCF.getAll()
        for record in result:
            kq['Conference'].append(record.conferenceId)
            kq['Description'].append(record.description)
            kq['Place'].append(record.place)
            kq['Year'].append(record.year)
            kq['Date'].append(record.date)
            kq['Deadline'].append(record.deadline)
            kq['Timezone'].append(record.timezone)
            kq['Website'].append(record.website)
            kq['Note'].append(record.note)

        data = pd.DataFrame(kq)

        # writing to Excel
        datatoexcel = pd.ExcelWriter('Reports/CCF.xlsx')
        
        # write DataFrame to excel
        data.to_excel(datatoexcel)
        
        # save the excel
        datatoexcel.close()

        return 'OK'

    def exportDataLixAhead(self):
        kq={'Conference': [],
            'City': [],
            'Deadline': [],
            'Date': [], 
            'Notification': [], 
            'Submission': []
            }
        
        result=contextModels.conferences.getAll()
        for record in result:
            kq['Conference'].append(record.conferenceId)
            kq['City'].append(record.city)
            kq['Deadline'].append(record.deadline)
            kq['Date'].append(record.date)
            kq['Notification'].append(record.notification)
            kq['Submission'].append(record.submission)

        data = pd.DataFrame(kq)

        # writing to Excel
        datatoexcel = pd.ExcelWriter('Reports/LIX-AheadConference.xlsx')
        
        # write DataFrame to excel
        data.to_excel(datatoexcel)
        
        # save the excel
        datatoexcel.close()

        return 'OK'

    def exportDataLixFuture(self):
        kq={'Conference': [],
            'City': [],
            'Date': [],
            'Notification': [], 
            'Final Version': [], 
            'Early Registration': [],
            'Remarks': []
            }
        
        result=contextModels.conferencesFutute.getAll()
        for record in result:
            kq['Conference'].append(record.conferenceId)
            kq['City'].append(record.city)
            kq['Date'].append(record.date)
            kq['Notification'].append(record.notification)
            kq['Final Version'].append(record.finalVersion)
            kq['Early Registration'].append(record.earlyRegistration)
            kq['Remarks'].append(record.remarks)

        data = pd.DataFrame(kq)

        # writing to Excel
        datatoexcel = pd.ExcelWriter('Reports/LIX-FutureConference.xlsx')
        
        # write DataFrame to excel
        data.to_excel(datatoexcel)
        
        # save the excel
        datatoexcel.close()

        return 'OK'

    def exportDataLixPlanning(self):
        kq={'Conference': [],
            'Year': [],
            'City': [],
            'Starting Date': [], 
            'Ending Date': [], 
            'Remarks': []
            }
        
        result=contextModels.conferencesPlanning.getAll()
        for record in result:
            kq['Conference'].append(record.conferenceId)
            kq['Year'].append(record.Year)
            kq['City'].append(record.city)
            kq['Starting Date'].append(record.startingDate)
            kq['Ending Date'].append(record.endingDate)
            kq['Remarks'].append(record.remarks)

        data = pd.DataFrame(kq)

        # writing to Excel
        datatoexcel = pd.ExcelWriter('Reports/LIX-PlanningConference.xlsx')
        
        # write DataFrame to excel
        data.to_excel(datatoexcel)
        
        # save the excel
        datatoexcel.close()

        return 'OK'

    def exportDataLixRunning(self):
        kq={'Conference': [],
            'City': [],
            'Date': [],
            'Remarks': []
            }
        
        result=contextModels.conferencesRunnning.getAll()
        for record in result:
            kq['Conference'].append(record.conferenceId)
            kq['City'].append(record.city)
            kq['Date'].append(record.date)
            kq['Remarks'].append(record.remarks)

        data = pd.DataFrame(kq)

        # writing to Excel
        datatoexcel = pd.ExcelWriter('Reports/LIX-RunningConference.xlsx')
        
        # write DataFrame to excel
        data.to_excel(datatoexcel)
        
        # save the excel
        datatoexcel.close()

        return 'OK'

controller=Controller()


