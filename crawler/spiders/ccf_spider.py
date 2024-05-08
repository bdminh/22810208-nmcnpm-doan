# https://ccfddl.github.io/conference/allconf.yml

# performing a scrapy request to get the data from the website 
import scrapy
import yaml
import json
from crawler.items import CrawlerCCFItem

class CCFSpider(scrapy.Spider):
    name = 'ccf-spider'
     
    def start_requests(self):
        yield scrapy.Request(url='https://ccfddl.github.io/conference/allconf.yml', callback=self.parse)
     
    def parse(self, response):
        crawlerItem=CrawlerCCFItem()

        # Process the response here
        with open('dest.yml', 'wb') as file:
            #dict = yaml.safe_load_all(response.body)
            file.write(response.body)

        with open("dest.yml", 'r') as yaml_in, open("dest.json", "w") as json_out:
            yaml_object = yaml.safe_load(yaml_in) # yaml_object will be a list or a dict
            json.dump(yaml_object, json_out)

        # Get json data from file (this mean data will have dictionary type)
        with open("dest.json", "rb") as json_out:
            data = json.load(json_out)
            for conference in data:
                crawlerItem['type']='ccf'
                crawlerItem['conference']=conference['title']
                crawlerItem['description']=conference['description']
                confs=conference['confs'][-1]
                crawlerItem['place']=confs['place']
                crawlerItem['year']=confs['year']
                crawlerItem['date']=confs['date']
                crawlerItem['deadline']=confs['timeline'][-1]['deadline']
                crawlerItem['timezone']=confs['timezone']
                crawlerItem['website']=confs['link']

                # abstact deadline or comment
                lastTimeLine=confs['timeline'][-1]
                if 'abstract_deadline' in lastTimeLine: 
                    crawlerItem['note']=lastTimeLine['abstract_deadline']  
                elif 'comment' in lastTimeLine :
                    crawlerItem['note']=lastTimeLine['comment']
                else:
                    crawlerItem['note']=""
                yield crawlerItem

        # # Process the response here
        # with open('source.txt', 'wb') as file:
        #     #dict = yaml.safe_load_all(response.body)
        #     file.write(response.body)

        # with open("source.txt", "rb") as source, open("dest.yml", "wb") as dest:
        #     dest.write(source.read())

        #print(response.body)


















