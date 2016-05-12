# -*- coding: Utf-8 -*-
"""Karakter osztály: Frame-ből leszármaztatva, így csatolhatok hozzá Tkinter
IntVar és StringVar objektumokat, de nem lesz 'mainloop'-olva."""
from tkinter import *

import data.hasznos as hasznos
import data.objektumok as objektumok
import data.resource as RES
import data.update as update


class Karakter(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        # A KARAKTER SZEMÉLYES ADATAI (Név, kaszt, jellem, stb)
        self.nev = StringVar(value='')
        self.szint = IntVar(value=1)
        self.KAP_szintenkent = 50
        self.KAP = IntVar(value=self.KAP_szintenkent)
        self.TP = IntVar(value=0)

        self.szemelyes_adatok = {}
        for c in RES.szemelyes_adat_nevek:
            self.szemelyes_adatok[c] = StringVar(value=' ')

        self.hatterek = {}
        for c in hasznos.get_sorted_list(RES.hatterek_resource):
            self.hatterek[c] = StringVar(value='0')

        self.faji_bonuszok = None

        # A KARAKTER FŐ TULAJDONSÁGAI (ERŐ, ÜGY, stb)
        self.fo_tulajdonsagok = {}
        self.fo_tulajdonsagok_faji = {}
        self.fo_tulajdonsag_mod = {}
        for c in RES.fo_tulajdonsag_nevek:
            self.fo_tulajdonsagok[c] = IntVar(value=13)
            self.fo_tulajdonsagok_faji[c] = IntVar(value=0)
            self.fo_tulajdonsag_mod[c] = IntVar(value=0)
        self.foTul_eloszthato = IntVar(value=5)
        self.foTul_KAP = IntVar(value=0)

        # Életerő Pontok és Fájdalomtűrési Pontok
        self.ep_max = IntVar(value=0)
        self.fp_max = IntVar(value=0)
        self.ep_akt = IntVar(value=0)
        self.fp_akt = IntVar(value=0)
        self.fp_KAP = IntVar(value=0)  # Fp-re költött KAP-ok száma

        # Képzettség pontok
        self.kp_KAP = IntVar(value=0)  # KAP-ból vásárolt képzettség pontok
        self.kp_alap = IntVar(value=0)  # intelligenciából származó képzettség pontok
        self.kp = IntVar(value=0)  # elosztható képzettség pontok
        self.kp_elkoltott = IntVar(value=0)

        self.kepzettsegek = {}
        for tipus in RES.kepzettsegek:
            for nev, d in RES.kepzettsegek[tipus].items():
                if nev[0] == "!": nev = nev[1:]
                self.kepzettsegek[nev] = \
                    objektumok.Kepzettseg(self, nev, tipus, d[0], d[1], d[2])

        # Pszi és mágia iskola és használat foka
        self.pszi_iskola = StringVar(value=' ')
        self.pszi_fok = self.kepzettsegek["Pszi"].fok
        self.magia_iskola = StringVar(value=' ')

        # Pszi pontok és mágiaellenállás
        self.pszi_max = IntVar(value=self.fo_tulajdonsagok['INT'].get())
        self.pszi_akt = IntVar(value=self.pszi_max.get())
        self.pszi_KAP = IntVar(value=0)
        self.AME = IntVar(value=self.fo_tulajdonsagok['AST'].get())
        self.MME = IntVar(value=self.fo_tulajdonsagok['AKE'].get())

        # Mana pontok
        self.mana_max = IntVar(value=0)
        self.mana_akt = IntVar(value=0)
        self.mana_KAP = IntVar(value=0)

        # Harcértékek
        self.harcertekek_alap = {}
        self.harcertekek_KAP = {}
        for c in RES.harcertekek_resource:
            self.harcertekek_KAP[c] = IntVar(value=0)
            self.harcertekek_alap[c] = IntVar(value=0)
        self.sebzes = StringVar(value='1k3')  # Ideglenessen
        self.sebzes_bonusz = 0

        # FEGYVEREK
        self.fegyverek = []

        # VÉRTEK és PAJZSOK
        self.vertpajzs_sz = {}
        for c in RES.vertpajzs:
            self.vertpajzs_sz[c] = StringVar(value=" ")
        self.vedett_testtajak = {}
        for c in RES.vedett_testtajak:
            self.vedett_testtajak[c] = BooleanVar(value=False)

        self.magia = Magia(self)
        # self.pontok = Pontok(self)

    def update(self):
        self.update_szemelyes()
        self.update_kepz()

    def update_szemelyes(self):
        ######## 1. FAJ FELDOLGOZÁSA ########

        faj = self.szemelyes_adatok["Faj"].get()

        # Faj háttér beállítása
        if faj in ("", " "):
            raise RuntimeError("Hibás adat! faj_update() nem tud így lefutni")
        if faj == "Ember":
            self.hatterek["Faj"].set("0")
        else:
            self.hatterek["Faj"].set("1")

        # Bizonyos fajok könnyebben tanulnak bizonyos képzettségeket
        elony = RES.faji_kepzettseg_elonyok[faj]
        for kepz in elony[:-1]:
            if kepz[0] == "!":
                kepz = kepz[1:]
            kepz_o = self.kepzettsegek[kepz]
            kepz_o.faji_elony = elony[-1]
            if kepz_o.oktatas_fok.get() < elony[-1]:
                kepz_o.oktatas_fok.set(elony[-1])

        ######## 2. KASZT FELDOLGOZÁSA ########

        # Aliasgyártás a jobb átláthatóság végett
        kaszt = self.szemelyes_adatok["Kaszt"].get()
        iskola = self.szemelyes_adatok["Iskola"].get()
        altip = self.szemelyes_adatok["Kaszt altípus"].get()
        hatterek = self.hatterek

        # Ha nincs kitöltve teljesen az adatlap -> elvileg ez sosem futhat
        if ((kaszt or iskola) in ("", " ")) or \
                ((kaszt == "Fejvadász") and (altip in ("", " "))):
            raise RuntimeError("Hibás adat! kaszt_update() nem tud így lefutni")

        # Kasztból adódó "ingyen" hátterek beállítása
        if kaszt in ('Harcművész', 'Kardművész', 'Fejvadász', 'Boszorkány',
                     'Boszorkánymester', 'Tűzvarázsló', 'Varázsló'):
            hatterek['Pszi érzékenység'].set(' ')
        elif kaszt in RES.magiahasznalok:
            hatterek['Mágikus fogékonyság'].set(' ')
        elif kaszt in ('Pap', 'Paplovag'):
            hatterek['Kegyelt'].set(' ')
        elif kaszt == 'Lovag':
            hatterek['Nemesi vér'].set(' ')

        # Szabadúszó kaszt esetén itt van egy kis trükközés.
        if "egyéb" in iskola.lower():
            iskola = "Egyéb " + kaszt.lower()

        # A fejvadász és a tolvaj még kaszt-altípussal is meg van bonyolítva
        if kaszt in ("Fejvadász"):
            iskola = kaszt.capitalize() + " (" + altip.lower() + ")"

        # Ezeknél a kasztoknál nem tér el az induló képzettség iskolánként
        elif kaszt in ("Tolvaj", "Harcművész", "Kardművész",
                       "Boszorkány", "Tűzvarázsló", "Varázsló"):
            iskola = kaszt

        # Kasztból származó oktatás bónuszok beállítása
        for kep in RES.oktatas_bonuszok[iskola]:
            self.kepzettsegek[kep].oktatas_fok.set(4)

        if kaszt == "Tolvaj":
            iskola = kaszt + " (" + altip.lower() + ")"

        # A kaszt induló képzettségeinek beállítása
        for kep, fok in RES.kaszt_indulo_kepzettsegek[iskola].items():
            self.kepzettsegek[kep].fok.set(fok)

        update.full(self)

    def update_kepz(self):
        for kepz in self.kepzettsegek.values():
            for fok, var in kepz.kp_szuks.items():
                var.set(kepz.calc_kp(fok_cel=fok))

    def hail_mary(self):
        import random
        kar = self
        kar.nev.set("Hail Mary")
        for adat_nev in RES.szemelyes_adat_nevek:
            if adat_nev in ("Iskola", "Kaszt altípus", "Isten", "Ország"): continue
            kar.szemelyes_adatok[adat_nev].set(random.choice(RES.szemelyes_adat_sz[adat_nev]))
        update.szemelyes_forrasok(kar)
        osszetett = ("Iskola", "Isten", "Ország")
        for adat_nev in osszetett:
            kar.szemelyes_adatok[adat_nev].set(random.choice(RES.szemelyes_adat_sz[adat_nev]))
        if kar.szemelyes_adatok["Kaszt"].get() in ("Tolvaj", "Fejvadász"):
            kar.szemelyes_adatok["Kaszt altípus"].set(random.choice(RES.szemelyes_adat_sz["Kaszt altípus"]))
        else:
            kar.szemelyes_adatok["Kaszt altípus"].set("Nincs")

        kar.update()

        eloszthato = self.foTul_eloszthato.get()

        if eloszthato < 0:
            for _ in range(5 - eloszthato):
                tul = random.choice(list(kar.fo_tulajdonsagok.values()))
                hasznos.mod_IntVar(tul, -1)
            update.foTul(self)

        for _ in range(self.foTul_eloszthato.get()):
            tul = random.choice(list(self.fo_tulajdonsagok.values()))
            hasznos.mod_IntVar(tul, 1)

        update.foTul(self)

        kar.update()


class Magia:
    "Ez egy információ-konténer"

    def __init__(self, master):
        self.kar = master
        self.update()

    def update(self):
        kaszt = self.kar.szemelyes_adatok["Kaszt"].get()
        self.magiahasznalo = kaszt in RES.magiahasznalok
        self.varazshasznalo = self.magiahasznalo  # csak mert össze-vissza használom
        self.aktiv = self.kar.kepzettsegek["Tapasztalati mágia"].fok.get() >= 3 or \
                     self.kar.kepzettsegek["Magas mágia"].fok.get() >= 3
        self.tapasztalati = kaszt in RES.tapasztalati_magiaformak

        if self.magiahasznalo:
            self.forma = kaszt
            if self.tapasztalati:
                self.kepzettseg = self.kar.kepzettsegek["Tapasztalati mágia"]
            else:
                self.kepzettseg = self.kar.kepzettsegek["Magas mágia"]
        else:
            self.forma = None
            self.kepzettseg = self.kar.kepzettsegek["Tapasztalati mágia"]


##class Pontok(dict):
##    #TODO: befejezni az update metódust és implementálni a bonusz_elkoltott
##    # szótárat
##    def __init__(self, master):
##        dict.__init__(self)
##        self.kar = master
##        self.bonuszok_szintek = {}
##        self.bonusz_elkoltott = {}
##        self.bonusz_kepzettsegek = {}
##        self.KAP  = {}
##        self.alap = {}
##        self.reset()
##
##    def reset(self):
##        for pont in res.pontok:
##            self[pont] = IntVar()
##        self.bonuszok_szintek = \
##            {pont: {i: 0 for i in range(1, 4)}
##             for pont in res.pontok}
##        self.bonusz_elkoltott = \
##            {pont: {i: 0 for i in range(1, 4)}
##             for pont in res.pontok}
##
##        self.bonusz_kepzettsegek = \
##            {pont: res.bonusz_mitmihez[pont]
##             for pont in res.pontok
##             if pont != "mana"}
##
##        self.kar.magia.update()
##        self.bonusz_kepzettsegek["mana"] =\
##            (self.kar.magia.kepzettseg,
##             self.kar.hatterek["Mágikus fogékonyság"])
##        
##        self.KAP = \
##            {pont: 0 for pont in res.pontok}
##        self.alap =
##            {pont: 0 for pont in res.pontok}
##        self.update()
##
##    def bonusz_ossz(self, pont):
##        max_bonusz = 0
##        for mertek, szint in self.bonusz_szintek[pont]:
##            max_bonusz += mertek * szint
##        return max_bonusz
##
##    def elkoltott_bonusz(self, pont):
##        max_elkoltott = 0
##        for pont in self.bonusz_elkoltott.values():
##            max_elkoltott += pont
##        return max_elkoltott
##
##    def bonusz_novekmeny(self, pont):
##        max_bonusz = self.bonusz_ossz(pont)
##        elkoltott = self.elkoltott_bonusz(pont)
##        return max_bonusz - elkoltott
##
##    def KAP_novekmeny(self, pont):
##        return int(self.KAP[pont] / res.pont_KAP_szorzok[pont])
##
##    def max_pont(self, pont):
##        return self.bonusz_novekmeny(pont) +\
##               self.KAP_novekmeny(pont) +\
##               self.alap[pont]
##        
##    def update_alap(self):
##        kar = self.kar
##        self.alap["fp"] =\
##            kar.fo_tulajdonsagok["ÁLL"].get() +\
##            kar.fo_tulajdonsagok["AKE"].get()
##        self.alap["hm"] = 0
##        self.alap["pszi"] =\
##            kar.fo_tulajdonsagok["INT"].get()
##        self.alap["mana"] = 0
##        self.alap["kegy"] = 0
##        self.alap["kp"] = kar.fo_tulajdonsagok["INT"].get()
##
##    def update_pont(self):
##        kar = self.kar
##        for pont in res.pontok:
##            self[pont].set(self.max_pont(pont))
##
##    def noveles(self, pont, mertek, flag_KAP=False):
##        szorzo = res.pont_KAP_szorzok[pont]






if __name__ == '__main__':
    import globz

    root = Tk()
    globz.kar = Karakter(root)
