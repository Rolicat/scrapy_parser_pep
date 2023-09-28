from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
RESULT_DIR = BASE_DIR / 'results'
RESULT_DIR.mkdir(exist_ok=True)
PATTERN = r'\w+ (?P<number>\d+) \D (?P<name>\w.+)$'
ENCODING = 'utf-8'
DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
