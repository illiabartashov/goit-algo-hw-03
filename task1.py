#Завдання N°1
from datetime import datetime

def get_days_from_today(date_string):
    try:
        parsed_date = datetime.strptime(date_string, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Неправильний формат дати. Використовуйте 'YYYY-MM-DD'.")

    today_date = datetime.today().date()
    target_date = parsed_date.date()

    difference = today_date - target_date

    return difference.days

print(get_days_from_today('2020-01-10'))