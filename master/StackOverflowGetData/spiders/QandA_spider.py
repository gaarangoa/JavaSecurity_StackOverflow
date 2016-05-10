import scrapy
from StackOverflowQA.items import StackoverflowqaItem

import json



class StackoverflowSpider(scrapy.Spider):
    name="StackOverflowQA"
    allowed_domains=["http://stackoverflow.com/"]
    urls=json.load(open('/Users/gustavoarango/Dropbox/classes/software_engineering/project/lda/questions.json'))
    start_urls=['http://stackoverflow.com/questions/'+x for x in urls]
    

    def parse(self,response):
        for sel in response.xpath('/html/body/div/div[@id="content"]/div/div[@id="mainbar"]'):
            item=StackoverflowqaItem()
            #question=" ".join(sel.xpath('div[@class="question"]/table/tr/td/div/div[@class="post-text"]//text()').extract()).strip().replace("\n","").replace("'","").replace('"',"")
            #answers=" ".join(sel.xpath('div[@id="answers"]/div/table/tr/td[@class="answercell"]/div[@class="post-text"]//text()').extract()).strip().replace("\n","").replace("'","").replace('"',"").split("\r")
            down_count=sel.xpath('div[@class="question"]/table/tr/td[@class="votecell"]/div[@class="vote"]/span[@itemprop="downvoteCount"]/text()').extract()
            up_count=sel.xpath('div[@class="question"]/table/tr/td[@class="votecell"]/div[@class="vote"]/span[@itemprop="upvoteCount"]/text()').extract()
            favorite=sel.xpath('div[@class="question"]/table/tr/td[@class="votecell"]/div[@class="vote"]/div[@class="favoritecount"]/b/text()').extract()
            num_answers=sel.xpath('div[@id="answers"]/div[@id="answers-header"]/div[@class="subheader answers-subheader"]/h2/span[@itemprop="answerCount"]/text()').extract()
            id="".join(sel.xpath('div[@class="question"]/@data-questionid').extract()).strip()
            asked=sel.xpath('div[@class="question"]/table/tr/td[@class="postcell"]/div/table[@class="fw"]/tr/td[@class="post-signature owner"]/div[@class="user-info "]/div[@class="user-action-time"]/span/@title').extract()
            user=sel.xpath('div[@class="question"]/table/tr/td[@class="postcell"]/div/table[@class="fw"]/tr/td[@class="post-signature owner"]/div[@class="user-info "]/div[@class="user-details"]/a/text()').extract()
            reputation=sel.xpath('div[@class="question"]/table/tr/td[@class="postcell"]/div/table[@class="fw"]/tr/td[@class="post-signature owner"]/div[@class="user-info "]/div[@class="user-details"]/div[@class="-flair"]/span[@class="reputation-score"]/text()').extract()
            views=sel.xpath('/html/body/div/div[@id="content"]/div/div[@id="sidebar"]/div[@class="module question-stats"]/table[@id="qinfo"]/tr/td/p[@class="label-key"]/b/text()').extract()
            active=sel.xpath('/html/body/div/div[@id="content"]/div/div[@id="sidebar"]/div[@class="module question-stats"]/table[@id="qinfo"]/tr/td/p[@class="label-key"]/b/a/@title').extract()
            item['link']= id; 
            #item['question']=question
            #item['answers']=answers
            item['up_count']=up_count
            item['down_count']=down_count
            item['favorite']=favorite
            item['num_answers']=num_answers
            item['asked']=asked
            item['user']=user
            item['reputation']=reputation
            item['views']=views
            item['active']=active
            #print id, up_count, asked, user, reputation, views, active
            yield item
            