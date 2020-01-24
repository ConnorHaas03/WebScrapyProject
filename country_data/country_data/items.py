# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CountryDataItem(scrapy.Item):
    # define the fields for your item here like:
    #city_state = scrapy.Field()
    city_name = scrapy.Field()
    pop_2018 = scrapy.Field()
    city_2016_land_area = scrapy.Field()
    pop_density = scrapy.Field()
