from datetime import date, timedelta
def close_birthday_users(users, start, end):
    now = date.today()
    result = []
    for user in users:
        birthday = user.get('birthday').replace(year=now.year)
        if birthday < now:
            birthday = birthday.replace(year=now.year + 1)
        if now <= birthday <= end:
            result.append(user)
    return result
def get_birthdays_per_week(users):
    WEEKDAYS = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',)
    now = date.today()
    current_week_day = now.weekday()
    if not users:
        return {}
    start_date = now
    end_date = now + timedelta(days=7)
    birthday_users = close_birthday_users(users, start=start_date, end=end_date)
    result_dict = {}
    for user in birthday_users:
        user_birthday = user.get('birthday').replace(year=now.year)
        if user_birthday < now:
            user_birthday = user_birthday.replace(year=now.year + 1)
        user_birthday_weekday = user_birthday.weekday()
        try:
            user_happy_day = WEEKDAYS[user_birthday_weekday]
        except IndexError:
            user_happy_day = WEEKDAYS[0]
        if user_happy_day not in result_dict:
            result_dict[user_happy_day] = []
        result_dict[user_happy_day].append(user.get('name'))
    return result_dict

if __name__ == "__main__":
    users = [
        {
            "name": "John",
            "birthday": (date.today() + timedelta(days=1)),
        },
        {
            "name": "Doe",
            "birthday": (date.today() + timedelta(days=3)),
        },
        {"name": "Alice", "birthday": (date.today() + timedelta(days=-3))},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")