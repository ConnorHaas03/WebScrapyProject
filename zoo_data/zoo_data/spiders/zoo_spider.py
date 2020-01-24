import scrapy
from zoo_data.items import ZooDataItem

#needed to use (scrapy startproject bestbuy) in shell to initialize these files in the cd we were in the cmd we called
#(scrapy shell "<url_to_scrape>")
#to crawl in shell, (scrapy crawl 'zoodata_spider') -name we designate below
#fetch to:  fetch('https://en.wikipedia.org/wiki/Abilene_Zoological_Gardens')

class ZooDataSpider( scrapy.Spider ):
    name = 'zoodata_spider'
    allowed_urls = ['https://en.wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/List_of_AZA_member_zoos_and_aquaria']

    def parse(self, response):
        
        zooTable = response.xpath('//table[contains(@class,"wikitable sortable")]//tbody/tr')

        #print(zooTable, '-'*50)
        for zoo in zooTable:
            name = zoo.xpath('./td[1]/a/text()').extract_first()
            if not name:
                continue
            else:
                #print(zoo.xpath('./td[1]/a/@href').extract_first(),'-'*80)
                name_url = response.urljoin(zoo.xpath('./td[1]/a/@href').extract_first()) 
                address = zoo.xpath('./td[2]/text()').extract_first()
                city = zoo.xpath('./td[3]/a/text()').extract_first()
                state = zoo.xpath('./td[4]/a/text()').extract_first() 
                country = zoo.xpath('td[4]/a[2]/text()').extract_first()

                item = {} #ZooDataItem()
                item['name'] = name
                item['address'] = address
                item['city'] = city
                item['state'] = state
                item['country'] = country
                item['name_url'] = name_url
                yield scrapy.Request(name_url, self.parse_zoo_path, meta=item)

    def parse_zoo_path(self,response):            

            #print(name_url)
            num_species = response.xpath('//table[@class = "infobox vcard"]/tbody//th/abbr//parent::th//following-sibling::td/text()').extract_first()    
            num_animals = response.xpath('//table[@class = "infobox vcard"]/tbody//th/abbr//parent::th//following-sibling::td/text()').extract_first()    

            item = ZooDataItem()
            item['name'] = response.meta['name']
            item['address'] = response.meta['address']
            item['city'] = response.meta['city']
            item['state'] = response.meta['state']
            item['country'] = response.meta['country']
            item['name_url'] = response.meta['name_url']
            item['num_species'] = num_species
            item['num_animals'] = num_animals

            yield item