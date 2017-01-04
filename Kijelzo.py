# -*- coding: Utf-8 -*-
from Karakterlap.data.frame_foTul_kijelzo import *
from Karakterlap.data.frame_harcertekek import *
from Karakterlap.data.frame_kepzettsegek import *
from Karakterlap.data.frame_pszi_magia import *
from Karakterlap.data.frame_szemelyes import *
from Karakterlap.data.objektumok import *


class KarakterlapAblak(Tk):
    """A karakterlap ablak osztálya"""

    def __init__(self):
        Tk.__init__(self)

        self.tl = None
        self.tl_aktiv = None
        self.bot_frame = None

        globz.kar = karakter.Karakter(self)

        self.title("M.A.G.U.S. karakterlap - Új Törvénykönyv alapján")

        # A frame_top tartalma: 3 további részre tagolódik vízszintesen.
        fotul = FrameFoTulKijelzo(self)
        fotul.grid(row=0, column=0)
        szemelyes = FrameSzemelyes(self)
        szemelyes.grid(row=0, column=1)

        frame_mid = Frame(self)
        frame_mid.grid(row=1, column=0, columnspan=3)

        self.buttons = {}
        for c in ("Harcértékek", "Képzettségek", "Pszi-Mágia"):
            self.buttons[c] = Button(frame_mid, width=24, height=3,
                                     text=c, font=14, bd=5,
                                     command=lambda arg=c: self.init_tl(arg))
            self.buttons[c].pack(side=LEFT)

    def init_tl(self, melyik):
        try:
            self.tl.destroy()
        except AttributeError:
            self.tl_aktiv = None

        if self.tl_aktiv == melyik:
            self.close_tl()
            return

        self.tl = Toplevel(self)
        self.tl.geometry('+100+100')
        for c in self.buttons:
            self.buttons[c].configure(relief=RAISED)
            self.buttons[melyik].configure(relief=SUNKEN)

        self.bot_frame = {"Harcértékek": FrameHarcertekek,
                          "Képzettségek": FrameKepzettsegek,
                          "Pszi-Mágia": FramePsziMagia,
                          }[melyik](self.tl)
        self.bot_frame.pack()

        self.tl.protocol('WM_DELETE_WINDOW', self.close_tl)
        self.tl_aktiv = melyik

    def close_tl(self):
        self.buttons[self.tl_aktiv].configure(relief=RAISED)
        self.tl.destroy()
        self.tl_aktiv = None


if __name__ == '__main__':
    globz.modeflag = "karakterlap"
    globz.rootwin = KarakterlapAblak()
    for tipus in hasznos.slist(resource.fegyverek):
        for fnev in hasznos.slist(resource.fegyverek[tipus]):
            globz.fegyverek[fnev] = Fegyver(globz.kar, tipus, fnev)
    root = KarakterlapAblak()
    root.mainloop()

"""
TODO:
##############################################################################
- frame_pszi_magia-ban meg kell csinálni a fokokat és képzettségeket, hogy ugyan
azon a var-on legyenek, mint a másik frame-en.
- Képzettségek toplevelben rosszul működik a Kp visszanyerés
- A harcérték-növelések Toplevelben vhogy reprezentálni kéne a maradék KAP-ok
számát.
- Az említett pontoknál figyelembe kell venni a képzettségekből adódó bónuszokat,
de oda kell figyelni, mert a képzettség különböző fokai különböző mennyiségű
pontot adnak, így ha 3. szinten valaminek felveszi a 4. fokát és addig 3. fokú
volt, onnantól több bónusz jár. Ezt reset-kor el kell tudni számolni valahogy.
- Be kell állítani a Topleveleket, hogy hová kerüljenek a képernyőn geometry()
metódussal kell, ('+x+y') formátumban kell megadni.
- Harcértékek mellé be kell huzalozni a páncélt és a pajzsot.
- Képzettségeket is be kell huzalozni normálisan!
- Felugró moduloknál a hibaüzenetek hátraküldik a modul főablakát.
Ez csúnya és sokszor a főablak mögé kerül miattuk. Destroy()-olni kellene a
modul ablakát a hibaüzenet után (vagy eliminálni a hülye hibaüzenetet)
- A fegyvereket is meg kellene csinálni, hogy kiválaszthatóak legyenek.

ÉS HÁT IGEN... ÚJRA KÉNE GONDOLNI AZ EGÉSZET:
AZ LENNE A LEGJOBB, HA A KARAKTERRŐL LENNE EGY KIINDULÁSI ÁLLAPOT ELMENTVE,
HA ESETLEG A JÚZER ÚJRA KÍVÁNNÁ OSZTANI MINDEN PONTJÁT, AKKOR LEHESSEN CSINÁLNI
EGY <ULTIMATE RESET ALL>-T ÉS VISSZAÁLLÍTANI MINDENT A KIINDULÁSI ÁLLAPOTBA.
SŐT MÉG JOBB LENNE, HA KÜLÖN TUDNA VISSZA-RESETELNI EGY KIINDULÁSI ÁLLAPOTBA ÉS
KÜLÖN TUDNA VISSZA-RESETELNI ELSŐ SZINTRE, HA ELTÉRNE A KETTŐ EGYMÁSTÓL.
"""
