import logging

logging.basicConfig(level=logging.CRITICAL)
logger = logging.getLogger(__name__)

logger.critical('Display critical infomration')
