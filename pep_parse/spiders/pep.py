import scrapy
from scrapy.http import Response
from pep_parse.items import PepParseItem
import re

from pep_parse.constants import PATTERN, DOMAIN
from pep_parse.css_tags import CSSSelector


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = [DOMAIN]
    start_urls = [f'https://{DOMAIN}/']

    def parse(self, response: Response) -> Response:
        table_tag = response.css(
            CSSSelector.TBODY_TAG
        )
        for row_tag in table_tag.css(CSSSelector.TR_TAG):
            href = row_tag.css(CSSSelector.A_HREF).get()
            yield response.follow(href, callback=self.parse_pep)

    def parse_pep(self, response: Response) -> Response:
        pep_title = response.css(CSSSelector.H1_TEXT).get()
        text_match = re.search(PATTERN, pep_title)
        if text_match is None:
            number, name = pep_title.split()[1], ''
        else:
            number, name = text_match.groups()
        status = response.css(CSSSelector.ABBR_TEXT).get()
        yield PepParseItem(
            number=number,
            name=name,
            status=status
        )
