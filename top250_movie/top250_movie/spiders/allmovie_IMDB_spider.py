import scrapy

class loopeachmovieSpider(scrapy.Spider):
	name = 'allmovie_IMDB'

	index = range(1,8000,100)
	start_urls = list()
	for page in index:
    		start_urls.append('http://www.imdb.com/list/ls057823854/?start=' + str(page) + '&view=detail&sort=listorian:asc')
 
	def parse(self,response):
	    # follow links to each movie page from top250 rated movie
	    for href in response.css('div.info').css('b a::attr(href)').extract():
		yield scrapy.Request(response.urljoin(href),
				     callback = self.parse_movie)


	def parse_movie(self,response):
            yield {
		'name' : response.css('div.title_wrapper').css('h1::text').extract()[0],
		'year' : response.css('div.title_wrapper').css('span a::text').extract(),
		'length' :response.css('div.title_wrapper').css('div.subtext').css('time::text').extract(),
        	'director':response.css('div.credit_summary_item')[0].css('a span::text').extract(),
        	'writers':response.css('div.credit_summary_item')[1].css('span a span::text').extract(),
        	'stars':response.css('div.credit_summary_item')[2].css('span a span::text').extract(),
        	'genre':response.css('div.subtext')[0].css('a[href*=genre] span::text').extract(),
        	'Description':response.css('div.plot_summary').css('div.summary_text').css('div::text').extract()

		}

