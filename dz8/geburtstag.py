import datetime

users = [
    {"name": "Billy", "birthday": datetime.date(2023, 8, 14)},
    {"name": "Jecky", "birthday": datetime.date(2023, 8, 14)},
    {"name": "Kim", "birthday": datetime.date(2023, 8, 16)},
    {"name": "Jean", "birthday": datetime.date(2023, 8, 18)},
    {"name": "Tom", "birthday": datetime.date(2023, 8, 15)},
    {"name": "Anna", "birthday": datetime.date(2023, 8, 20)},
]

def get_birthdays_per_week(users):
    today = datetime.date.today()
    weekday = today.weekday()
    birthdays = {i: [] for i in range(7)}

    for user in users:
        birthday = user["birthday"]
        delta = (birthday - today).days
        if 0 <= delta <= 6:
            birthday_weekday = birthday.weekday()
            if birthday_weekday in (5, 6):
                birthdays[0].append(user["name"])
            else:
                birthdays[birthday_weekday].append(user["name"])
                
    for day, names in birthdays.items():
        if names:
            day_name = datetime.date(2023, 8, day + weekday + 1).strftime("%A")
            print(f"{day_name}: {', '.join(names)}")


get_birthdays_per_week(users)

