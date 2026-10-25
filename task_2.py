import random


def get_numbers_ticket(min, max, quantity):
    if any(type(value) is not int for value in (min, max, quantity)):
        return []

    if not (1 <= min <= max <= 1000):
        return []

    if not (min <= quantity <= max) or quantity > max - min + 1:
        return []

    return sorted(random.sample(range(min, max + 1), quantity))


if __name__ == "__main__":
    print("Ваші лотерейні числа:", get_numbers_ticket(1, 49, 6))
