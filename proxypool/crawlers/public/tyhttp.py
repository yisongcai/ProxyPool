from pyquery import PyQuery as pq
from proxypool.schemas.proxy import Proxy
from proxypool.crawlers.base import BaseCrawler


BASE_URL = 'https://www.tyhttp.com/free/page{page}/'
MAX_PAGE = 3


class TyhttpCrawler(BaseCrawler):

    urls = [BASE_URL.format(page=page) for page in range(1, MAX_PAGE + 1)]

    def parse(self, html):
        """
        parse html file to get proxies
        :return:
        """

        doc = pq(html)
        trs = doc('#ip_list > div').items()

        for tr in trs:
            host = tr.find('div:nth-child(1)').text()
            port = int(tr.find('div:nth-child(2)').text())
            yield Proxy(host=host, port=port)



if __name__ == '__main__':
    crawler = TyhttpCrawler()
    for proxy in crawler.crawl():
        print(proxy)