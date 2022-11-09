from openpyxl import load_workbook

book = load_workbook(filename="/Users/mitya.kulikbk.ru/Desktop/ДЗ/ДЗ python/8Seminar/Auto.xlsx") 
shet = book.active

def pajero(): 
    p = shet['B3':'I17']
  
    for ser, marka, model, pokolenie, modif, dvig, kpp, privod in p:
        print(ser.value, marka.value, model.value, pokolenie.value, modif.value, dvig.value, kpp.value, privod.value)

def pajeroMini(): 
    p = shet['B19':'I32']
  
    for ser, marka, model, pokolenie, modif, dvig, kpp, privod in p:
        print(ser.value, marka.value, model.value, pokolenie.value, modif.value, dvig.value, kpp.value, privod.value)

def pajeroSport(): 
    p = shet['B33':'I58']
  
    for ser, marka, model, pokolenie, modif, dvig, kpp, privod in p:
        print(ser.value, marka.value, model.value, pokolenie.value, modif.value, dvig.value, kpp.value, privod.value)

def montero3Door(): 
    p = shet['B59':'I119']
  
    for ser, marka, model, pokolenie, modif, dvig, kpp, privod in p:
        print(ser.value, marka.value, model.value, pokolenie.value, modif.value, dvig.value, kpp.value, privod.value)

def pajero3Door(): 
    p = shet['B120':'I151']
  
    for ser, marka, model, pokolenie, modif, dvig, kpp, privod in p:
        print(ser.value, marka.value, model.value, pokolenie.value, modif.value, dvig.value, kpp.value, privod.value)

def pajeroMini3Door(): 
    p = shet['B152':'I162']
  
    for ser, marka, model, pokolenie, modif, dvig, kpp, privod in p:
        print(ser.value, marka.value, model.value, pokolenie.value, modif.value, dvig.value, kpp.value, privod.value)

def pajeroPinin3Door(): 
    p = shet['B163':'I168']
  
    for ser, marka, model, pokolenie, modif, dvig, kpp, privod in p:
        print(ser.value, marka.value, model.value, pokolenie.value, modif.value, dvig.value, kpp.value, privod.value)

def pajeroMontero5Door(): 
    p = shet['B169':'I230']
  
    for ser, marka, model, pokolenie, modif, dvig, kpp, privod in p:
        print(ser.value, marka.value, model.value, pokolenie.value, modif.value, dvig.value, kpp.value, privod.value)


def pajero5Door(): 
    p = shet['B231':'I291']
  
    for ser, marka, model, pokolenie, modif, dvig, kpp, privod in p:
        print(ser.value, marka.value, model.value, pokolenie.value, modif.value, dvig.value, kpp.value, privod.value)

def pajeroPinin5Door(): 
    p = shet['B292':'I296']
  
    for ser, marka, model, pokolenie, modif, dvig, kpp, privod in p:
        print(ser.value, marka.value, model.value, pokolenie.value, modif.value, dvig.value, kpp.value, privod.value)

pajeroPinin5Door()
