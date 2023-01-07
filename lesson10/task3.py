# Виберіть будь-яку папку на своєму пк, яка має вложенні директорії. Вивести на прінт
# в термінал її зміст


import pathlib as pt

p = pt.Path('C:/Users/pc/Desktop/заняття/group_10_01/lesson10')


def parse_file(path: pt.Path):
    for el in path.iterdir():
        if el.is_dir():
            parse_file(el)  # C:/Users/pc/Desktop/заняття/group_10_01/lesson9/test/test1
        else:
            print(f'This is file: {el.name}')


if __name__ == "__main__":
    parse_file(p)
