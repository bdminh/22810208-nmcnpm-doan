import scrapy
from crawler.items import CrawlerPlanningItem

class lixPlanningSpider(scrapy.Spider):
    name='lix-planning-spider'
    start_urls=['https://www.lix.polytechnique.fr/~hermann/conf.php']

    def parse(self, response):
        crawlerItem=CrawlerPlanningItem()
        BODY='tbody tr'
        NEXT_BODY_SELECTOR=' + td'    # trong thẻ tbody
        RESULT='::text'
        RESULT_BODY=' *::text'

        response=response.replace(body=response.body.replace(b'<br>', b' '))

        ######################## Planning ########################
        PLANNING_SELECTOR=f'.central + .conference'
        START=f'{PLANNING_SELECTOR} {BODY}'
        for title in response.css(START):
            START_PLANNING_SELECTOR=f'td'
            crawlerItem['type']='planning'
            crawlerItem['conference']=title.css(START_PLANNING_SELECTOR+RESULT_BODY).extract_first()
            crawlerItem['year']=title.css(START_PLANNING_SELECTOR+NEXT_BODY_SELECTOR+RESULT).extract_first()
            crawlerItem['city']=f'{title.css(START_PLANNING_SELECTOR+NEXT_BODY_SELECTOR*2+RESULT).extract_first()}'
            crawlerItem['starting_date']=f'{title.css(START_PLANNING_SELECTOR+NEXT_BODY_SELECTOR*3+RESULT).extract_first()}'
            crawlerItem['ending_date']=f'{title.css(START_PLANNING_SELECTOR+NEXT_BODY_SELECTOR*4+RESULT).extract_first()}'
            crawlerItem['remark']=f'{title.css(START_PLANNING_SELECTOR+NEXT_BODY_SELECTOR*5+RESULT_BODY).extract()}'.replace('  ', '')\
                                                                                                                    .replace('\'', '')\
                                                                                                                    .replace('[', '')\
                                                                                                                    .replace(']', '')\
                                                                                                                    .replace('\\n', '')\
                                                                                                                    .replace('\\t', '')\
                                                                                                                    .replace(' ,', ',')\
                                                                                                                    .replace('with,', 'with')\
                                                                                                                    .strip()
            yield crawlerItem
