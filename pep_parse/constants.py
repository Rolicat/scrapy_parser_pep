from pathlib import Path

BASE_DIR = Path(__file__).parent.parent / 'results'
BASE_DIR.mkdir(exist_ok=True)
PATTERN = r'\w+ (?P<number>\d+) \D (?P<name>\w.+)$'
ENCODING = 'utf-8'
DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
