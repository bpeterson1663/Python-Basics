# OOP Notes


class PlayerCharacter:
    # Class Object Attribute
    membership = True

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
        self._name = name
        self.attack = attack

    def wizard_attack(self):
        print(f'{self._name} attacked with {self.attack}')

    pass


class Archer(PlayerCharacter):
    def __init__(self, name, arrows):
        self._name = name
        self.arrows = arrows

    def check_arrows(self):
        print(f'{self.arrows} remaining')

    def run(self):
        print(f'{self._name} ran really fast')


class Hybrid(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Archer.__init__(self, name, arrows)
        Wizard.__init__(self, name, power)


hb1 = Hybrid('Brady The Great', 50, 100)
print(hb1.check_arrows())
hb1.run()


player1 = Wizard('Brady', 100)

player1.run()
player1.attack_move(50)
player1.cancel_membership()
player1.attack_move(50)
Wizard.get_instructions()
Wizard.get_result_of_attack(30, 20)


class SuperList(list):
    def __len__(self):
        return 1000


super_list1 = SuperList()
print(len(super_list1))  # 1000
super_list1.append(5)
print(super_list1[0])  # 5
print(issubclass(SuperList, list))
