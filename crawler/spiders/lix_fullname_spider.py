import scrapy
from crawler.items import CrawlerFullnameItem

class lixFullnameSpider(scrapy.Spider):
    name='lix-fullname-spider'
    start_urls=['https://www.lix.polytechnique.fr/~hermann/conf.php']

    def parse(self, response):
        crawlerItem=CrawlerFullnameItem()
        BODY='tbody tr'
        NEXT_BODY_SELECTOR=' + td'    # trong thẻ tbody
        RESULT='::text'

        response=response.replace(body=response.body.replace(b'<br>', b' '))

        # ######################## Fullname ########################
        FULLNAME_SELECTOR=f'#popup .navlist + .central'
        START=f'{FULLNAME_SELECTOR} {BODY}'
        for title in response.css(START):
            START_FULLNAME_SELECTOR=f'td'
            crawlerItem['type']='fullname'
            crawlerItem['conference']=title.css(START_FULLNAME_SELECTOR+RESULT).extract_first()
            crawlerItem['conference_fullname']=title.css(START_FULLNAME_SELECTOR+NEXT_BODY_SELECTOR+RESULT).extract_first()
            yield crawlerItem