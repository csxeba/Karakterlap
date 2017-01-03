# -*- coding: Utf-8 -*-
import warnings
from tkinter import *
import tkinter.messagebox as tkmb

from . import globz, hasznos, karakter, resource, update


class FramePsziMagia(Frame):
    """A Pszi és Mágia frame fő konténere"""

    def __init__(self, master):
        Frame.__init__(self, master)

        globz.kar = karakter

        py, bw, rel = 10, 20, RAISED
        self.pszi_frame = FramePszi(self, bd=bw, relief=rel)
        self.pszi_frame.pack()

        if globz.kar.szemelyes_adatok["Kaszt"].get() in resource.magiahasznalok:
            self.magia_frame = FrameMagia(self, bd=bw, relief=rel)
            self.magia_frame.pack()
        else:
            Label(self, bd=bw, relief=rel, font=("Courier New", 10), width=33,
                  text="Ez a karakter nem mágiahasználó!").pack()


class _MainFrame(Frame):
    """A mágia és Pszi Frame-ek ősosztálya"""

    def __init__(self, master, chain, **kw):
        Frame.__init__(self, master, **kw)

        globz.kar = self.master.kar

        self.kepzettsegek = {}

        if chain == "Pszi":
            self.iskola = globz.kar.pszi_iskola
            self.fok = globz.kar.kepzettsegek["Pszi"].fok
            self.max = globz.kar.pszi_max
            self.akt = globz.kar.pszi_akt
            self.kep = globz.kar.pszi_kep
            self.KAP = globz.kar.pszi_KAP
        elif chain == "Mana":
            self.iskola = globz.kar.magia_iskola
            self.fok = globz.kar.magia_fok
            self.max = globz.kar.mana_max
            self.akt = globz.kar.mana_akt
            self.kep = globz.kar.mana_kep
            self.KAP = globz.kar.mana_KAP

        self.update_method = {"Pszi": update.pszi, "Mana": update.mana}[self.chain]
        self.chain = chain
        self.buttons = []

        bw = 2.5
        px, py = 5, 3

        ftop = Frame(self)
        ftop.pack(side=TOP)

        f = Frame(ftop)
        f.pack(side=RIGHT)
        n = 0
        for c in ((self.iskola, 20), (self.fok, 3)):
            l = Label(f, textvar=c[0], bd=bw, relief=RIDGE, bg='white', width=c[1])
            l.bind("<Button-1>", self.set_isk)
            l.grid(row=0, column=n)
            n += 2
        n = 0
        for c in ('{} iskola'.format(chain), 'Fok'):
            Label(f, text=c).grid(row=1, column=n)
            n += 2

        f = Frame(ftop)
        f.pack(side=LEFT)

        # A framet bezáró gomb. Mégsincs rá szükség :( De azért jól néz ki :D
        ######################################################################
        Button(f, text=chain, width=5, font=("Courier", 16, "bold")).pack()  #
        ######################################################################

        fmid = Frame(self)
        fmid.pack()

        f = Frame(fmid)
        f.pack()
        n = 0
        w, px = 3, 3
        for c in (('Max {} pont'.format(chain), 'Képzettségből'),
                  ('Akt {} pont'.format(chain), 'KAP')):
            Label(f, text=c[0], width=13, bd=bw, relief=RIDGE).grid(row=0, column=n, padx=px)
            Label(f, text=c[1], width=13, bd=bw, relief=RIDGE).grid(row=1, column=n, padx=px)
            n += 2

        w = 2
        for c in ((self.max, (0, 1)), (self.akt, (0, 3)),
                  (self.kep, (1, 1)), (self.KAP, (1, 3))):
            Label(f, textvar=c[0], bd=bw, relief=RIDGE, width=w).grid(row=c[1][0], column=c[1][1])

        f = Frame(fmid, bd=bw, relief=RIDGE)
        f.pack(padx=12, pady=3)

        Label(f, text="{}-pont növelése: ".format(chain)).grid(row=2, column=0)
        n = 1
        px = 5
        for c in (('+1', 1), ('+5', 5), ('Mégse', 'mégse')):
            self.buttons.append(Button(f, text=c[0],
                                       command=lambda: self.set_pont(x=c[1])))
            self.buttons[-1].grid(row=2, column=n, padx=px, pady=py)
            if self.fok.get() == 0:
                self.buttons[-1].configure(state=DISABLED)
            n += 1

    def set_isk(self, x=None):
        del x
        hatter_chain = {"Pszi": "Pszi érzékenység", "Mana": "Mágikus fogékonyság"}[self.chain]
        hatter = globz.kar.hatterek[hatter_chain]
        if hatter.get() == '0':
            msg = 'Karakterednek nincs meg a {} háttere.\n'.format(hatter_chain)
            msg += 'Így nem választhatsz iskolát neki!\n'
            msg += 'Megveszed neki most a {} hátteret? (1 KAP)'.format(hatter_chain)
            if tkmb.askyesno('Vigyázz, Kalandozó!', msg):
                hatter.set(1)
                update.kap(globz.kar)
                self.update_method(globz.kar)
            else:
                return

        IskolaToplevel(self)

    def set_pont(self, x=None):
        warnings.warn("Ez a metódus szar. Újra kell írni.")
        multiplier = {"Pszi": 2, "Mana": 3}[self.chain]
        "Kezeli a max pont növelésére irányuló próbálkozásokat. <x> a gomb lenyomásakor generálódik (lamba)"
        if x in (1, 5):  # Ez az ág akkor fut, ha a user növelni akarja a pszi pontjait. <x> 1 lehet vagy 5.
            hasznos.mod_IntVar(self.max, x)  # megnöveljük a widgeten kijelzett értékeket
            hasznos.mod_IntVar(self.KAP, (multiplier * x))  #
            hasznos.mod_IntVar(globz.kar.KAP, (-multiplier * x))  # Levonjuk a növelés árát az elosztható KAPokból.

        elif x == "mégse":  # Ez az ág a "Mégse" gombra való kattintáskor fut.
            hasznos.mod_IntVar(globz.kar.KAP,
                               self.KAP.get())  # Trükkös: vissza kívánjuk állítani az elosztható KAP-ok számát,
            # minden Pszi-pont 2 KAP-ba kerül,
            # így minden elosztott pont 0-ra állítása után 2 elosztható kapot nyerünk vissza,
            # tehát a levonás utáni KAP-ok számához hozzáadjuk a pontokra költött KAP-ok 2X-esét.
            self.KAP.set(0)  # A Karakter objektum megfelelő attribútumát is lenullázzuk.

        else:
            raise RuntimeError("Wrong parameter: {}".format(x))

        self.update_method(globz.kar)


