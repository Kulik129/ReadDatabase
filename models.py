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



montero3Door()
