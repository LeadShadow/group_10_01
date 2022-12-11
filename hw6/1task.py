# Создайте список years_list, содержащий год, в который вы родились, и каждый
# последующий год вплоть до вашего пятого дня рождения. Например, если вы
# родились в 1980 году, список будет выглядеть так: years_list = [1980, 1981,
# 1982, 1983, 1984, 1985]

year = int(input('Введіть свій рік народження: '))


def get_list_years(year: int) -> list:
    count = 0
    list_years = []
    while count != 6:
        list_years.append(year+count)
        count += 1
    return list_years


if __name__ == "__main__":
    print(get_list_years(year))

