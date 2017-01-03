"""A karakterlap újraszervezése karakteralkotás szempontjából.
A változás annyi a megjelenítéshez képest, hogy ez lépésenként végigvezet
a modulokon a megfelelő sorrendben, mintha karakterlapot készítene az ember."""

from data.frame_foTul import *
from data.frame_harcertekek import *
from data.frame_kepzettsegek import *
from data.frame_pszi_magia import *
from data.frame_szemelyes import *
from data.karakter import *

steps = \
    [
        "adatok",
        "fő tulajdonságok",
        "képzettségek",
        "harcértékek",
        "pszi/mágia"
    ]

frame_szotar = \
    {
        "adatok": FrameAdatok,
        "fptp": FrameFpTp,
        "személyes": FrameSzemelyes,
        "fő tulajdonságok": FoTulBeallitas,
        "képzettségek": FrameKepzettsegek,
        "harcértékek": FrameHarcertekek,
        "pszi/mágia": FramePsziMagia
    }


class Root(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("M.A.G.U.S. karakteralkotás - Új Törvénykönyv szabályrendszerben")

        self.step = steps[0]

        globz.kar = Karakter(self)
        update.kornyezet_inicializalasa(globz.kar)
        globz.kar.fegyverek.append(globz.fegyverek["Slan kard"])
        globz.kar.fegyverek.append(globz.fegyverek["Mara-sequor"])
        globz.kar.fegyverek.append(globz.fegyverek["Béltépő"])
        globz.kar.fegyverek.append(globz.fegyverek["Visszacsapó íj"])
        update.full(globz.kar)

        # Felső Frame (Fő Frame)
        self.mainf = Frame(self)
        self.mainf.pack(fill=BOTH)
        ##################

        self.frame = frame_szotar[self.step](self.mainf)
        self.frame.grid(row=0, column=0, sticky=E + W)
        # Alsó Frame (gombokat tartalmazza)
        buttonsf = Frame(self.mainf)
        #####################
        buttonsf.grid(row=1, column=0)

        # Előző gomb
        self.prev = Button(buttonsf, width=12, height=2, bd=5, state=DISABLED,
                           text="Vissza", font=12,
                           command=lambda: self.lepes(-1))
        self.prev.pack(side=LEFT)
        #################

        # Középső KAP kijelző panel
        miniframe = Frame(buttonsf)
        miniframe.pack(side=LEFT, padx=33, fill=X)

        w, bw, rel = 10, 5, RIDGE
        Label(miniframe, width=w, bd=bw, relief=rel,
              textvariable=globz.kar.KAP).pack(side=BOTTOM)
        Label(miniframe, width=w, bd=bw, relief=rel,
              text="KAP").pack(side=BOTTOM)
        ##############################

        # Következő gomb
        self.next = Button(buttonsf, height=2, bd=5, width=12,
                           text="Következő", font=12,
                           command=lambda: self.lepes(1))
        self.next.pack(side=LEFT)
        ##############

        # Random gomb (csak debug esetén)
        Button(self, text="Hail Mary", font=14, bd=5,
               command=self.hail_mary).pack(fill=X)

        # Néhány állandó beállítása
        globz.rootwin = self

    def lepes(self, hova):
        if hova == 1:
            if not self.frame.check():
                tkmb.showerror("Figyelem", "Hiányos adatkitöltés!")
                return

        volt = steps.index(self.step)
        self.step = steps[volt + hova]
        lett = volt + hova

        update.full(globz.kar)

        self.frame.destroy()
        self.frame = frame_szotar[self.step](self.mainf)
        self.frame.grid(row=0, column=0)

        self.prev.configure(state=(ACTIVE if lett else DISABLED))

    def hail_mary(self):
        self.frame.randomize()


if __name__ == '__main__':
    globz.modeflag = "karakteralkotás"
    root = Root()
    root.mainloop()
