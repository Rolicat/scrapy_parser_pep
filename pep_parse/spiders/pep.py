import scrapy
from pep_parse.items import PepParseItem
import re

from pep_parse.constants import PATTERN


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        table_tag = response.css(
            'section#numerical-index table.pep-zero-table tbody'
        )
        for row_tag in table_tag.css('tr'):
            href = row_tag.css('a.reference::attr(href)').get()
            yield response.follow(href, callback=self.parse_pep)

    def parse_pep(self, response):
        pep_title = response.css('h1.page-title::text').get()
        text_match = re.search(PATTERN, pep_title)
        if text_match is None:
            number, name = pep_title.split()[1], ''
        else:
            number, name = text_match.groups()
        status = response.css('abbr::text').get()
        yield PepParseItem(
            number=number,
            name=name,
            status=status
        )
