import csv
from datetime import datetime as dt

from pep_parse.constants import (
    BASE_DIR, ENCODING, DATETIME_FORMAT
)


class PepParsePipeline:

    def open_spider(self, spider):
        self.results = {}
        self.total = 0

    def process_item(self, item, spider):
        status = item['status']
        if status in self.results:
            self.results[status] += 1
        else:
            self.results[status] = 1
        self.total += 1
        return item

    def close_spider(self, spider):
        result_dir = BASE_DIR / 'results'
        result_dir.mkdir(exist_ok=True)
        now = dt.now()
        now_formatted = now.strftime(DATETIME_FORMAT)
        status_file_name = f'status_summary_{now_formatted}.csv'
        status_path = result_dir / status_file_name
        with open(status_path, 'w', encoding=ENCODING) as f:
            writer = csv.writer(f, dialect='unix')
            writer.writerow(('Статус', 'Количество'))
            for status, value in self.results.items():
                writer.writerow((status, value))
            writer.writerow(('Total', self.total))