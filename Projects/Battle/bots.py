class Bot:
    def __init__(self, name):
        self.__name = name
        self.__lvl = 1
        self.__hp = 100
        self.__atk = 30
        self.__defence = 5
        self.__experience = 0
        self.__energy = 0
        self.def_zone = None
        self.atk_zone = None

    def __str__(self):
        if self.def_zone is None and self.atk_zone is None:
            return f'\nСостояние {self.get_name()}:\n' \
                   f'LVL: {self.get_lvl()}\n' \
                   f'Exp: {self.get_experience()}\n' \
                   f'HP: {self.get_hp()}\n' \
                   f'Attack: {self.get_atk()}\n' \
                   f'Defence: {self.get_defence()}\n' \
                   f'Energy: {self.get_energy()}\n'
        else:
            return f'\nСостояние {self.get_name()}:\n' \
                   f'Выбранная область защиты:{self.def_zone}\n' \
                   f'Выбранная область атаки:{self.atk_zone}\n'

    def set_name(self, name):
        self.__name = name

    def set_lvl(self, score):
        self.__lvl += score

    def set_hp(self, score):
        self.__hp += (-score)

    def set_atk(self, score):
        self.__atk += score

    def set_defence(self, score):
        self.__defence += score

    def set_experience(self, score):
        self.__experience += score

    def set_energy(self, score):
        self.__energy += score

    def get_name(self):
        return self.__name

    def get_lvl(self):
        return self.__lvl

    def get_hp(self):
        return self.__hp

    def get_atk(self):
        return self.__atk

    def get_defence(self):
        return self.__defence

    def get_experience(self):
        return self.__experience

    def get_energy(self):
        return self.__energy


class FireBot(Bot):
    element = 'Огонь'

    def __str__(self):
        super().__str__()
        return f'\nСостояние {self.get_name()}:\n' \
               f'LVL: {self.get_lvl()}\n' \
               f'Exp: {self.get_experience()}\n' \
               f'HP: {self.get_hp()}\n' \
               f'Attack: {self.get_atk()}\n' \
               f'Defence: {self.get_defence()}\n' \
               f'Energy: {self.get_energy()}\n' \
               f'Стихия: {self.element}'


class WaterBot(Bot):
    element = 'Вода'

    def __str__(self):
        super().__str__()
        return f'\nСостояние {self.get_name()}:\n' \
               f'LVL: {self.get_lvl()}\n' \
               f'Exp: {self.get_experience()}\n' \
               f'HP: {self.get_hp()}\n' \
               f'Attack: {self.get_atk()}\n' \
               f'Defence: {self.get_defence()}\n' \
               f'Energy: {self.get_energy()}\n' \
               f'Стихия: {self.element}'


class WindBot(Bot):
    element = 'Ветер'

    def __str__(self):
        super().__str__()
        return f'\nСостояние {self.get_name()}:\n' \
               f'LVL: {self.get_lvl()}\n' \
               f'Exp: {self.get_experience()}\n' \
               f'HP: {self.get_hp()}\n' \
               f'Attack: {self.get_atk()}\n' \
               f'Defence: {self.get_defence()}\n' \
               f'Energy: {self.get_energy()}\n' \
               f'Стихия: {self.element}'
