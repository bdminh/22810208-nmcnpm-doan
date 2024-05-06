import scrapy
from crawler.items import CrawlerFutureItem

class lixFutureSpider(scrapy.Spider):
    name='lix-future-spider'
    start_urls=['https://www.lix.polytechnique.fr/~hermann/conf.php']

    def parse(self, response):
        crawlerItem=CrawlerFutureItem()
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

        ######################## Future ########################
        FUTURE_SELECTOR=f'{ID_LIST[2]} + {CONFERENCE_SELECTOR}'

        # header
        for title in response.css(FUTURE_SELECTOR):
            START_FUTURE_SELECTOR=f' {HEADER} th'  
            crawlerItem['type']='future'
            crawlerItem['conference']=title.css(START_FUTURE_SELECTOR+RESULT).extract_first()
            crawlerItem['city']=title.css(START_FUTURE_SELECTOR+NEXT_BANNER_SELECTOR+RESULT).extract_first()
            crawlerItem['date']=title.css(START_FUTURE_SELECTOR+NEXT_BANNER_SELECTOR*2+RESULT).extract_first()
            crawlerItem['notification']=title.css(START_FUTURE_SELECTOR+NEXT_BANNER_SELECTOR*3+RESULT).extract_first()
            crawlerItem['final_version']=title.css(START_FUTURE_SELECTOR+NEXT_BANNER_SELECTOR*4+RESULT).extract_first()
            crawlerItem['early_registration']=title.css(START_FUTURE_SELECTOR+NEXT_BANNER_SELECTOR*5+RESULT).extract_first()
            crawlerItem['remark']=title.css(START_FUTURE_SELECTOR+NEXT_BANNER_SELECTOR*6+RESULT).extract_first()
            yield crawlerItem

        # body
        START=f'{FUTURE_SELECTOR} {BODY}'
        for title in response.css(START):
            START_FUTURE_SELECTOR=f'td'
            crawlerItem['type']='future'
            crawlerItem['conference']=title.css(START_FUTURE_SELECTOR+RESULT_BODY).extract_first()
            crawlerItem['city']=title.css(START_FUTURE_SELECTOR+NEXT_BODY_SELECTOR+RESULT).extract_first()
            crawlerItem['date']=f'{title.css(START_FUTURE_SELECTOR+NEXT_BODY_SELECTOR*2+RESULT).extract_first()}'
            crawlerItem['notification']=f'{title.css(START_FUTURE_SELECTOR+NEXT_BODY_SELECTOR*3+RESULT).extract_first()}'.replace('\n', '')\
                                                                                                                                .replace('\t', '')\
                                                                                                                                .replace('None', '')\
                                                                                                                                .strip()
            crawlerItem['final_version']=f'{title.css(START_FUTURE_SELECTOR+NEXT_BODY_SELECTOR*4+RESULT).extract_first()}'.replace('\n', '')\
                                                                                                                                 .replace('\t', '')\
                                                                                                                                 .replace('None', '')\
                                                                                                                                 .strip()
            crawlerItem['early_registration']=f'{title.css(START_FUTURE_SELECTOR+NEXT_BODY_SELECTOR*5+RESULT).extract_first()}'.replace('\n', '')\
                                                                                                                                      .replace('\t', '')\
                                                                                                                                      .replace('None', '')\
                                                                                                                                      .strip()
            crawlerItem['remark']=f'{title.css(START_FUTURE_SELECTOR+NEXT_BODY_SELECTOR*6+RESULT_BODY).extract()}'.replace('  ', '')\
                                                                                                                         .replace('[', '')\
                                                                                                                         .replace(']', '')\
                                                                                                                         .replace('\'', '')\
                                                                                                                         .replace('\\n', '')\
                                                                                                                         .replace('\\t', '')\
                                                                                                                         .replace(' ,', '')\
                                                                                                                         .replace(',,', ',')\
                                                                                                                         .replace('None', '')\
                                                                                                                         .strip()
            yield crawlerItem

        # footer
        for title in response.css(FUTURE_SELECTOR):
            START_FUTURE_SELECTOR=f'{FOOTER} th'
            crawlerItem['type']='future'
            crawlerItem['conference']=title.css(START_FUTURE_SELECTOR+RESULT).extract_first()
            crawlerItem['city']=title.css(START_FUTURE_SELECTOR+NEXT_BANNER_SELECTOR+RESULT).extract_first()
            crawlerItem['date']=title.css(START_FUTURE_SELECTOR+NEXT_BANNER_SELECTOR*2+RESULT).extract_first()
            crawlerItem['notification']=title.css(START_FUTURE_SELECTOR+NEXT_BANNER_SELECTOR*3+RESULT).extract_first()
            crawlerItem['final_version']=title.css(START_FUTURE_SELECTOR+NEXT_BANNER_SELECTOR*4+RESULT).extract_first()
            crawlerItem['early_registration']=title.css(START_FUTURE_SELECTOR+NEXT_BANNER_SELECTOR*5+RESULT).extract_first()
            crawlerItem['remark']=title.css(START_FUTURE_SELECTOR+NEXT_BANNER_SELECTOR*6+RESULT).extract_first()
            yield crawlerItem