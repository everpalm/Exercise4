import logging
import pack.test_module

logging.basicConfig(level=logging.CRITICAL)
logger = logging.getLogger(__name__)

logger.critical('Display critical infomration')

''' Practice on invoking function '''
pack.test_module.test_invoke('Jaron','Anny')

''' Practice on invoking class '''
acct = pack.test_module.Account('Justin', '123-4567', 1000)
acct.deposit(500)
print acct
