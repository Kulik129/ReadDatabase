from car import series
from marki import mitsubishi
from marki import bmw

while True:
    s = input('Нажмите 1 если хотите выбрать серии авто\nНажмите 2 если хотите выбрать марки\n')
    if s == '1':
        series()

    elif s == '2':
        e = input('Введите 1 если нравиться mitsubishi\nВведите 2 если нравиться BMW\n')
        if e == '1':
            mitsubishi()
        elif e == '2':
            bmw()