class FramePszi(_MainFrame):
    def __init__(self, master, **kw):
        self.chain = "Pszi"
        _MainFrame.__init__(self, master, self.chain, **kw)

        fbot = Frame(self)
        fbot.pack()

        bw, px, py = 2.5, 5, 3

        f = Frame(fbot, bd=bw, relief=RIDGE)
        f.pack(pady=5)
        n = 1
        px, py = 3, 3
        for c in (globz.kar.AME, globz.kar.MME):
            Label(f, textvar=c, font=('Calibri', 10), bd=bw, relief=RIDGE
                  ).grid(row=0, column=n, padx=px, pady=py)
            n += 2
        n = 0
        for c in ("A", "M"):
            Label(f, text=c + "ME:", font=('Calibri', 14), bd=bw, relief=RIDGE
                  ).grid(row=0, column=n, padx=px, pady=py)
            n += 2


class FrameMagia(_MainFrame):
    def __init__(self, master, **kw):
        self.chain = "Mana"
        _MainFrame.__init__(self, master, self.chain, **kw)


class IskolaToplevel(Toplevel):
    def __init__(self, master):
        Toplevel.__init__(self, master)

        self.chain = self.master.chain
        self.iskola = self.master.iskola
        self.fok = self.master.fok
        self.update_method = self.master.update_method
        self.title(self.chain)

        self.rb_sz = []  # = Radiobutton szintek

        fr_top = Frame(self)
        fr_top.pack()

        bw = 2.5
        fr1 = Frame(fr_top, bd=bw, relief=RIDGE)
        fr1.pack(side=LEFT)

        fo = ("Times New Roman", 16, 'bold')

        for c in {"Pszi": resource.pszi_iskolak,
                  "Mana": resource.magia_iskolak}[self.chain]:
            r = Radiobutton(fr1, text=c, variable=self.iskola, value=c, font=fo, command=self.rb_modifier)
            r.pack(anchor=W, pady=4)

        fr2 = Frame(fr_top, bd=bw, relief=RIDGE)
        fr2.pack(side=RIGHT)

        for c in range(1, 6):
            self.rb_sz.append(Radiobutton(fr2, text=str(c),
                                          variable=self.fok, value=c, font=fo))
            self.rb_sz[-1].pack(anchor=W)
            if self.iskola.get() == ' ':
                self.rb_sz[-1].configure(state=DISABLED)

        fr_bot = Frame(self)
        fr_bot.pack()

        Button(fr_bot, text="OK", command=self.update, width=5).pack(side=LEFT, pady=8)
        Button(fr_bot, text="Törlés", command=self.reset).pack(side=RIGHT, pady=8)

    def update(self):
        self.update_method(globz.kar)
        if self.fok.get() > 0:
            for c in self.master.buttons:
                c.configure(state=ACTIVE)

        # A megfelelő képzettség-változót átállítjuk
        # kepzettseg = None
        if self.chain == "Pszi":
            kepzettseg = globz.kar.kepzettsegek["Pszi"]
        else:
            kepzettseg = ({True: "Tapasztalati mágia", False: "Magasmágia"}
                          [self.iskola.get() in resource.tapasztalai_magiaformak])

        kepzettseg.fok.set(self.fok.get())

    def reset(self):
        """Alapértemezettre állítja vissza a Karakter objektum megfelelő attribútumait."""
        self.iskola.set(' ')  # Ezek a sorok majd függenek a személyes tulajdonságoktól!
        self.fok.set(0)
        self.update_method(globz.kar)
        self.destroy()

    def rb_modifier(self):
        """A különféle iskolák kizárnak bizonyos fok-értékeket. A megfelelő Radiobutton-ok itt deaktiválódnak."""
        for c in self.rb_sz:
            c.configure(state=ACTIVE)
        x = self.iskola.get()
        if x == 'Pyarroni módszer':  # Nincs 5. foka!
            self.rb_sz[4].configure(state=DISABLED)
        elif x in ('Slan út', 'Godoni ösvény', 'Kyr metódus'):  # A többinek pedig nincs első két foka.
            self.rb_sz[0].configure(state=DISABLED)
            self.rb_sz[1].configure(state=DISABLED)
        else:
            assert self.chain == "Mana", "Pszi frame rossz ágba jutott!"


"""
TODO:
- A mágia sok esetben függ a pszi használattól. Ha nincs a karakternek Pszi képzettsége,
akkor meg kellene csinálni, hogy ne tudja felvenni azokat a mágiaformákat (Mozaik, stb?),
amelyeknek feltétele a Pszi valamilyen fokú ismerete.
- Van két karakter attribútum, a <pszi_fok> és a <magia_fok>. Ezeket át kéne vinni
képzettségekbe. Ez nem lesz egyszerű.
- Iskola_Toplevel OK és Törlés gombok csúnyák. Ki kéne húzni szépen az ablak alján őket.
- + apróságok, amiket kommentekbe beirkáltam.

"""
