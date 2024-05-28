import os
import pandas as pd

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from Models.index import contextModels
from crawler.spiders.ccf_spider import CCFSpider
from crawler.spiders.lix_ahead_spider import lixAheadSpider
from crawler.spiders.lix_fullname_spider import lixFullnameSpider
from crawler.spiders.lix_future_spider import lixFutureSpider
from crawler.spiders.lix_planning_spider import lixPlanningSpider
from crawler.spiders.lix_running_spider import lixRunningSpider

class Controller():
    def __init__(self):
        self.path=os.path.dirname(os.path.abspath(__file__)).replace('Controller', '')

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
        kq=[['Conference', 
             'Fullname'
             ]]

        result=contextModels.conferencesDetails.getByID(keyword)

        for i in result:
            kq.append([i.conferenceId, 
                       i.name
                       ])
        return kq

    def searchHeadConference(self, keyword):
        kq=[['Conference', 
            'City', 
            'Deadline',
            'Date', 
            'Notification', 
            'Submission']]

        records = contextModels.conferences.getByID(keyword)
        for i in records:
            kq.append([i.conferenceId, i.city, i.deadline, i.date, i.notification, i.submission])

        records = contextModels.conferences.getByCity(keyword)
        for i in records:
            kq.append([i.conferenceId, i.city, i.deadline, i.date, i.notification, i.submission])

        records = contextModels.conferences.getByDeadline(keyword)
        for i in records:
            kq.append([i.conferenceId, i.city, i.deadline, i.date, i.notification, i.submission])
        
        new_kq = []
        for elem in kq:
            if elem not in new_kq:
                new_kq.append(elem)
                
        return new_kq
    
    def searchCCFConference(self, keyword):
        kq=[['Conference', 
            'Description', 
            'Place', 
            'Year', 
            'Date', 
            'Deadline', 
            'Timezone', 
            'Website', 
            'Note']]

        records = contextModels.conferencesCCF.getByID(keyword)
        for i in records:
            kq.append([i.conferenceId, 
                       i.description, 
                       i.place, 
                       i.year, 
                       i.date, 
                       i.deadline, 
                       i.timezone, 
                       i.timezone, 
                       i.note])

        records = contextModels.conferencesCCF.getByCity(keyword)
        for i in records:
            kq.append([i.conferenceId, 
                       i.description, 
                       i.place, 
                       i.year, 
                       i.date, 
                       i.deadline, 
                       i.timezone, 
                       i.timezone, 
                       i.note])

        records = contextModels.conferencesCCF.getByDeadline(keyword)
        for i in records:
            kq.append([i.conferenceId, 
                       i.description, 
                       i.place, 
                       i.year, 
                       i.date, 
                       i.deadline, 
                       i.timezone, 
                       i.timezone, 
                       i.note])
        
        new_kq = []
        for elem in kq:
            if elem not in new_kq:
                new_kq.append(elem)
                
        return new_kq

    def searchFutureConference(self, keyword):
        kq=[['Conference', 
              'City', 
              'Date', 
              'Notification', 
              'Final Version', 
              'Early Registration', 
              'Remarks']]

        records = contextModels.conferencesFutute.getByID(keyword)
        for i in records:
            kq.append([i.conferenceId, 
                       i.city, 
                       i.date, 
                       i.notification, 
                       i.finalVersion, 
                       i.earlyRegistration, 
                       i.remarks])

        records = contextModels.conferencesFutute.getByCity(keyword)
        for i in records:
            kq.append([i.conferenceId, 
                       i.city, 
                       i.date, 
                       i.notification, 
                       i.finalVersion, 
                       i.earlyRegistration, 
                       i.remarks])

        records = contextModels.conferencesFutute.getByDeadline(keyword)
        for i in records:
            kq.append([i.conferenceId, 
                       i.city, 
                       i.date, 
                       i.notification, 
                       i.finalVersion, 
                       i.earlyRegistration, 
                       i.remarks])
        
        new_kq = []
        for elem in kq:
            if elem not in new_kq:
                new_kq.append(elem)
                
        return new_kq

    def searchPlanningConference(self, keyword):
        kq=[['Conference', 
              'Year', 
              'City', 
              'Starting Date', 
              'Ending Date',
              'Remarks']]

        records = contextModels.conferencesPlanning.getByID(keyword)
        for i in records:
            kq.append([i.conferenceId, 
                       i.Year, 
                       i.city, 
                       i.startingDate, 
                       i.endingDate, 
                       i.remarks])

        records = contextModels.conferencesPlanning.getByCity(keyword)
        for i in records:
            kq.append([i.conferenceId, 
                       i.Year, 
                       i.city, 
                       i.startingDate, 
                       i.endingDate, 
                       i.remarks])

        records = contextModels.conferencesPlanning.getByDeadline(keyword)
        for i in records:
            kq.append([i.conferenceId, 
                       i.Year, 
                       i.city, 
                       i.startingDate, 
                       i.endingDate, 
                       i.remarks])
        
        new_kq = []
        for elem in kq:
            if elem not in new_kq:
                new_kq.append(elem)
                
        return new_kq

    def searchRunningConference(self, keyword):
        kq=[['Conference', 
             'City', 
             'Date',
             'Remarks'
             ]]

        records = contextModels.conferencesRunnning.getByID(keyword)
        for i in records:
            kq.append([i.conferenceId,
                       i.city, 
                       i.date,
                       i.remarks])

        records = contextModels.conferencesRunnning.getByCity(keyword)
        for i in records:
            kq.append([i.conferenceId,
                       i.city, 
                       i.date,
                       i.remarks])

        records = contextModels.conferencesRunnning.getByDeadline(keyword)
        for i in records:
            kq.append([i.conferenceId,
                       i.city, 
                       i.date,
                       i.remarks])
        
        new_kq = []
        for elem in kq:
            if elem not in new_kq:
                new_kq.append(elem)
                
        return new_kq

    def updateDataCCF(self):
        # delete database first
        contextModels.conferencesCCF.deleteAll()

        settings=get_project_settings()
        process=CrawlerProcess(settings)

        # run command
        process.crawl(CCFSpider)
        process.start()

        return 'Updated completely'

    def updateDataLix(self):
        # delete database first
        contextModels.conferences.deleteAll()
        contextModels.conferencesDetails.deleteAll()
        contextModels.conferencesFutute.deleteAll()
        contextModels.conferencesPlanning.deleteAll()
        contextModels.conferencesRunnning.deleteAll()

        settings=get_project_settings()
        process=CrawlerProcess(settings)

        # run command
        process.crawl(lixAheadSpider)
        process.crawl(lixFullnameSpider)
        process.crawl(lixFutureSpider)
        process.crawl(lixPlanningSpider)
        process.crawl(lixRunningSpider)
        process.start()  

        return 'Updated completely'

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
        datatoexcel = pd.ExcelWriter(f'{self.path}\\Reports\\/CCF.xlsx')
        
        # write DataFrame to excel
        data.to_excel(datatoexcel)
        
        # save the excel
        datatoexcel.close()

        return 'Exported completely'

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
        datatoexcel = pd.ExcelWriter(f'{self.path}\\Reports\\LIX-AheadConference.xlsx')
        
        # write DataFrame to excel
        data.to_excel(datatoexcel)
        
        # save the excel
        datatoexcel.close()

        return 'Exported completely'

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
        datatoexcel = pd.ExcelWriter(f'{self.path}\\Reports\\LIX-FutureConference.xlsx')
        
        # write DataFrame to excel
        data.to_excel(datatoexcel)
        
        # save the excel
        datatoexcel.close()

        return 'Exported completely'

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
        datatoexcel = pd.ExcelWriter(f'{self.path}\\Reports\\LIX-PlanningConference.xlsx')
        
        # write DataFrame to excel
        data.to_excel(datatoexcel)
        
        # save the excel
        datatoexcel.close()

        return 'Exported completely'

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
        datatoexcel = pd.ExcelWriter(f'{self.path}\\Reports\\LIX-RunningConference.xlsx')
        
        # write DataFrame to excel
        data.to_excel(datatoexcel)
        
        # save the excel
        datatoexcel.close()

        return 'Exported completely'

controller=Controller()


