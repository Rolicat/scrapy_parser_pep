from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
PATTERN = r'\w+ (?P<number>\d+) \D (?P<name>\w.+)$'
ENCODING = 'utf-8'
DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
