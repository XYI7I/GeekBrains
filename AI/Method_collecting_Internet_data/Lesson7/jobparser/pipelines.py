# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient

class JobparserPipeline:
    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.mongobase = client.vacancies2808

    def process_item(self, item, spider):
        my_item = dict(item)
        item['salary_min'], item['salary_max'], item['salary_cur'] = self.process_salary(item['salary'])

        collection = self.mongobase[spider.name]
        collection.insert_one(item)
        return item


    def process_salary(self, salary):
        salary_min = 0
        salary_max = 0
        salary_cur = ''
        return salary_min, salary_max, salary_cur
