from datetime import date, datetime, timedelta
from collections import defaultdict


def get_birthdays_per_week(users):
    today = date.today()
    cong_dict = defaultdict(list)
    period_dict = {}
    period = today  # цю змінну прийшлося додати тільки через те шо тест не працює без неї, а взагалі всюди де вказаний period можна було залишити today, 
                    # але тест бере змінну тудей після того як я її змінюю і дата виходить не коректна
    for _ in range(7):
        period_dict[period.day,period.month] = period.year
        period += timedelta(1)
        if period.strftime('%w') == '1': # замість цього можна в 25 рядку просто вказати "Monday" або вказати дату хардово (якесь 05-01-1970)
            after_weekend = period       # але так є прив'язка до конкретної дати, якщо раптом прийдеться програму розвити
   
    for data in users:
        birthday = data['birthday'].replace(year = today.year)
        birthday_dm = data['birthday'].day, data['birthday'].month

        if birthday_dm in list(period_dict):
           
            if birthday.strftime('%w') not in ['0','6']:
                cong_dict[birthday.strftime('%A')].append(data['name'])
            else:
               cong_dict[after_weekend.strftime('%A')].append(data['name'])
  
    return dict(cong_dict)

if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 10, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")