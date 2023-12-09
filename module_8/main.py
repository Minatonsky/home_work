from datetime import date, timedelta, datetime

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

today = date.today()

def close_birthday_users(users, start, end):
    result = []
    for user in users:
        birthday = user.get('birthday').replace(year=today.year)
        if birthday < today:
            birthday = birthday.replace(year=today.year + 1)
        if today <= birthday <= end:
            result.append(user)
    return result
def get_birthdays_per_week(users):

    now = date.today()

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
            user_happy_day = weekdays[user_birthday_weekday]
        except IndexError:
            user_happy_day = weekdays[0]
        if user_happy_day not in result_dict:
            result_dict[user_happy_day] = []
        result_dict[user_happy_day].append(user.get('name'))
    return result_dict

if __name__ == "__main__":
    users = [
        {"name": "Denys Kuryshko", "birthday": datetime(2023, 12, 9).date()},
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
        {"name": "Bill Gates", "birthday": datetime(2023, 12, 2).date()},
        {"name": "Jan Koum", "birthday": datetime(2023, 12, 5).date()},
        {"name": "Iryna Popovych", "birthday": datetime(2023, 12, 30).date()}
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")