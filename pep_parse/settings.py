from pep_parse.constants import FILE_TYPE


BOT_NAME = 'pep_parse'
NEWSPIDER_MODULE = f'{BOT_NAME}.spiders'
SPIDER_MODULES = [NEWSPIDER_MODULE]

LOG_LEVEL = 'INFO'
ROBOTSTXT_OBEY = True
ITEM_PIPELINES = {
    f'{BOT_NAME}.pipelines.PepParsePipeline': 300,
}
FEEDS = {
    f'results/pep_%(time)s.{FILE_TYPE}': {
        'format': FILE_TYPE,
        'fields': ['number', 'name', 'status'],
        'overwrite': True,
    }
}
