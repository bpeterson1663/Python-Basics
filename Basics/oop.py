'''Wizard'''

class User:
    '''User Class'''
    def __init__(self, name):
        self.name = name
    def sign_in(self):
        '''User logged in'''
        print('logged in')

    def sign_out(self):
        '''User signed out'''
        print('logged out')

class Wizard(User):
    '''Wizard Class'''
    def shall_not_pass(self):
        '''shall not pass'''
        print('shall not pass')
    def smoke_pipe(self):
        '''smoking pipe'''
        print('smoking pipe')


class PlayerCharacter:
    '''Player Character'''
    membership = True # Class Object Attribute

    def __init__(self, name):
        self._name = name

    @classmethod
    def get_membership(cls):
        '''returns membership'''
        return cls.membership

    @staticmethod # doesn't have access to cls
    def combine_attack(attack_one, attack_two):
        '''combines attacks'''
        return attack_one + attack_two

    def run(self):
        '''player runs'''
        print('ran away')

    def attack(self, hit_point):
        '''attack method'''
        print(f'attacked with {hit_point}')

    def get_name(self):
        '''returns name'''
        return self._name


player1 = PlayerCharacter('Brady')

print(player1.get_name())
print(PlayerCharacter.get_membership())
print(PlayerCharacter.combine_attack(12, 22))

wizard = Wizard('Brady')
wizard.sign_in()
print(wizard.name)
