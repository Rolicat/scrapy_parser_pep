from pathlib import Path

BASE_DIR = Path(__file__).parent.parent / 'results'
BASE_DIR.mkdir(exist_ok=True)
# Регулярка используется при вычленении номера PEP и его названия из заголовка
PATTERN = r'\w+ (?P<number>\d+) \D (?P<name>\w.+)$'
ENCODING = 'utf-8'
DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
DOMAIN = 'peps.python.org'
FILE_TYPE = 'csv'
