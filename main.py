import random


def santa():
    santas = ['Maria', 'Ivan', 'Anna', 'Khristina', 'Dasha', 'Anatolii', 'Vladimir',
              'Stanislav', 'Evgeniy', 'Ekaterina', 'Tatiana']

    for_who = santas.copy()
    result = {}
    while True:
        random.shuffle(for_who)

        for giver, getter in zip(sorted(santas), for_who):
            if getter == giver:
                continue
            result[giver] = getter

        for g1, g2 in result.items():
            print(f'{g1} -> {g2}')
        return False


if __name__ == '__main__':
    santa()
