from lxml import etree
from proxypool.schemas.proxy import Proxy
from proxypool.crawlers.base import BaseCrawler


BASE_URL = 'http://www.kxdaili.com/dailiip/{type}/{page}.html'
MAX_PAGE = 3


class KxdailiCrawler(BaseCrawler):

    urls = [BASE_URL.format(type=type, page=page) for type in [1, 2] for page in range(1, MAX_PAGE + 1)]

    def parse(self, html):
        """
        parse html file to get proxies
        :return:
        """

        tree = etree.HTML(html)

        trs = tree.xpath('//table[@class="active"]/tbody/tr')

        for tr in trs:
            host = tr.xpath('./td[1]/text()')[0]
            port = int(tr.xpath('./td[2]/text()')[0])
            yield Proxy(host=host, port=port)


if __name__ == '__main__':
    crawler = KxdailiCrawler()
    for proxy in crawler.crawl():
        print(proxy)