from tkinter import *
from tkinter import messagebox as tkmb


from . import update, hasznos, globz, resource


class FoTulBeallitas(Frame):
    def __init__(self, master, **kw):
        Frame.__init__(self, master, **kw)

        bw, rel = 10, RAISED

        FoTulFejlec(self, bd=bw, relief=rel).pack()
        FoTulMainframe(self, bd=bw, relief=rel).pack()
        FoTulLablec(self, bd=bw, relief=rel).pack()

    def check(self):
        if globz.kar.foTul_eloszthato.get() == 0:
            return True
        else:
            return False

    def randomize(self):
        import random

        eloszthato = globz.kar.foTul_eloszthato.get()

        if eloszthato <= 0:
            for _ in range(5 - eloszthato):
                tul = random.choice(list(globz.kar.fo_tulajdonsagok.values()))
                hasznos.mod_IntVar(tul, -1)
            update.foTul(globz.kar)

        for _ in range(globz.kar.foTul_eloszthato.get()):
            tul = random.choice(list(globz.kar.fo_tulajdonsagok.values()))
            hasznos.mod_IntVar(tul, 1)

        update.foTul(globz.kar)


class FoTulFejlec(Frame):
    def __init__(self, master, **kw):
        Frame.__init__(self, master, **kw)
        # Elrendezés: [fejléc] + [alul 2 hasáb]
        mww = 51  # Főablak szélessége

        # A cím Label
        Label(self, width=mww, font=("Courier", 16),
              text="A Karakter Fő tulajdonságainak beállítása").pack()


class FoTulMainframe(Frame):
    def __init__(self, master, **kw):
        Frame.__init__(self, master, **kw)

        kar = globz.kar

        main_container = Frame(self)
        main_container.pack()

        left_container = Frame(main_container)
        left_container.pack(side=LEFT)

        right_container = Frame(main_container)
        right_container.pack(side=LEFT)

        bw = 3
        for chain, container in zip(("Fizikai", "Szellemi"),
                                    (left_container, right_container)):

            Label(container, width=36, font=12, bd=bw, relief=RAISED,
                  text=chain + " tulajdonságok"
                  ).pack()
            namesf = Frame(container, bd=bw, relief=RIDGE)
            namesf.pack(fill=X)

            for col, colname in enumerate(('Tul.', 'Faji', 'Mód', 'Alap', 'Csúszka')):
                w = 4
                if colname == 'Csúszka': w = 12
                if colname == 'Tul.': w = 5
                Label(namesf, text=colname, font="Courier",
                      bd=bw, width=w,
                      relief=RAISED
                      ).grid(row=0, column=col)
            w, h = 4, 1
            for rw, tul in enumerate(resource.tulajdonsagok[chain]):
                f = Frame(container, bd=bw, relief=RIDGE)
                f.pack()
                # Erre a button-ra be lehetne kötni valamiféle súgó funkciót
                Button(f, width=6,
                       bd=bw,
                       text=tul
                       ).pack(side=LEFT)
                Label(f, bd=bw, width=w, relief=RAISED, height=h, font="Courier",
                      textvar=kar.fo_tulajdonsagok_faji[tul]
                      ).pack(side=LEFT)
                Label(f, bd=bw, width=w, relief=RAISED, height=h, font="Courier",
                      text="0"
                      ).pack(side=LEFT)
                Label(f, bd=bw, width=w, relief=RAISED, height=h, font="Courier",
                      textvariable=kar.fo_tulajdonsagok[tul]
                      ).pack(side=LEFT)
                Scale(f, width=13, length=120, orient=HORIZONTAL,
                      bd=2, relief=RAISED, showvalue=0,
                      from_=5, to=18 + int(kar.fo_tulajdonsagok_faji[tul].get()),
                      variable=kar.fo_tulajdonsagok[tul],
                      command=lambda x: update.foTul(kar)
                      ).pack(side=LEFT, padx=1)


class FoTulLablec(Frame):
    def __init__(self, master, **kw):
        Frame.__init__(self, master, **kw)

        lframe = Frame(self)
        lframe.pack(side=LEFT)
        Button(lframe, text="Visszaállítás", font=14,
               command=self.reset).pack(fill=X)

        mframe = Frame(self)
        mframe.pack(side=LEFT, padx=38)
        bw, rel = 4, RIDGE
        Label(mframe, bd=bw, relief=rel, font=16,
              text="Fő tulajdonságokra költhető pontok száma:"
              ).pack(side=LEFT)
        Label(mframe, bd=bw, relief=rel, font=20, width=5,
              textvariable=globz.kar.foTul_eloszthato
              ).pack(side=LEFT)

        rframe = Frame(self)
        rframe.pack(side=LEFT)
        Button(self, text="+1 pont (20 KAP)", font=14,
               command=self.pluszpont).pack()

    def reset(self):
        for tul in globz.kar.fo_tulajdonsagok.values():
            tul.set(13)
        globz.kar.foTul_KAP.set(0)
        update.kap(globz.kar)
        update.foTul(globz.kar)

    def pluszpont(self):
        if globz.kar.KAP.get() < 20:
            tkmb.showerror("Vigyázat", "Nincs elég Karakteralkotó Pontod!")
            return
        hasznos.mod_IntVar(globz.kar.foTul_KAP, 1)
        update.kap(globz.kar)
        update.foTul(globz.kar)


if __name__ == "__main__":
    import karakter

    root = Tk()
    globz.kar = karakter.Karakter(root)
    update.full(globz.kar)
    globz.kar.hail_mary()
    update.full(globz.kar)
    FoTulBeallitas(root).pack()
