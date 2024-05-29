import scrapy
from scrapy_splash import SplashRequest


class RealtySSpider(scrapy.Spider):
    name = 'realty_s_spider'
    allowed_domains = ['xn--80az8a.xn--d1aqf.xn--p1ai']
    start_urls = [
        'https://xn--80az8a.xn--d1aqf.xn--p1ai/сервисы/каталог-новостроек/список-объектов/список?place=0-6'
    ]

    def start_requests(self):
        for url in self.start_urls:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'en-US,en;q=0.9',
                'Referer': 'https://www.google.com/',
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1'
            }
            yield SplashRequest(url, self.parse, args={'wait': 2}, headers=headers)

    def parse(self, response):
        objects_ = response.xpath('//div[@class="search-results__item"]')
        print(f'Length of objects: {len(objects_)}')

        for obj in objects_:
            yield {
                'headline': obj.xpath('.//div[@class="object-info__title"]/a/text()').get(default='').strip(),
                'address': obj.xpath('.//div[@class="object-info__location"]/text()').get(default='').strip(),
                'id': obj.xpath('.//div[@class="object-info__id"]/text()').get(default='').strip(),
                'commissioning': obj.xpath('.//div[contains(text(), "Ввод в эксплуатацию")]/following-sibling::div/text()').get(default='').strip(),
                'developer': obj.xpath('.//div[contains(text(), "Застройщик")]/following-sibling::div/a/text()').get(default='').strip(),
                'group_of_companies': obj.xpath('.//div[contains(text(), "Группа компаний")]/following-sibling::div/text()').get(default='').strip(),
                'date_of_project_publication': obj.xpath('.//div[contains(text(), "Дата публикации проекта")]/following-sibling::div/text()').get(default='').strip(),
                'key_issue': obj.xpath('.//div[contains(text(), "Выдача ключей")]/following-sibling::div/text()').get(default='').strip(),
                'average_price_per_m2': obj.xpath('.//div[contains(text(), "Средняя цена за 1 м²")]/following-sibling::div/text()').get(default='').strip(),
                'apartment_sold_out': obj.xpath('.//div[contains(text(), "Распроданность квартир")]/following-sibling::div/text()').get(default='').strip(),
                'property_class': obj.xpath('.//div[contains(text(), "Класс недвижимости")]/following-sibling::div/text()').get(default='').strip(),
                'number_of_apartments': obj.xpath('.//div[contains(text(), "Количество квартир")]/following-sibling::div/text()').get(default='').strip(),
            }

        # Найти кнопку "Показать еще" и создать запрос для следующей страницы
        next_page = response.xpath('//a[@class="show-more-button"]/@href').get()
        if next_page:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'en-US,en;q=0.9',
                'Referer': response.url,
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1'
            }
            yield SplashRequest(response.urljoin(next_page), self.parse, args={'wait': 2}, headers=headers)
