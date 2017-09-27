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

check_acct = pack.test_module.CheckingAccount('Anny', '123-4567', 100, 'Female')
logger.debug('acct = {}'.format(acct))
logger.debug('check_acct = {}'.format(check_acct))

acct.deposit(500)
#acct.deposit(-100)
check_acct.deposit(100)
logger.debug('acct = {}'.format(acct))
logger.debug('check_acct = {}'.format(check_acct))
logger.debug("{0}'s balance = {1}".format(acct.name, acct.get_balance()))

check_acct.set_gendor('Male')
logger.debug("check_acct = {}".format(check_acct))
