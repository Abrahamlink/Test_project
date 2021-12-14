import random
from families import families


def santa():
    """
    Secret Santa function
    """
    santas = ['Maria', 'Ivan', 'Anna', 'Khristina', 'Daria', 'Anatolii', 'Vladimir',
              'Stanislav', 'Evgeniy', 'Ekaterina', 'Tatiana']

    for_who = santas.copy()
    result = {}
    while True:
        random.shuffle(for_who)

        # Iterate over givers and getters
        for giver, getter in zip(sorted(santas), for_who):
            # Test on coincidence
            if getter == giver:
                continue

            # Test on family
            for family in families:
                if getter in family and giver in family:
                    continue
            result[giver] = getter

        for g1, g2 in result.items():
            print(f'{g1} -> {g2}')
        return False


if __name__ == '__main__':
    santa()
