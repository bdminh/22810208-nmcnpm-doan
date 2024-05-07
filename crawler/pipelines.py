# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from Models.index import contextModels

class CrawlerPipeline:
    def process_item(self, item, spider):
        result=True
        if item['type'] == 'ahead':
            conferencesIDs = contextModels.conferences.getAll()
            for id in conferencesIDs:
                if item['conference'] == id.conferenceId:
                    result=False
                    break
            if result is True:
                contextModels.conferences.insert(item['conference'],
                                                item['city'], 
                                                item['deadline'], 
                                                item['date'], 
                                                item['notification'], 
                                                item['format_and_comemnt'])
                
        if item['type'] == 'ccf':
            conferencesIDs = contextModels.conferencesCCF.getAll()
            for id in conferencesIDs:
                if item['conference'] == id.conferenceId:
                    result=False
                    break
            if result is True:
                contextModels.conferencesCCF.insert(item['conference'],
                                                    item['description'], 
                                                    item['place'], 
                                                    item['year'], 
                                                    item['date'], 
                                                    item['deadline'], 
                                                    item['timezone'], 
                                                    item['website'], 
                                                    item['note'])
                
        if item['type'] == 'running':
            conferencesRunnningIDs = contextModels.conferencesRunnning.getAll()
            for id in conferencesRunnningIDs:
                if item['conference'] == id.conferenceId:
                    result=False
                    break
            if result is True:
                contextModels.conferencesRunnning.insert(item['conference'],
                                                        item['city'],
                                                        item['date'], 
                                                        item['remark'])
        if item['type'] == 'future':
            conferencesFututeIDs = contextModels.conferencesFutute.getAll()
            for id in conferencesFututeIDs:
                if item['conference'] == id.conferenceId:
                    result=False
                    break
            if result is True:
                contextModels.conferencesFutute.insert(item['conference'],
                                                        item['city'], 
                                                        item['date'], 
                                                        item['notification'], 
                                                        item['final_version'], 
                                                        item['early_registration'],
                                                        item['remark'])
        if item['type'] == 'planning':
            conferencesPlanningIDs = contextModels.conferencesPlanning.getAll()
            for id in conferencesPlanningIDs:
                if item['conference'] == id.conferenceId:
                    result=False
                    break
            if result is True:
                contextModels.conferencesPlanning.insert(item['conference'],
                                                        item['year'], 
                                                        item['city'], 
                                                        item['starting_date'], 
                                                        item['ending_date'],
                                                        item['remark'])
        if item['type'] == 'fullname':
            conferencesDetailsIDs = contextModels.conferencesDetails.getAll()
            for id in conferencesDetailsIDs:
                if item['conference'] == id.conferenceId:
                    result=False
                    break
            if result is True:
                contextModels.conferencesDetails.insert(item['conference'], 
                                                        item['conference_fullname'],
                                                        "")
        return item
