import logging
from logging import handlers

logger =logging.getLogger("test")
# fh = logging.FileHandler("test.log")
sh = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# fh.setFormatter(formatter)
sh.setFormatter(formatter)
# logger.addHandler(fh)
logger.addHandler(sh)

logger.setLevel(logging.DEBUG)  # 取最高级别,如果不设置,默认为warning,再给handler设置debug和info就会无效
# fh.setLevel(logging.DEBUG)
sh.setLevel(logging.INFO)

logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')

