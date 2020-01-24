import scrapy
from country_data.items import CountryDataItem

#needed to use (scrapy startproject bestbuy) in shell to initialize these files in the cd we were in the cmd we called
#(scrapy shell "<url_to_scrape>")
#to crawl in shell, (scrapy crawl 'zoodata_spider') -name we designate below

class CountryDataSpider( scrapy.Spider ):
    name = 'countrydata_spider'
    allowed_urls = ['https://en.wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population']

    def parse(self, response):

        countryTable = response.xpath('//table[contains(@class,"wikitable sortable")]')

        for country in countryTable:
            print("entered for", '-'*50)
            #city_state = country.xpath('//tbody/tr/td//a/text()').extract()
            city_name = country.xpath('//tbody/tr/td[2]//a/text()').extract()
            pop_2018 = country.xpath('//table[contains(@class, "wikitable sortable")]//tbody/tr/td[4]/text()').extract() 
            city_2016_land_area = country.xpath('//tbody/tr/td[7]/text()').extract()
            pop_density = country.xpath('//tbody/tr/td[9]/text()').extract()

            item2 = CountryDataItem()
            item2['city_name'] = city_name
            #item2['city_state'] = city_state
            item2['pop_2018'] = pop_2018
            item2['city_2016_land_area'] = city_2016_land_area
            item2['pop_density'] = pop_density
            yield item2



