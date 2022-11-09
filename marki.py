from openpyxl import load_workbook

book = load_workbook(filename="/Users/mitya.kulikbk.ru/Desktop/ДЗ/ДЗ python/8Seminar/Auto.xlsx") 
shet = book.active


def mitsubishi(): 
    cells = shet['B3':'I296']
  
    for ser, marka, model, pokolenie, modif, dvig, kpp, privod in cells:
        print(ser.value, marka.value, model.value, pokolenie.value, modif.value, dvig.value, kpp.value, privod.value)

    a = shet['B699':'I788']
    for ser, marka, model, pokolenie, modif, dvig, kpp, privod in a:
        print(ser.value, marka.value, model.value, pokolenie.value, modif.value, dvig.value, kpp.value, privod.value)

    b = shet['B1128':'I1203']
    for ser, marka, model, pokolenie, modif, dvig, kpp, privod in b:
        print(ser.value, marka.value, model.value, pokolenie.value, modif.value, dvig.value, kpp.value, privod.value)       
    c = shet['B1216':'I1250']
    for ser, marka, model, pokolenie, modif, dvig, kpp, privod in c:
        print(ser.value, marka.value, model.value, pokolenie.value, modif.value, dvig.value, kpp.value, privod.value)     

def bmw():
    cells = shet['B789':'I1127']
    for ser, marka, model, pokolenie, modif, dvig, kpp, privod in cells:
        print(ser.value, marka.value, model.value, pokolenie.value, modif.value, dvig.value, kpp.value, privod.value)

    a = shet['B527':'I698']
    for ser, marka, model, pokolenie, modif, dvig, kpp, privod in a:
        print(ser.value, marka.value, model.value, pokolenie.value, modif.value, dvig.value, kpp.value, privod.value)

    b = shet['B297':'I525']
    for ser, marka, model, pokolenie, modif, dvig, kpp, privod in b:
        print(ser.value, marka.value, model.value, pokolenie.value, modif.value, dvig.value, kpp.value, privod.value)

