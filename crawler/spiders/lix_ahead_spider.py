import scrapy
from crawler.items import CrawlerAheadItem

class lixAheadSpider(scrapy.Spider):
    name='lix-ahead-spider'
    start_urls=['https://www.lix.polytechnique.fr/~hermann/conf.php']

    def parse(self, response):
        crawlerItem=CrawlerAheadItem()
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

        ######################## ahead ########################
        AHEAD_SELECTOR=f'{ID_LIST[0]} + {CONFERENCE_SELECTOR}'

        # header
        for title in response.css(AHEAD_SELECTOR):
            START_AHEAD_SELECTOR=f' {HEADER} th'
            crawlerItem['type']='ahead'
            crawlerItem['conference']=title.css(START_AHEAD_SELECTOR+RESULT).extract_first()
            crawlerItem['city']=title.css(START_AHEAD_SELECTOR+NEXT_BANNER_SELECTOR+RESULT).extract_first()
            crawlerItem['deadline']=title.css(START_AHEAD_SELECTOR+NEXT_BANNER_SELECTOR*2+RESULT).extract_first()
            crawlerItem['date']=title.css(START_AHEAD_SELECTOR+NEXT_BANNER_SELECTOR*3+RESULT).extract_first()
            crawlerItem['notification']=title.css(START_AHEAD_SELECTOR+NEXT_BANNER_SELECTOR*4+RESULT).extract_first()
            crawlerItem['format_and_comemnt']=title.css(START_AHEAD_SELECTOR+NEXT_BANNER_SELECTOR*5+RESULT).extract_first()
            yield crawlerItem

        # body
        START=f'{AHEAD_SELECTOR} {BODY}'
        for title in response.css(START):
            START_AHEAD_SELECTOR=f'td'
            DEADLINE_TH1=START_AHEAD_SELECTOR+NEXT_BODY_SELECTOR*2+RESULT
            DEADLINE_TH2=START_AHEAD_SELECTOR+NEXT_BODY_SELECTOR*2+' b'+RESULT
            
            crawlerItem['type']='ahead'
            crawlerItem['conference']=title.css(START_AHEAD_SELECTOR+RESULT_BODY).extract_first()
            crawlerItem['city']=title.css(START_AHEAD_SELECTOR+NEXT_BODY_SELECTOR+RESULT).extract_first()
            crawlerItem['deadline']=f'{title.css(DEADLINE_TH2).extract_first()} {title.css(DEADLINE_TH1).extract_first()}'.replace('None', '')\
                                                                                                                          .replace('double-blind', '')\
                                                                                                                          .strip()
            crawlerItem['date']=title.css(START_AHEAD_SELECTOR+NEXT_BODY_SELECTOR*3+RESULT).extract_first()
            crawlerItem['notification']=title.css(START_AHEAD_SELECTOR+NEXT_BODY_SELECTOR*4+RESULT).extract_first()
            crawlerItem['format_and_comemnt']=f'{title.css(START_AHEAD_SELECTOR+NEXT_BODY_SELECTOR*5+RESULT_BODY).extract()}'.replace('  ', '')\
                                                                                                                           .replace('[', '')\
                                                                                                                           .replace(']', '')\
                                                                                                                           .replace('\'', '')\
                                                                                                                           .replace('\\n', '')\
                                                                                                                           .replace('\\t', '')\
                                                                                                                           .replace(' ,', '')\
                                                                                                                           .strip()
            yield crawlerItem

        # footer
        for title in response.css(AHEAD_SELECTOR):
            START_AHEAD_SELECTOR=f'{FOOTER} th'
            crawlerItem['type']='ahead'
            crawlerItem['conference']=title.css(START_AHEAD_SELECTOR+RESULT).extract_first()
            crawlerItem['city']=title.css(START_AHEAD_SELECTOR+NEXT_BANNER_SELECTOR+RESULT).extract_first()
            crawlerItem['deadline']=title.css(START_AHEAD_SELECTOR+NEXT_BANNER_SELECTOR*2+RESULT).extract_first()
            crawlerItem['date']=title.css(START_AHEAD_SELECTOR+NEXT_BANNER_SELECTOR*3+RESULT).extract_first()
            crawlerItem['notification']=title.css(START_AHEAD_SELECTOR+NEXT_BANNER_SELECTOR*4+RESULT).extract_first()
            crawlerItem['format_and_comemnt']=title.css(START_AHEAD_SELECTOR+NEXT_BANNER_SELECTOR*5+RESULT).extract_first()
            yield crawlerItem