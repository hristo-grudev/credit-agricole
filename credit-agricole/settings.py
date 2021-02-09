BOT_NAME = 'credit-agricole'

SPIDER_MODULES = ['credit-agricole.spiders']
NEWSPIDER_MODULE = 'credit-agricole.spiders'
FEED_EXPORT_ENCODING = 'utf-8'
LOG_LEVEL = 'ERROR'
DOWNLOAD_DELAY = 0

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
	'credit-agricole.pipelines.CreditagricolePipeline': 100,

}