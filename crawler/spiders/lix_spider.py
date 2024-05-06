import scrapy

class lixSpider(scrapy.Spider):
    name='lix-spider'
    start_urls=['https://www.lix.polytechnique.fr/~hermann/conf.php']
    
    def parse(self, response):
        # #planning = .central + .conference
        # #popup
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
            yield {
                'Type': 'Ahead',
                'Conference': title.css(START_AHEAD_SELECTOR+RESULT).extract_first(),
                'City': title.css(START_AHEAD_SELECTOR+NEXT_BANNER_SELECTOR+RESULT).extract_first(),
                'Deadline': title.css(START_AHEAD_SELECTOR+NEXT_BANNER_SELECTOR*2+RESULT).extract_first(),
                'Date': title.css(START_AHEAD_SELECTOR+NEXT_BANNER_SELECTOR*3+RESULT).extract_first(),
                'Notification': title.css(START_AHEAD_SELECTOR+NEXT_BANNER_SELECTOR*4+RESULT).extract_first(),
                'FormatAndComemnt': title.css(START_AHEAD_SELECTOR+NEXT_BANNER_SELECTOR*5+RESULT).extract_first(),
            }  
        
        # body
        START=f'{AHEAD_SELECTOR} {BODY}'
        for title in response.css(START):
            START_AHEAD_SELECTOR=f'td'
            DEADLINE_TH1=START_AHEAD_SELECTOR+NEXT_BODY_SELECTOR*2+RESULT
            DEADLINE_TH2=START_AHEAD_SELECTOR+NEXT_BODY_SELECTOR*2+' b'+RESULT

            yield {
                'Type': 'Ahead',
                'Conference': title.css(START_AHEAD_SELECTOR+RESULT_BODY).extract_first(),
                'City': title.css(START_AHEAD_SELECTOR+NEXT_BODY_SELECTOR+RESULT).extract_first(),
                'Deadline': f'{title.css(DEADLINE_TH2).extract_first()} {title.css(DEADLINE_TH1).extract_first()}'.replace('None', '').replace('double-blind', '').strip(),
                'Date': title.css(START_AHEAD_SELECTOR+NEXT_BODY_SELECTOR*3+RESULT).extract_first(),
                'Notification': title.css(START_AHEAD_SELECTOR+NEXT_BODY_SELECTOR*4+RESULT).extract_first(),
                'FormatAndComemnt': f'{title.css(START_AHEAD_SELECTOR+NEXT_BODY_SELECTOR*5+RESULT_BODY).extract()}'.replace('  ', '').replace('[', '').replace(']', '').replace('\'', '').replace('\\n', '').replace('\\t', '').replace(' ,', '').strip(),
            }  

        # footer
        for title in response.css(AHEAD_SELECTOR):
            START_AHEAD_SELECTOR=f'{FOOTER} th'
            yield {
                'Type': 'Ahead',
                'Conference': title.css(START_AHEAD_SELECTOR+RESULT).extract_first(),
                'City': title.css(START_AHEAD_SELECTOR+NEXT_BANNER_SELECTOR+RESULT).extract_first(),
                'Deadline': title.css(START_AHEAD_SELECTOR+NEXT_BANNER_SELECTOR*2+RESULT).extract_first(),
                'Date': title.css(START_AHEAD_SELECTOR+NEXT_BANNER_SELECTOR*3+RESULT).extract_first(),
                'Notification': title.css(START_AHEAD_SELECTOR+NEXT_BANNER_SELECTOR*4+RESULT).extract_first(),
                'FormatAndComemnt': title.css(START_AHEAD_SELECTOR+NEXT_BANNER_SELECTOR*5+RESULT).extract_first(),
            }  

        ######################## Runing ########################
        RUNNING_SELECTOR=f'{ID_LIST[1]} + {CONFERENCE_SELECTOR}'

        # header
        for title in response.css(RUNNING_SELECTOR):
            START_RUNNING_SELECTOR=f' {HEADER} th'
            yield {
                'Type': 'Running',
                'Conference': title.css(START_RUNNING_SELECTOR+RESULT).extract_first(),
                'City': title.css(START_RUNNING_SELECTOR+NEXT_BANNER_SELECTOR+RESULT).extract_first(),
                'Date': title.css(START_RUNNING_SELECTOR+NEXT_BANNER_SELECTOR*2+RESULT).extract_first(),
                'Remarks': title.css(START_RUNNING_SELECTOR+NEXT_BANNER_SELECTOR*3+RESULT).extract_first(),
            }  
        
        # body
        START=f'{RUNNING_SELECTOR} {BODY}'
        for title in response.css(START):
            START_RUNNING_SELECTOR=f'td'
            yield {
                'Type': 'Running',
                'Conference': title.css(START_RUNNING_SELECTOR+RESULT_BODY).extract_first(),
                'City': title.css(START_RUNNING_SELECTOR+NEXT_BODY_SELECTOR+RESULT).extract_first(),
                'Date': title.css(START_RUNNING_SELECTOR+NEXT_BODY_SELECTOR*2+RESULT).extract_first(),
                'Remarks': title.css(START_RUNNING_SELECTOR+NEXT_BODY_SELECTOR*3+RESULT).extract_first()
            }  

        # footer
        for title in response.css(RUNNING_SELECTOR):
            START_RUNNING_SELECTOR=f'{FOOTER} th'
            yield {
                'Type': 'Running',
                'Conference': title.css(START_RUNNING_SELECTOR+RESULT).extract_first(),
                'City': title.css(START_RUNNING_SELECTOR+NEXT_BANNER_SELECTOR+RESULT).extract_first(),
                'Date': title.css(START_RUNNING_SELECTOR+NEXT_BANNER_SELECTOR*2+RESULT).extract_first(),
                'Remarks': title.css(START_RUNNING_SELECTOR+NEXT_BANNER_SELECTOR*3+RESULT).extract_first(),
            }

        ######################## Future ########################
        FUTURE_SELECTOR=f'{ID_LIST[2]} + {CONFERENCE_SELECTOR}'

        # header
        for title in response.css(FUTURE_SELECTOR):
            START_FUTURE_SELECTOR=f' {HEADER} th'
            yield {
                'Type': 'Future',
                'Conference': title.css(START_FUTURE_SELECTOR+RESULT).extract_first(),
                'City': title.css(START_FUTURE_SELECTOR+NEXT_BANNER_SELECTOR+RESULT).extract_first(),
                'Date': title.css(START_FUTURE_SELECTOR+NEXT_BANNER_SELECTOR*2+RESULT).extract_first(),
                'Notification': title.css(START_FUTURE_SELECTOR+NEXT_BANNER_SELECTOR*3+RESULT).extract_first(),
                'FinalVersion': title.css(START_FUTURE_SELECTOR+NEXT_BANNER_SELECTOR*4+RESULT).extract_first(),
                'EarlyRegistraion': title.css(START_FUTURE_SELECTOR+NEXT_BANNER_SELECTOR*5+RESULT).extract_first(),
                'Remarks': title.css(START_FUTURE_SELECTOR+NEXT_BANNER_SELECTOR*6+RESULT).extract_first()
            }  
        
        # body
        START=f'{FUTURE_SELECTOR} {BODY}'
        for title in response.css(START):
            START_FUTURE_SELECTOR=f'td'
            yield {
                'Type': 'Future',
                'Conference': title.css(START_FUTURE_SELECTOR+RESULT_BODY).extract_first(),
                'City': title.css(START_FUTURE_SELECTOR+NEXT_BODY_SELECTOR+RESULT).extract_first(),
                'Date': f'{title.css(START_FUTURE_SELECTOR+NEXT_BODY_SELECTOR*2+RESULT).extract_first()}',
                'Notification': f'{title.css(START_FUTURE_SELECTOR+NEXT_BODY_SELECTOR*3+RESULT).extract_first()}'.replace('\n', '')
                                                                                                                 .replace('\t', '')
                                                                                                                 .replace('None', '')
                                                                                                                 .strip(),
                'FinalVersion': f'{title.css(START_FUTURE_SELECTOR+NEXT_BODY_SELECTOR*4+RESULT).extract_first()}'.replace('\n', '')
                                                                                                                 .replace('\t', '')
                                                                                                                 .replace('None', '')
                                                                                                                 .strip(),
                'EarlyRegistraion': f'{title.css(START_FUTURE_SELECTOR+NEXT_BODY_SELECTOR*5+RESULT).extract_first()}'.replace('\n', '')
                                                                                                                     .replace('\t', '')
                                                                                                                     .replace('None', '')
                                                                                                                     .strip(),
                'Remarks': f'{title.css(START_FUTURE_SELECTOR+NEXT_BODY_SELECTOR*6+RESULT_BODY).extract()}'.replace('  ', '')
                                                                                                           .replace('[', '')
                                                                                                           .replace(']', '')
                                                                                                           .replace('\'', '')
                                                                                                           .replace('\\n', '')
                                                                                                           .replace('\\t', '')
                                                                                                           .replace(' ,', '')
                                                                                                           .replace(',,', ',')
                                                                                                           .replace('None', '')
                                                                                                           .strip(),
            }  

        # footer
        for title in response.css(FUTURE_SELECTOR):
            START_FUTURE_SELECTOR=f'{FOOTER} th'
            yield {
                'Type': 'Future',
                'Conference': title.css(START_FUTURE_SELECTOR+RESULT).extract_first(),
                'City': title.css(START_FUTURE_SELECTOR+NEXT_BANNER_SELECTOR+RESULT).extract_first(),
                'Date': title.css(START_FUTURE_SELECTOR+NEXT_BANNER_SELECTOR*2+RESULT).extract_first(),
                'Notification': title.css(START_FUTURE_SELECTOR+NEXT_BANNER_SELECTOR*3+RESULT).extract_first(),
                'FinalVersion': title.css(START_FUTURE_SELECTOR+NEXT_BANNER_SELECTOR*4+RESULT).extract_first(),
                'EarlyRegistraion': title.css(START_FUTURE_SELECTOR+NEXT_BANNER_SELECTOR*5+RESULT).extract_first(),
                'Remarks': title.css(START_FUTURE_SELECTOR+NEXT_BANNER_SELECTOR*6+RESULT).extract_first()
            }

        ######################## Planning ########################
        PLANNING_SELECTOR=f'.central + .conference'

        # header
        for title in response.css(PLANNING_SELECTOR):
            START_PLANNING_SELECTOR=f' {HEADER} th'
            yield {
                'Type': 'Planning',
                'Conference': title.css(START_PLANNING_SELECTOR+RESULT).extract_first(),
                'Year': title.css(START_PLANNING_SELECTOR+NEXT_BANNER_SELECTOR+RESULT).extract_first(),
                'City': title.css(START_PLANNING_SELECTOR+NEXT_BANNER_SELECTOR*2+RESULT).extract_first(),
                'StartingDate': title.css(START_PLANNING_SELECTOR+NEXT_BANNER_SELECTOR*3+RESULT).extract_first(),
                'EndingDate': title.css(START_PLANNING_SELECTOR+NEXT_BANNER_SELECTOR*4+RESULT).extract_first(),
                'Remarks': title.css(START_PLANNING_SELECTOR+NEXT_BANNER_SELECTOR*5+RESULT).extract_first()
            }  
        
        # body
        START=f'{PLANNING_SELECTOR} {BODY}'
        for title in response.css(START):
            START_PLANNING_SELECTOR=f'td'
            yield {
                'Type': 'Planning',
                'Conference': title.css(START_PLANNING_SELECTOR+RESULT_BODY).extract_first(),
                'Year': title.css(START_PLANNING_SELECTOR+NEXT_BODY_SELECTOR+RESULT).extract_first(),
                'City': f'{title.css(START_PLANNING_SELECTOR+NEXT_BODY_SELECTOR*2+RESULT).extract_first()}',
                'StartingDate': f'{title.css(START_PLANNING_SELECTOR+NEXT_BODY_SELECTOR*3+RESULT).extract_first()}',
                'EndingDate': f'{title.css(START_PLANNING_SELECTOR+NEXT_BODY_SELECTOR*4+RESULT).extract_first()}',
                'Remarks': f'{title.css(START_PLANNING_SELECTOR+NEXT_BODY_SELECTOR*5+RESULT_BODY).extract()}'.replace('  ', '')
                                                                                                             .replace('\'', '')
                                                                                                             .replace('[', '')
                                                                                                             .replace(']', '')
                                                                                                             .replace('\\n', '')
                                                                                                             .replace('\\t', '')
                                                                                                             .replace(' ,', ',')
                                                                                                             .replace('with,', 'with')
                                                                                                             .strip()
            }  

        # footer
        for title in response.css(PLANNING_SELECTOR):
            START_PLANNING_SELECTOR=f'{FOOTER} th'
            yield {
                'Type': 'Planning',
                'Conference': title.css(START_PLANNING_SELECTOR+RESULT).extract_first(),
                'Year': title.css(START_PLANNING_SELECTOR+NEXT_BANNER_SELECTOR+RESULT).extract_first(),
                'City': title.css(START_PLANNING_SELECTOR+NEXT_BANNER_SELECTOR*2+RESULT).extract_first(),
                'StartingDate': title.css(START_PLANNING_SELECTOR+NEXT_BANNER_SELECTOR*3+RESULT).extract_first(),
                'EndingDate': title.css(START_PLANNING_SELECTOR+NEXT_BANNER_SELECTOR*4+RESULT).extract_first(),
                'Remarks': title.css(START_PLANNING_SELECTOR+NEXT_BANNER_SELECTOR*5+RESULT).extract_first()
            }

        ######################## Fullname ########################
        FULLNAME_SELECTOR=f'#popup .navlist + .central'
        
        # body
        START=f'{FULLNAME_SELECTOR} {BODY}'
        for title in response.css(START):
            START_FULLNAME_SELECTOR=f'td'
            yield {
                'Type': 'Fullname',
                'ConferenceID': title.css(START_FULLNAME_SELECTOR+RESULT).extract_first(),
                'Fullname': title.css(START_FULLNAME_SELECTOR+NEXT_BODY_SELECTOR+RESULT).extract_first()
            }  









