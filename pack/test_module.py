import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# This is for testing function
def test_invoke(test_arg1, test_arg2):
    print('my wife is yelling at {}'.format(test_arg1))
    print('nothing is gonna change {}'.format(test_arg2))

# This is for testing class
class Account:
    def __init__(self, name, number, balance):
        self.name = name
        self.number = number
        self.balance = balance
        
    def deposit(self, amount):
        assert amount > 0, 'You son of bitch wanna take away money from me' #Check the usage of assert
        #if amount <= 0:
        #    raise ValueError('amount must be positive')
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise RuntimeError('balance not enough')
        self.balance -= amount

    def __str__(self):
        logger.debug("self.name = {}".format(self.name))
        return 'Account({0}, {1}, {2})'.format(self.name, self.number, self.balance)

''' Practice on inheriting Account '''
class CheckingAccount(Account):
    def __init__(self, name, number, balance, gender):
        self.name = name
        self.number = number
        self.balance = balance
        self.gender = gender
    
    def set_gendor(self, gender):
        self.gender = gender

    def __str__(self):
        return 'CheckingAccount({0}, {1}, {2}, {3})'.format(self.name, self.number, self.balance, self.gender)
