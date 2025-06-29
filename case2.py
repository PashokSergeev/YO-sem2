from datetime import datetime, date

# Табло цифр из звёздочек
DIGIT_ART = {
    '0': [" *** ",
          "*   *",
          "*   *",
          "*   *",
          " *** "],
    '1': ["  *  ",
          " **  ",
          "  *  ",
          "  *  ",
          " *** "],
    '2': [" *** ",
          "*   *",
          "   * ",
          "  *  ",
          "*****"],
    '3': ["*****",
          "    *",
          " *** ",
          "    *",
          "*****"],
    '4': ["   * ",
          "  ** ",
          " * * ",
          "*****",
          "   * "],
    '5': ["*****",
          "*    ",
          "**** ",
          "    *",
          "**** "],
    '6': [" *** ",
          "*    ",
          "**** ",
          "*   *",
          " *** "],
    '7': ["*****",
          "    *",
          "   * ",
          "  *  ",
          " *   "],
    '8': [" *** ",
          "*   *",
          " *** ",
          "*   *",
          " *** "],
    '9': [" *** ",
          "*   *",
          " ****",
          "    *",
          " *** "]
}

# Ввод данных пользователя
def input_birth_date():
    day = int(input("Введите день рождения (дд): "))
    month = int(input("Введите месяц рождения (мм): "))
    year = int(input("Введите год рождения (гггг): "))
    return date(year, month, day)

# Определение дня недели
def get_weekday(birth_date):
    days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
    return days[birth_date.weekday()]

# Проверка на високосный год
def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# Возраст пользователя
def calculate_age(birth_date):
    today = date.today()
    age = today.year - birth_date.year
    if (birth_date.month, birth_date.day) > (today.month, today.day):
        age -= 1
    return age

# Вывод даты в табло-формате
def print_date_as_stars(birth_date):
    date_str = birth_date.strftime("%d%m%Y")
    lines = [""] * 5
    for digit in date_str:
        digit_lines = DIGIT_ART[digit]
        for i in range(5):
            lines[i] += digit_lines[i] + "  "
    print("\nДата рождения в виде табло:")
    for line in lines:
        print(line)

# Основная логика
def main():
    birth_date = input_birth_date()
    print("День недели:", get_weekday(birth_date))
    print("Високосный год?" , "Да" if is_leap_year(birth_date.year) else "Нет")
    print("Ваш возраст:", calculate_age(birth_date), "лет")
    print_date_as_stars(birth_date)

# Запуск
if __name__ == "__main__":
    main()
