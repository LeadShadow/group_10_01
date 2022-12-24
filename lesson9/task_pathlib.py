import pathlib as pt

p = pt.Path('C:/Users/pc/Desktop/заняття/group_10_01/lesson9')


def parse_folder(path: pt.Path) -> None:
    for el in path.iterdir():
        if el.is_dir():
            print(f'This is folder {el.name}')
        else:
            print(f'This is file {el.name}')


def parse_file(path: pt.Path):
    for el in path.iterdir():
        if el.is_dir():
            parse_file(el)  # C:/Users/pc/Desktop/заняття/group_10_01/lesson9/test/test1
        else:
            print(f'This is file: {el.name}')


if __name__ == "__main__":
    parse_file(p)
