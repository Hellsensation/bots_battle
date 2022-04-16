from typing import ClassVar
import random
from bots import FireBot, WindBot, WaterBot


def calculate_damage(attacking: ClassVar[int], defensive: ClassVar[int]) -> None:
    """
    Функция подсчета урона при обычном ударе. Принимает значения атаки и защиты.
    """

    if attacking.atk_zone == defensive.def_zone:
        defensive.set_hp(attacking.get_atk() // 2)
        print(f'{defensive.get_name()} отражает удар!!!')

    else:

        defensive.set_hp(attacking.get_atk()-defensive.get_defence())
        print(f'{defensive.get_name()} получает {attacking.get_atk()-defensive.get_defence()} урона.')
        attacking.set_energy(5)


def battle(player_1: ClassVar, player_2:ClassVar) -> None:
    """
    Функция отвечающая за поединок. Принимает двух игроков.
    """
    choose_attack_zone = int(input('\nВыберите зону для атаки:\n1-Голова\n2-Тело\n3-Ноги\nОтвет: \n'))
    try:
        if choose_attack_zone not in (1, 2, 3):
            raise IndexError

        player_1.atk_zone = choose_attack_zone

        enemy_defence_zone = random.randint(1, 3)  # Бот выбирает зону защиты.
        player_2.def_zone = enemy_defence_zone

        calculate_damage(player_1, player_2)

        choose_defence_zone = int(input('\nВыберите зону для защиты:\n1-Голова\n2-Тело\n3-Ноги\nОтвет: \n'))
        if choose_defence_zone not in (1, 2, 3):
            raise IndexError
        player_1.def_zone = choose_defence_zone

        enemy_atk_zone = random.randint(1, 3)  # Бот выбирает зону атаки.
        player_2.def_zone = enemy_atk_zone

        calculate_damage(player_2, player_1)

    except IndexError:
        print('Неверное значение')
        battle(player_1, player_2)


def round_design(player_1: ClassVar, player_2: ClassVar):
    while player_1.get_hp() > 0 or player_2.get_hp() > 0:
        global rounds
        rounds += 1
        print(f'====== Раунд {rounds} ======')
        battle(player_1, player_2)
        print(f'\n!!!!!!!!!!!!!!\n'
              f'По результатам {rounds} раунда:\n'
              f'User HP - {player_1.get_hp()}\n'
              f'User energy - {player_1.get_energy()}\n\n'
              f'NPC HP - {player_2.get_hp()}\n'
              f'NPC energy - {player_2.get_energy()}\n'
              f'!!!!!!!!!!!!!!')
        print()
        if player_1.get_hp() <= 0:
            print(f'\nПобеду одержал {player_2.get_name()}')
            break
        elif player_2.get_hp() <= 0:
            print(f'\nПобеду одержал {player_1.get_name()}')
            player_2.get_lvl(1)


rounds = 0

fire_bot = FireBot('Огненный')
water_bot = WaterBot('Водный')
wind_bot = WindBot('Ветреный')

print(fire_bot)
print(water_bot)

round_design(fire_bot, water_bot)



