import scrapy
from crawler.items import CrawlerRunningItem

class lixRunningSpider(scrapy.Spider):
    name='lix-running-spider'
    start_urls=['https://www.lix.polytechnique.fr/~hermann/conf.php']

    def parse(self, response):
        crawlerItem=CrawlerRunningItem()
        ID_LIST=['#ahead', '#running', '#future']
        HEADER='thead tr'
        BODY='tbody tr'
        FOOTER='tfoot tr'
        CONFERENCE_SELECTOR='.navlist + .conference'
        NEXT_BODY_SELECTOR=' + td'    # trong thẻ tbody
        NEXT_BANNER_SELECTOR=' + th'   # BANNER dai dien cho header va footer
        RESULT='::text'
        RESULT_BODY=' *::text'

        response=response.replace(body=response.body.replace(b'<br>', b' '))

        ######################## Runing ########################
        RUNNING_SELECTOR=f'{ID_LIST[1]} + {CONFERENCE_SELECTOR}'

        # header
        for title in response.css(RUNNING_SELECTOR):
            START_RUNNING_SELECTOR=f' {HEADER} th'
            crawlerItem['type']='running'
            crawlerItem['conference']=title.css(START_RUNNING_SELECTOR+RESULT).extract_first()
            crawlerItem['city']=title.css(START_RUNNING_SELECTOR+NEXT_BANNER_SELECTOR+RESULT).extract_first()
            crawlerItem['date']=title.css(START_RUNNING_SELECTOR+NEXT_BANNER_SELECTOR*2+RESULT).extract_first()
            crawlerItem['remark']=title.css(START_RUNNING_SELECTOR+NEXT_BANNER_SELECTOR*3+RESULT).extract_first()
            yield crawlerItem

        # body
        START=f'{RUNNING_SELECTOR} {BODY}'
        for title in response.css(START):
            START_RUNNING_SELECTOR=f'td'
            crawlerItem['type']='running'
            crawlerItem['conference']=title.css(START_RUNNING_SELECTOR+RESULT_BODY).extract_first()
            crawlerItem['city']=title.css(START_RUNNING_SELECTOR+NEXT_BODY_SELECTOR+RESULT).extract_first()
            crawlerItem['date']=title.css(START_RUNNING_SELECTOR+NEXT_BODY_SELECTOR*2+RESULT).extract_first()
            crawlerItem['remark']=title.css(START_RUNNING_SELECTOR+NEXT_BODY_SELECTOR*3+RESULT).extract_first()
            yield crawlerItem

        # footer
        for title in response.css(RUNNING_SELECTOR):
            START_RUNNING_SELECTOR=f'{FOOTER} th'
            crawlerItem['type']='running'
            crawlerItem['conference']=title.css(START_RUNNING_SELECTOR+RESULT).extract_first()
            crawlerItem['city']=title.css(START_RUNNING_SELECTOR+NEXT_BANNER_SELECTOR+RESULT).extract_first()
            crawlerItem['date']=title.css(START_RUNNING_SELECTOR+NEXT_BANNER_SELECTOR*2+RESULT).extract_first()
            crawlerItem['remark']=title.css(START_RUNNING_SELECTOR+NEXT_BANNER_SELECTOR*3+RESULT).extract_first()
            yield crawlerItem