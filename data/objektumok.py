"""Inicializáló fő script"""
from tkinter import *

from . import resource


class Fegyver(Frame):
    def __init__(self, master, tipus, nev):
        Frame.__init__(self, master)
        # Ez egy tuple:(méretkat.,időig.,Sp,KÉ,TÉ/CÉ,VÉ,ár,Lefegyverzés,Fegyvertörés,Átütés)
        res = resource.fegyverek[tipus][nev]
        self.nev = StringVar(value=nev)
        self.meretkategoria = StringVar(value=res[0])
        self.idoigeny = IntVar(value=res[1])
        self.sp = StringVar(value=res[2])
        self.mods = {}
        self.ossz = {}
        n = 3
        for c in resource.harcertekek_resource:  # (KÉ,TÉ,VÉ)
            self.mods[c] = IntVar(value=res[n])
            self.ossz[c] = IntVar(value=0)
            n += 1

        if res[0] != 'táv':
            self.mods['CÉ'].set(0)
            self.ossz['CÉ'].set(0)
        else:
            self.mods['CÉ'].set(self.mods['TÉ'].get())
            self.mods['TÉ'].set(0)

        self.suly = DoubleVar(value=res[6])
        self.ar = StringVar(value=res[7])

        self.lefegyverzes, self.fegyvertores, self.atutes \
            = BooleanVar(value=res[8]), BooleanVar(value=res[9]), BooleanVar(value=res[10])


class Kepzettseg(Frame):
    def __init__(self, master, nev, tipus, neh, kov_k, kov_t):
        Frame.__init__(self, master)
        self.osszetett = False
        if nev[0] == "!":
            self.osszetett = True
            nev = nev[1:]
        self.kar = self.master
        self.nev = StringVar(value=nev)
        self.tipus = StringVar(value=tipus)
        self.nehezseg = IntVar(value=neh)
        self.kovetelmeny_k = kov_k
        self.kovetelmeny_t = kov_t
        self.alcsoport = None
        self.widgetek = None
        self.userdef = False
        self.max_szint = 5
        self.min_szint = 1

        self.kp_alap = {0: 0,
                        1: (1, 1, 2, 3)[neh - 1],
                        2: (3, 5, 8, 10)[neh - 1],
                        3: (8, 10, 15, 20)[neh - 1],
                        4: (15, 20, 30, 35)[neh - 1],
                        5: (25, 30, 45, 55)[neh - 1]}

        self.kp_szuks = dict(zip(self.kp_alap.keys(), [IntVar() for _ in range(6)]))

        self.fok = IntVar(value=0)
        self.oktatas_fok = IntVar(value=0)
        self.faji_elony = 0
        self.kp_rakoltott = 0

        if self.osszetett and (
                    "USERDEF" in resource.kepzettseg_alcsoportok[self.nev.get()]):
            self.userdef = True

        if self.nev in resource.specializalhato_kepzettsegek:
            self.max_szint = 2
        elif "specializáció" in self.nev.get():
            self.min_szint = 3

    def alcsoportok(self, spec):
        if not self.osszetett:
            raise RuntimeError("Ez a képzettség nem összetett:" + self.nev.get())

        res = resource.kepzettseg_alcsoportok[nev[1:]]
        # A SPECIFY flag esetén a választható alcsoportok az "anyaképzettségtől"
        # függenek, így helyben kell lekérdezni őket. Egyébként a resource
        # modulban vannak egy szótárban.
        if "SPECIFY" in res:
            if nev == "Fegyver specializáció":
                return sorted([alcs for alcs in resource.fegyverek[spec]])
            elif nev == "Vallásismeret specializáció":
                return sorted([alcs for alcs in resource.vallasok[spec]])
            else:
                return [alcs for alcs in res if alcs != "USERDEF"]

    def calc_kp(self, fok_cel):
        if self.nehezseg.get() == 0:
            return self.szazalekos(fok_cel)

        fok_akt = self.fok.get()

        if fok_akt >= fok_cel:
            return ""

        if self.kovetelmeny_k:  # ha van képzettség-követelmény
            eros = self.kovetelmeny_k[0]
            if eros:  # ha van erős képzettség-követelmény
                if (not self.master.kepzettsegek[eros]) or\
                        self.master.kepzettsegek[eros].fok.get() <= fok_akt:
                    return "Nem felvehető"  # kisebb a szintje az erős köv-nél.

            if (self.kovetelmeny_k[1]) and \
                    (self.master.kepzettsegek[self.kovetelmeny_k[1]].fok.get() < fok_akt):
                # Ezek a gyenge képzettség-követelmények.
                return "Nem felvehető"

        # Ha nincs képzettség követelmény, vagy mindegyik teljesítve van,
        # kiszámoljuk a szükséges Kp-t a továbblépéshez.
        alap = self.kp_alap[fok_cel]
        try:
            kp = alap - self.kp_alap[fok_akt]
        except KeyError:
            pass
        else:
            kp = alap
        plusz = 0
        if self.kovetelmeny_t:  # Ez a tulajdonság-követelmények miatti pluszpontokat számolja ki
            for c in self.kovetelmeny_t:
                tul = self.master.fo_tulajdonsagok[c].get()
                x = 10 + fok_cel - tul
                if x > 0:
                    plusz += x

        okt = 0
        okt_fok = self.oktatas_fok.get()
        if okt_fok >= fok_cel:  # Ez az oktatás bónuszból fakadó levonást számolja ki
            okt = {1: 1, 2: 1, 3: 1, 4: 2, 5: 3}[okt_fok]

        kp = alap + plusz - okt  # okt pozitív!
        if kp <= 0:
            kp = 1  # A Kp költség minimum 1.

        return kp

    def szazalekos(self, mod):
        return "%"
