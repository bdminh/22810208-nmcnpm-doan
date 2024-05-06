import scrapy
from crawler.items import CrawlerPlanningItem

class lixPlanningSpider(scrapy.Spider):
    name='lix-planning-spider'
    start_urls=['https://www.lix.polytechnique.fr/~hermann/conf.php']

    def parse(self, response):
        crawlerItem=CrawlerPlanningItem()
        HEADER='thead tr'
        BODY='tbody tr'
        FOOTER='tfoot tr'
        NEXT_BODY_SELECTOR=' + td'    # trong thẻ tbody
        NEXT_BANNER_SELECTOR=' + th'   # BANNER dai dien cho header va footer
        RESULT='::text'
        RESULT_BODY=' *::text'

        response=response.replace(body=response.body.replace(b'<br>', b' '))

        ######################## Planning ########################
        PLANNING_SELECTOR=f'.central + .conference'

        # header
        for title in response.css(PLANNING_SELECTOR):
            START_PLANNING_SELECTOR=f' {HEADER} th'
            crawlerItem['type']='planning'
            crawlerItem['conference']=title.css(START_PLANNING_SELECTOR+RESULT).extract_first()
            crawlerItem['year']=title.css(START_PLANNING_SELECTOR+NEXT_BANNER_SELECTOR+RESULT).extract_first()
            crawlerItem['city']=title.css(START_PLANNING_SELECTOR+NEXT_BANNER_SELECTOR*2+RESULT).extract_first()
            crawlerItem['starting_date']=title.css(START_PLANNING_SELECTOR+NEXT_BANNER_SELECTOR*3+RESULT).extract_first()
            crawlerItem['ending_date']=title.css(START_PLANNING_SELECTOR+NEXT_BANNER_SELECTOR*4+RESULT).extract_first()
            crawlerItem['remark']=title.css(START_PLANNING_SELECTOR+NEXT_BANNER_SELECTOR*5+RESULT).extract_first()
            yield crawlerItem

        # body
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

        # footer
        for title in response.css(PLANNING_SELECTOR):
            START_PLANNING_SELECTOR=f'{FOOTER} th'
            crawlerItem['type']='planning'
            crawlerItem['conference']=title.css(START_PLANNING_SELECTOR+RESULT).extract_first()
            crawlerItem['year']=title.css(START_PLANNING_SELECTOR+NEXT_BANNER_SELECTOR+RESULT).extract_first()
            crawlerItem['city']=title.css(START_PLANNING_SELECTOR+NEXT_BANNER_SELECTOR*2+RESULT).extract_first()
            crawlerItem['starting_date']=title.css(START_PLANNING_SELECTOR+NEXT_BANNER_SELECTOR*3+RESULT).extract_first()
            crawlerItem['ending_date']=title.css(START_PLANNING_SELECTOR+NEXT_BANNER_SELECTOR*4+RESULT).extract_first()
            crawlerItem['remark']=title.css(START_PLANNING_SELECTOR+NEXT_BANNER_SELECTOR*5+RESULT).extract_first()
            yield crawlerItem