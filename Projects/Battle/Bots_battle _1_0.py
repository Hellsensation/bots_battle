import random


class Bot:
    def __init__(self, name):
        self.name = name
        self.lvl = 1
        self.__hp = 10
        self.atk = 2
        self.defence = 1
        self.pix_money = 0
        self.energy = 0
        self.def_zone = None
        self.atk_zone = None

    def __str__(self):
        if self.def_zone is None and self.atk_zone is None:
            return f'\nСостояние {self.name}:\nLVL:{self.lvl}\nHP:{self.get_hp()}\nAttack:{self.atk}\n' \
                   f'Defence{self.defence}\n' \
                   f'PixMoney:{self.pix_money}\nEnergy:{self.energy}\n'
        else:
            return f'\nСостояние {self.name}:\nВыбранная область защиты:{self.def_zone}\n' \
                   f'Выбранная область атаки:{self.atk_zone}\n'

    def set_hp(self, score):
        self.__hp += (-score)

    def get_hp(self):
        return self.__hp


def calculate_damage(attacking, defensive):
    if attacking.atk_zone == defensive.def_zone:
        defensive.set_hp(attacking.atk - 2)
        print(f'{defensive.name} отражает удар!!!')
    else:
        defensive.set_hp(attacking.atk)
        print(f'{defensive.name} получает {attacking.atk} урона.')


def battle(player_1, player_2):
    choose_attack_zone = int(input('\nВыберите зону для атаки:\n1-Голова\n2-Тело\n3-Ноги\nОтвет: \n'))
    player_1.atk_zone = choose_attack_zone

    enemy_defence_zone = random.randint(1, 3)  # Бот выбирает зону защиты.
    player_2.def_zone = enemy_defence_zone

    calculate_damage(player_1, player_2)

    print(player_1)
    print(player_2)

    choose_defence_zone = int(input('\nВыберите зону для защиты:\n1-Голова\n2-Тело\n3-Ноги\nОтвет: \n'))
    player_1.def_zone = choose_defence_zone

    enemy_atk_zone = random.randint(1, 3)  # Бот выбирает зону атаки.
    player_2.def_zone = enemy_atk_zone

    calculate_damage(player_2, player_1)

    print(player_1)
    print(player_2)


user = Bot('User')
npc = Bot('NPC')
rounds = 0
print(user)
print(npc)

while user.get_hp() > 0 or npc.get_hp() > 0:
    rounds += 1
    print(f'====== Раунд {rounds} ======')
    battle(user, npc)
    print(f'По результатам {rounds} раунда:\nUser HP - {user.get_hp()}\nNPC HP - {npc.get_hp()}')
    if user.get_hp() <= 0:
        print(f'\nПобеду одержал {npc.name}')
        break
    elif npc.get_hp() <= 0:
        print(f'\nПобеду одержал {user.name}')
        break
