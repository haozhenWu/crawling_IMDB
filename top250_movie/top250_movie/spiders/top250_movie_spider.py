import scrapy

class Top250_movie(scrapy.Spider):
	name = "top250_movie"
	start_urls = ['http://www.imdb.com/chart/top?ref_=nv_mv_250_6']
	
	def parse(self,response):
	    for movie in response.css('td.titleColumn'):
		yield {
			'url' : movie.css('a::attr(href)').extract(),
        		'name' : movie.css('a::text').extract(),
        		'year' : movie.css('span.secondaryInfo::text').extract()		}
