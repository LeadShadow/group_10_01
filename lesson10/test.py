# fh = open('test.txt', 'w+')
# fh.close()
with open('test.txt', 'w+', encoding='utf-8') as fh:
    fh.write('Hello')


# Pathlib
# .name, .parent, .is_dir(), .is_file(), .exists(), .unlink(), .suffix, .iterdir(), .glob()


from pathlib import Path

dir = Path('.')

for el in dir.glob('**/*.txt'):
    print(el)


tmp = Path('empty.txt')
tmp.unlink()



