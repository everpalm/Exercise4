import logging
import unittest

import pack.test_module


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

logger.critical('Display critical infomration')

''' Practice on invoking function '''
pack.test_module.test_invoke('Jaron','Anny')

''' Practice on invoking class '''
acct = pack.test_module.Account('Justin', '123-4567', 1000)
check_acct = pack.test_module.CheckingAccount('123-4567', 'Justin')
acct.deposit(500)
#print(acct)
logger.debug('acct = {}'.format(acct))
logger.debug('check_acct = {}'.format(check_acct))
