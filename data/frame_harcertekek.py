# -*- coding: Utf-8 -*-
import warnings
from tkinter import *

from . import globz, hasznos, resource, update
from .bases import FrameBase


class FrameHarcertekek(FrameBase):
    def __init__(self, master):
        FrameBase.__init__(self, master, bd=3, relief=RAISED, bg='dark grey')
        self.aktiv = None

        HarcertekFrame(self).pack(side=LEFT)
        VertPajzsFrame(self).pack(side=LEFT)

    def check(self):
        warnings.warn("Unimplemented check() invoked in FrameHarcertekek")
        return 1

    @staticmethod
    def harcertek_noveles(arg):
        """A harcértéket KAP-ből növelő folyamatot levezénylő metódus

        :type arg: tuple
        :param arg: 2-tuple, első eleme a változtatandó harcérték, a második pedig, hogy mennyi az az annyi.
        """
        print("Frame_harcertekek.harcertek_noveles metódus rossz. Újra kell írni.")
        update.hm(globz.kar)
        if (arg[1] == 1) or (arg[1] == 5):
            hasznos.mod_IntVar(globz.kar.harcertekek_KAP[arg[0]], arg[1])
            if globz.kar.HM_kep.get() - arg[1] >= 0:  # Ha van képzettségből származó HM-bónusz
                hasznos.mod_IntVar(globz.kar.HM_kep, -arg[1])  # akkor abból vonjuk le a levonandót
                globz.kar.HM_kep_elhasznalva += arg[1]  # eltároljuk, mennyi ment el bónuszokra

            else:  # Ha nincs bónusz, akkor a KAP-okból megy a HM költsége
                hasznos.mod_IntVar(globz.kar.KAP, (-2 * arg[1]))  # 1 HM = 2 KAP
        else:  # Ez az ág a nullázó
            vissza = globz.kar.harcertekek_KAP[arg[0]].get()
            if globz.kar.HM_kep_elhasznalva:
                vissza -= globz.kar.HM_kep_elhasznalva * 2
                globz.kar.HM_kep_elhasznalva = 0
                globz.kar.kepzettsegek_update()
            hasznos.mod_IntVar(globz.kar.KAP, vissza)
            globz.kar.harcertekek_KAP[arg[0]].set(0)

        update.hm(globz.kar)


class HarcertekFrame(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        frame = Frame(self)
        frame.pack(side=LEFT)

        bw = 3
        frames = []  # Ez a lista tartalmazza a 4 harcérték-frame-et
        n = 0
        for c in ('KÉ', 'TÉ', 'VÉ', 'CÉ'):
            frames.append(Frame(frame, bd=10, relief=RAISED))  # Később grideljük!
            print(c, "lekreálva")

            f = Frame(frames[-1], bd=bw, relief=RIDGE)
            f.pack()
            Label(f, text={'TÉ': 'Támadó', 'VÉ': 'Védő',
                           'KÉ': 'Kezdő', 'CÉ': 'Célzó'
                           }[c] + 'érték alap:',
                  font=14, width=23).grid(row=0, column=0)
            Label(f, textvar=globz.kar.harcertekek_alap[c], width=3, bd=bw, relief=RAISED, anchor=W
                  ).grid(row=0, column=1)

            # Ez a lista tartalmazza az egyes harcérték frame-ek widget-jeit.
            frames1 = []
            m = 0
            for d in globz.kar.fegyverek:
                frames1.append(Frame(frames[-1], bd=bw, relief=RIDGE))
                frames1[-1].pack(padx=3)
                Label(frames1[-1], textvar=d.nev, bd=bw, relief=RIDGE, width=15
                      ).grid(row=m, column=1)
                Label(frames1[-1], text='Mód:').grid(row=m, column=2)
                Label(frames1[-1], textvar=d.mods[c], bd=bw, relief=RAISED, width=3
                      ).grid(row=m, column=3)
                Label(frames1[-1], text='Össz:').grid(row=m, column=4)
                Label(frames1[-1], textvar=d.ossz[c], bd=bw, relief=RAISED, width=3
                      ).grid(row=m, column=5)
                m += 1

            # Minden harcérték-framehez tartozik egy HM vásárló-kezelő izé widgetcsapat
            f = Frame(frames[-1], bd=bw, relief=RIDGE)
            f.pack()
            w = 5
            Label(f, text='KAP-ból vásárolt:', bd=bw, relief=RIDGE, anchor=W
                  ).grid(row=0, column=0)
            Label(f, textvar=globz.kar.harcertekek_KAP[c], bd=bw, relief=RIDGE, width=w
                  ).grid(row=0, column=1)
            Button(f, text='Nulláz',
                   command=lambda arg=(c, 'mégse'): self.master.harcertek_noveles(arg)
                   ).grid(row=0, column=2, columnspan=3)
            Label(f, text=c + ' növelése:', bd=bw, relief=RIDGE, width=13, anchor=W
                  ).grid(row=1, column=0)
            px, w = 0, 5
            m = 1
            for e in (('+1', 1), ('+5', 5)):
                Button(f, text=e[0], width=w,
                       command=lambda arg=(c, e[1]): self.master.harcertek_noveles(arg)
                       ).grid(row=1, column=m, padx=px)
                m += 1
            n += 1

        # Itt gridelem (későbbi variálások miatt)
        px, py = 1, 1
        n = 0
        for c in (frames[0], frames[2]):
            c.grid(row=0, column=n, padx=px, pady=py)
            n += 1
        n = 0
        for c in (frames[1], frames[3]):
            c.grid(row=1, column=n, padx=px, pady=py)
            n += 1


class VertPajzsFrame(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        for c in (("Vértezet", "Max.SFÉ", "Akt.SFÉ", "Vértviselet"),
                  ("Pajzs", "VÉ", "Sebzés", "Pajzshasználat")):
            f = Frame(self, bd=3, relief=RIDGE)
            f.pack()

            Label(f, text=c[0], width=15, font=14).grid(row=0, column=0, columnspan=3)

            n = 1
            for d in ("Típusa", "MGT", c[1], c[2]):
                Label(f, text=d, width=7, bd=3, relief=RIDGE).grid(row=n, column=0)
                Label(f, textvar=globz.kar.vertpajzs_sz[c[0] + " " + d],
                      bg="white", width=15, bd=3, relief=RIDGE).grid(row=n, column=1)
                n += 1

            f = Frame(f)
            f.grid(row=5, column=0, columnspan=3)
            Label(f, text=c[3] + " foka", width=15, bd=3, relief=RIDGE).pack(side=LEFT)
            Label(f, textvar=globz.kar.kepzettsegek[c[3]].fok, width=7, bd=3, relief=RIDGE
                  ).pack(side=LEFT)

        f = Frame(self, bd=3, relief=RIDGE)
        f.pack()

        Label(f, text="Védett testtájak", bd=3, relief=RIDGE, width=23, anchor=N
              ).grid(row=0, column=0, columnspan=2)
        n = 1
        for c in resource.vedett_testtajak:
            Label(f, text=c, width=11, anchor=W).grid(row=n, column=0)
            Checkbutton(f, variable=globz.kar.vedett_testtajak[c]).grid(row=n, column=1)
            n += 1
