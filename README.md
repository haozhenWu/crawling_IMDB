# crawling_IMDB

This is a demo code of how to use scrapy to crawl the Top250 rate movies' Link,Name and year. 

Use
git clone https://github.com/haozhenWu/crawling_IMDB.git

to download the repository and run 

scrapy crawl top250_movie -o top250_movie.csv

This will run the crawler named "top250_movie" and store the extracted informations into a csv file named top250_movie.csv


Right now, there are 3 spiders in the folder.

* top250_movie : This spider looks through the http://www.imdb.com/chart/top?ref_=nv_mv_250_6 page and extract attributes from it.

* loopeachmovie : This will first get all the movie url from http://www.imdb.com/chart/top?ref_=nv_mv_250_6 and go into each movie's page and extract attributes from each movie's page.

* allmovie_IMDB : This will get around 8000 movies from url such as http://www.imdb.com/list/ls057823854/?start=001&view=detail&sort=listorian:asc 

