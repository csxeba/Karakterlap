from tkinter import *

from Karakterlap.data import globz
from Karakterlap.data.karakter import Karakter
from Karakterlap.data.frame_szemelyes import FrameSzemelyes
from Karakterlap.data.frame_kepzettsegek import FrameKepzettsegek

tk = Tk()
globz.kar = Karakter(tk)
print("kar created")
globz.kar.hail_mary()
print("hail mary done")
globz.kar.update()
print("update done")

frame = FrameKepzettsegek(tk)
# frame = FrameSzemelyes(tk)


frame.pack()

##counter = 0
##kihagyva = 0
##for kaszt in res.kasztok:
##    if kaszt in ("Fejvadász", "Tolvaj"):
##        continue
##    for iskola in res.iskolak[kaszt]:
##        print(kaszt, "/", iskola)
##        counter += 1
##        globz.kar = kar.Karakter(tk)
##        globz.kar.hail_mary()
##        globz.kar.szemelyes_adatok["Kaszt"].set(kaszt)
##        globz.kar.szemelyes_adatok["Iskola"].set(iskola)
##        globz.kar.update("Személyes")
##
##for kaszt in ("Fejvadász", "Tolvaj"):
##    for iskola in res.iskolak[kaszt]:
##        for altip in res.kaszt_altipusok[kaszt]:
##            print(kaszt, "/", iskola, "/", altip)
##            counter += 1
##            globz.kar = kar.Karakter(tk)
##            globz.kar.hail_mary()
##            globz.kar.szemelyes_adatok["Kaszt"].set(kaszt)
##            globz.kar.szemelyes_adatok["Iskola"].set(iskola)
##            globz.kar.szemelyes_adatok["Kaszt altípus"].set(altip)
##            globz.kar.update("Személyes")
##
##print("Teszt vége, tesztelve:", counter)
