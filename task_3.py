import re


def normalize_phone(phone_number):
    cleaned = re.sub(r"[^0-9+]", "", phone_number)
    has_plus = cleaned.startswith("+")
    digits = re.sub(r"[^0-9]", "", cleaned)

    if has_plus:
        return "+" + digits
    if digits.startswith("380"):
        return "+" + digits
    return "+38" + digits


if __name__ == "__main__":
    raw_numbers = [
        "067\t123 4567",
        "(095) 234-5678\n",
        "+380 44 123 4567",
        "380501234567",
        "    +38(050)123-32-34",
        "     0503451234",
        "(050)8889900",
        "38050-111-22-22",
        "38050 111 22 11   ",
    ]
    print([normalize_phone(number) for number in raw_numbers])
