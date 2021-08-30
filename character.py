# OOP Notes


class PlayerCharacter:
    # Class Object Attribute
    membership = True

    def __init__(self, name):
        if PlayerCharacter.membership:
            self._name = name

    def run(self):
        print(f'{self._name} ran away')

    def attack_move(self, strength):
        if self.membership:
            print(f'{self._name} attacked with {strength} power')
        else:
            print('Your character membership has been cancelled and no longer has power')

    def cancel_membership(self):
        self.membership = False
        print('Membership has been cancelled')

    @classmethod  # Do not need to instantiate the class to call
    def get_instructions(cls):
        print("Instructions for the game will come to you when you are ready")
        print(f"Membership required: {cls.membership}")

    @staticmethod  # Do not care about the attributes of the class
    def get_result_of_attack(attack, defend):
        result = attack - defend
        print(f'result of the attack {result}')

    @property
    def name(self):
        return self._name


class Wizard(PlayerCharacter):
    def __init__(self, name, attack):
        super().__init__(name)
        self.attack = attack

    def wizard_attack(self):
        print(f'{self._name} attacked with {self.attack}')

    pass


player1 = Wizard('Brady', 100)

player1.run()
player1.attack_move(50)
player1.cancel_membership()
player1.attack_move(50)
Wizard.get_instructions()
Wizard.get_result_of_attack(30, 20)
