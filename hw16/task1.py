# Пользователь делает вклад в размере a рублей сроком на years лет под 10% годовых (каждый
# год размер его вклада увеличивается на 10%. Эти деньги прибавляются к сумме вклада, и на
# них в следующем году тоже будут проценты).
#
# Написать функцию bank, принимающая аргументы a и years, и возвращающую сумму, которая будет
# на счету пользователя.

def bank(a: float, years: int)-> float:
    procent1 = procent
    idk = 0
    while idk < years:
        a = a * (1 + procent1 / 100)
        idk += 1
    return round(a, 2)
attachments = int(input('вклад: '))
years = int(input('на скок лет?:'))
procent = int(input('под скок % ?: '))
if __name__ == '__main__':
   print (bank(attachments, years))
