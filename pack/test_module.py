
def test_invoke(test_arg1, test_arg2):
    print('my wife is yelling at {}'.format(test_arg1))
    print('nothing is gonna change {}'.format(test_arg2))

class Account:
    def __init__(self, name, number, balance):
        self.name = name
        self.number = number
        self.balance = balance
        
    def deposit(self, amount):
                if amount <= 0:
                    raise ValueError('amount must be positive')
                self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise RuntimeError('balance not enough')
        self.balance -= amount

    def get_balance(self):
        return self.balance

    def __str__(self):
        return 'Account({0}, {1}, {2})'.format(self.name, self.number, self.balance)

    
class CheckingAccount(Account):
    def __init__(self, name, number, balance, gender):
        self.name = name
        self.number = number
        self.balance = balance
        self.gender = gender

    def set_gendor(self, gender):
        self.gender = gender
        #return 'gendor = {}'.format(self.gendor)

    def __str__(self):
        return 'CheckingAccount({0}, {1}, {2}, {3})'.format(self.name, self.number, self.balance, self.gender)
