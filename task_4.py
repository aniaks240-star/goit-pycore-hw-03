from datetime import datetime, timedelta


def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        year = today.year

        try:
            next_birthday = birthday.replace(year=year)
        except ValueError:
            next_birthday = birthday.replace(year=year, day=28)

        if next_birthday < today:
            year += 1
            try:
                next_birthday = birthday.replace(year=year)
            except ValueError:
                next_birthday = birthday.replace(year=year, day=28)

        days_until_birthday = (next_birthday - today).days
        if 0 <= days_until_birthday < 7:
            congratulation_date = next_birthday

            if congratulation_date.weekday() >= 5:
                congratulation_date += timedelta(
                    days=7 - congratulation_date.weekday()
                )

            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d"),
            })

    return upcoming_birthdays


if __name__ == "__main__":
    users = [
        {"name": "John Doe", "birthday": "1985.01.23"},
        {"name": "Jane Smith", "birthday": "1990.01.27"},
    ]
    print("Список привітань на цьому тижні:", get_upcoming_birthdays(users))
