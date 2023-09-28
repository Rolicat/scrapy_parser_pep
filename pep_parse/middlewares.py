from scrapy import signals, Crawler, Spider
from scrapy.http import Response, Request


class PepParseSpiderMiddleware:

    @classmethod
    def from_crawler(cls, crawler: Crawler):
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(
            self, response: Response, spider: Spider
    ) -> None:
        return None

    def process_spider_output(
            self, response: Response, result, spider: Spider
    ):
        for i in result:
            yield i

    def process_spider_exception(
            self, response: Response, exception, spider: Spider
    ) -> None:
        pass

    def process_start_requests(self, start_requests, spider: Spider):
        for r in start_requests:
            yield r

    def spider_opened(self, spider: Spider) -> None:
        spider.logger.info('Spider opened: %s' % spider.name)


class PepParseDownloaderMiddleware:

    @classmethod
    def from_crawler(cls, crawler: Crawler):
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request: Request, spider: Spider) -> None:
        return None

    def process_response(
            self, request: Request, response: Response, spider: Spider
    ) -> Response:
        return response

    def process_exception(
            self, request: Request, exception, spider: Spider
    ) -> None:
        pass

    def spider_opened(self, spider: Spider) -> None:
        spider.logger.info('Spider opened: %s' % spider.name)
