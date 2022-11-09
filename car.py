from bd import suv
from bd import kabriolet
from bd import kross
from bd import kupe
from bd import liftback

def series():
    a = input("Ведите 1 если хотите внедорожник\nВведите 2 если хотите кабриолет\nВедите 3 если хотите кроссовер\nВведите 4 если хотите купе\nВведите 5 если хотите лифтбек\n")
    if a == "1":
        suv()
    elif a == "2":
        kabriolet()
    elif a == "3":
        kross()
    elif a == "4":
        kupe()
    elif a == "5":
        liftback()

