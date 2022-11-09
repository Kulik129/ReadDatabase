from openpyxl import load_workbook

book = load_workbook(filename="/Users/mitya.kulikbk.ru/Desktop/ДЗ/ДЗ python/8Seminar/Auto.xlsx") 
shet = book.active


def suv(): #Внедорожник
    cells = shet['C2':'I296']
    for marka, model, pokolenie, modif, dvig, kpp, privod in cells:
        print(marka.value, model.value, pokolenie.value, modif.value, dvig.value, kpp.value, privod.value)

def kabriolet(): #Кабриолет
    cells = shet['C297':'I526']
    for marka, model, pokolenie, modif, dvig, kpp, privod in cells:
        print(marka.value, model.value, pokolenie.value, modif.value, dvig.value, kpp.value, privod.value)

def kross(): #Кроссовер
    cells = shet['C527':'I788']
    for marka, model, pokolenie, modif, dvig, kpp, privod in cells:
        print(marka.value, model.value, pokolenie.value, modif.value, dvig.value, kpp.value, privod.value)

def kupe(): 
    cells = shet['C789':'I1215']
    for marka, model, pokolenie, modif, dvig, kpp, privod in cells:
        print(marka.value, model.value, pokolenie.value, modif.value, dvig.value, kpp.value, privod.value)


def liftback(): 
    cells = shet['C1216':'I1250']
    for marka, model, pokolenie, modif, dvig, kpp, privod in cells:
        print(marka.value, model.value, pokolenie.value, modif.value, dvig.value, kpp.value, privod.value)

