# -*- coding: Utf-8 -*-
import tkinter.messagebox as tkmb
from tkinter import *

import data.globz as globz
import data.hasznos as hasznos
import data.resource as res
import data.update as update


class Frame_kepzettsegek(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        self.frame = None
        self.buttons = {}
        self.aktiv = None

        self.fr_Main = Frame(self, bg='light grey')
        self.fr_Main.pack()

        fr_Buttons = Frame(self.fr_Main)
        fr_Buttons.pack(side=TOP)
        w, h = 10, 1
        for c in ('Harci', 'Alvilági', 'Világi', 'Tudományos', 'Misztikus'):
            self.buttons[c] = Button(fr_Buttons, text=c, width=w, height=h, font='bold',
                                     command=lambda arg=c: self.create_frame(arg))
            self.buttons[c].pack(side=LEFT)

    @staticmethod
    def check():
        update.kap(globz.kar)
        if globz.kar.KAP.get() < 0:
            return False
        else:
            return True

    @staticmethod
    def randomize():
        tkmb.showerror("Debug info", "No Hail Mary yet!")

    def create_frame(self, tipus):
        if tipus == self.aktiv:
            return
        if self.aktiv:  # Ha van aktív Frame, akkor:
            self.buttons[self.aktiv].configure(relief=RAISED)  # a benyomott gombot kiemeljük
            self.frame.destroy()  # Az aktív frame-et megsemmisítjük
            self.aktiv = None  # Ebben tároljuk az aktuális aktív frame-et.
        self.buttons[tipus].configure(relief=SUNKEN)  # Az új frame gombját benyomjuk

        self.aktiv = tipus
        self.frame = Tipus_Frame(self.fr_Main, tipus, bd=3, relief=RIDGE)
        self.frame.pack()


class Tipus_Frame(Frame):
    def __init__(self, master, tipus, **kw):
        Frame.__init__(self, master, **kw)
        bw = 3

        Label(self, text=tipus, font=16
              ).pack()

        f = Frame(self, bd=bw, relief=RAISED)
        f.pack()

        # név, követelmények, kp-költség, fok
        ws = 21, 4, 5, 7, 10

        # Ez a ciklus létrehozza a fejlécet
        for s, w, c in zip(('Képzettség', 'Fok', 'Neh.', 'Oktatás', 'Faji előny'),
                           ws, range(5)):
            Label(f, text=s, width=w, bd=bw, relief=RIDGE).grid(row=0, column=c)

        simak = []
        szazalekosak = []
        for nev in res.kepzettsegek[tipus].keys():
            if "specializáció" in nev:
                continue
            if nev[0] == "!":
                nev = nev[1:]
            if globz.kar.kepzettsegek[nev].nehezseg.get() > 0:
                simak.append(nev)
            else:
                szazalekosak.append(nev)
        rendezett_nevek = sorted(simak) + sorted(szazalekosak)

        # Ez pedig minden képzettség megfelelő sorát
        for rown, nev in enumerate(rendezett_nevek):
            rown += 1

            # Az aktuális képzettség-objektum
            kep = globz.kar.kepzettsegek[nev]
            neh = StringVar(value=("%", "I", "II", "III", "IV")[kep.nehezseg.get()])

            for coln, w, var in zip(range(5), ws,
                                    (kep.nev, kep.fok, neh, kep.oktatas_fok,
                                     kep.faji_elony)):
                Label(f, width=w, bd=bw, relief=RIDGE,
                      textvar=var
                      ).grid(row=rown, column=coln)

            # Végén a beállító-widget
            l = Label(f, text="Módosítás", width=10, bd=bw, relief=RAISED,
                      )
            l.var = kep
            l.grid(row=rown, column=5)
            l.bind("<Button-1>", self.kepz_beallitas)

        Frame_KAP_Kp(self, bd=3, relief=RAISED, width=20
                     ).pack()

    def kepz_beallitas(self, event):
        tl = Kepz_toplevel(self, event.widget.var)
        tl.grab_set()


class Kepz_toplevel(Toplevel):
    def __init__(self, master, kepz):
        Toplevel.__init__(self, master)

        bw = 8

        self.title(kepz.nev.get())

        fejlec = Frame(self, bd=bw, relief=RAISED)
        fejlec.pack()

        h1, h2 = 1, 1
        cw, sw1, sw2 = 36, 13, 4
        f = ("Courier", 18)

        Label(fejlec, font=f, width=cw, bd=bw, relief=RIDGE,
              text=kepz.tipus.get() + " képzettség").pack()
        Label(fejlec, font=f, width=cw, bd=bw, relief=RIDGE,
              textvar=kepz.nev).pack()

        Label(fejlec, font=f, width=(sw1 - 2), bd=bw, relief=RIDGE, anchor=W,
              text="Nehézség:"
              ).pack(side=LEFT)
        Label(fejlec, font=f, width=sw2, bd=bw, relief=RIDGE,
              text=("%", "I", "II", "III", "IV")[kepz.nehezseg.get()]
              ).pack(side=LEFT)
        Label(fejlec, bd=bw, relief=RIDGE, anchor=W, font=f,
              width=sw1, height=h1,
              text="Ismeret foka:"
              ).pack(side=LEFT)
        Label(fejlec, bd=bw, relief=RIDGE, bg='white', font=f,
              width=sw2, height=h2,
              textvar=kepz.fok
              ).pack(side=LEFT)

        frame_kkov = Frame(self, bd=bw, relief=RAISED)
        frame_kkov.pack()

        f = 12

        l = list(kepz.kovetelmeny_k)
        if not l:
            l = (None, None)

        for t, f, k, r in zip(
                ("Erős képzettség-követelmény:", "Gyenge képzettség-követelmény:"),
                (self.get_eros_chain, self.get_gyenge_chain),
                l,
                range(2)):

            Label(frame_kkov, bd=4, relief=RIDGE, anchor=W, font=f,
                  width=26,
                  text=t).grid(row=r, column=0)

            Label(frame_kkov, bd=4, relief=RIDGE, bg='white', anchor=W, font=f,
                  width=18,
                  text=f(kepz)).grid(row=r, column=1)

            Label(frame_kkov, bd=4, relief=RIDGE, anchor=W, font=f,
                  width=5,
                  text="Szint").grid(row=r, column=2)

            if k:
                x = globz.kar.kepzettsegek[k].fok
            else:
                x = StringVar(value=" - ")

            Label(frame_kkov, bd=4, relief=RIDGE, font=f,
                  width=5,
                  textvariable=x
                  ).grid(row=r, column=3)

        kozep = Frame(self)
        kozep.pack()

        frame_tkov = Frame(kozep, bd=bw, relief=RAISED)
        frame_tkov.pack(side=LEFT)

        Label(frame_tkov, bd=3, relief=RAISED, font=f,
              width=30,
              text="Tulajdonság-követelmények"
              ).grid(row=0, column=0, columnspan=3)

        w = 13, 8, 8

        for coln, chain in enumerate(("Tulajdonság", "Érték", "Mód")):
            Label(frame_tkov, width=w[coln], bd=2, relief=RIDGE, font=f,
                  text=chain).grid(row=1, column=coln)

        lst = list(kepz.kovetelmeny_t)
        lst = lst + [None] * (4 - len(lst))
        for rown, tul in enumerate(lst):
            rown += 2
            for coln in range(3):
                if tul:
                    mod = (kepz.fok.get() + 1) - (globz.kar.fo_tulajdonsagok[tul].get() - 10)
                    if mod < 0:
                        mod = 0
                    if coln == 0:
                        x = StringVar(value=lst[rown - 2])
                    elif coln == 1:
                        x = globz.kar.fo_tulajdonsagok[tul]
                    elif coln == 2:
                        x = IntVar(value=mod)
                    else:
                        raise RuntimeError("Valami balul sült el!")
                else:
                    x = StringVar(value=" - ")
                Label(frame_tkov, bd=2, relief=RIDGE, font=f,
                      width=w[coln], height=1,
                      textvariable=x
                      ).grid(row=rown, column=coln)

        frame_kp = Frame(kozep, bd=bw, relief=RAISED)
        frame_kp.pack(side=LEFT)

        Label(frame_kp, bd=3, relief=RAISED, font=f,
              width=25,
              text="Szükséges képzettségpontok"
              ).grid(row=0, column=0, columnspan=3)

        w1, w2 = 15, 10
        for rown in range(5):
            rown += 2
            Label(frame_kp, bd=2, relief=RIDGE, font=f, anchor=W,
                  width=w1, height=1,
                  text=str(rown - 1) + ". fokhoz:"
                  ).grid(row=rown, column=0)
            Label(frame_kp, bd=2, relief=RIDGE, font=f,
                  width=w2, height=1,
                  textvariable=kepz.kp_szuks[rown - 1]  # -2 lenne, de calc_kp miatt meg van keverve ez a szótár... TPD
                  ).grid(row=rown, column=1)

        frame_fejlesztes = Frame(self, bd=bw, relief=RAISED)
        frame_fejlesztes.pack(fill=X)
        self.fok_gombok = {}
        w1, w2 = 25, 5
        for n in range(1, 6):
            Label(frame_fejlesztes, bd=2, relief=RIDGE, font=f, anchor=W,
                  width=w1,
                  text="Képzettség fejlesztése {}. fokra".format(n)
                  ).grid(row=n - 1, column=0)

            self.fok_gombok[n] = \
                Button(frame_fejlesztes, font=f,
                       width=w2,
                       text=n,
                       command=lambda: self.kepzettseg_fejlesztes(kepz, n)
                       ).grid(row=n - 1, column=1)

        # KAP kijelző / Kp vásárló Frame
        frame_KAP_Kp = Frame_KAP_Kp(self, bd=bw, relief=RAISED)
        frame_KAP_Kp.pack()

    @staticmethod
    def kepzettseg_fejlesztes(melyik, fok):
        print(melyik, fok, "TBD...")

    @staticmethod
    def get_gyenge_chain(kep):
        gyenge = ''
        if kep.kovetelmeny_k:
            if kep.kovetelmeny_k[1]:
                gyenge = gyenge + kep.kovetelmeny_k[1]
            else:
                gyenge += 'Nincs'
        else:
            gyenge += "Nincs"
        return gyenge

    @staticmethod
    def get_eros_chain(kep):
        eros = ''
        if kep.kovetelmeny_k:
            if kep.kovetelmeny_k[0]:
                eros = eros + kep.kovetelmeny_k[0]
            else:
                eros += 'Nincs'
        else:
            eros += "Nincs"
        return eros

    @staticmethod
    def get_tul_chain(kep):
        chain = ''
        if kep.kovetelmeny_t:
            for e in kep.kovetelmeny_t:
                chain = chain + e + ", "
            chain = chain[:-2]
        else:
            chain += 'Nincs'
        return chain


class Frame_KAP_Kp(Frame):
    def __init__(self, master, **kw):
        Frame.__init__(self, master, **kw)
        f = ("Courier", 18)

        w = self.cget("width")

        if w:
            w1, w2, w3 = 8, 3, 6
        else:
            w1, w2, w3 = 13, 3, 6

        c = 0
        for c, t in enumerate((StringVar(value="KAP"), globz.kar.KAP,
                               StringVar(value="Kp "), globz.kar.kp)):
            Label(self, bd=2, relief=RIDGE, font=f,
                  width={0: w1, 1: w2}[c % 2],
                  textvariable=t
                  ).grid(row=0, column=c)
        Button(self, bd=4, font=16,
               width=w3,
               text="+1",
               command=self.kp_nov
               ).grid(row=0, column=c + 1)

    @staticmethod
    def kp_nov():
        hasznos.mod_IntVar(globz.kar.kp_KAP, 1)
        update.kp(globz.kar)


if __name__ == '__main__':
    import data.karakter as karakter

    tk = Tk()
    tk.title("Képzettségek")
    globz.kar = karakter.Karakter(tk)
    fr = Frame_kepzettsegek(tk)
    fr.pack()
    tk.mainloop()
