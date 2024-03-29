import csv
from datetime import datetime as dt

from scrapy import Spider

from pep_parse.items import PepParseItem
from pep_parse.constants import (
    ENCODING, DATETIME_FORMAT, BASE_DIR, FILE_TYPE
)


class PepParsePipeline:

    def open_spider(self, spider: Spider) -> None:
        self.results = {}
        self.total = 0

    def process_item(self, item: PepParseItem, spider: Spider) -> PepParseItem:
        status = item['status']
        if status in self.results:
            self.results[status] += 1
        else:
            self.results[status] = 1
        self.total += 1
        return item

    def close_spider(self, spider: Spider) -> None:
        now = dt.now()
        now_formatted = now.strftime(DATETIME_FORMAT)
        status_file_name = f'status_summary_{now_formatted}.{FILE_TYPE}'
        status_path = BASE_DIR / status_file_name
        with open(status_path, 'w', encoding=ENCODING) as f:
            writer = csv.writer(f, dialect='unix')
            writer.writerow(('Статус', 'Количество'))
            for status, value in self.results.items():
                writer.writerow((status, value))
            writer.writerow(('Total', self.total))
