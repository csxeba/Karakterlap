# -*- coding: Utf-8 -*-
from tkinter import *
import tkinter.messagebox as tkmb
import data.resource as RES
import data.globz as globz


class Frame_foTul_kijelzo(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.configure(relief=RAISED,borderwidth=20)

        bw = 2.5
        frame_top = Frame(self,height=220,width=300,bd=bw,relief=RAISED)
        frame_top.pack()
        
        n = 0
        for c, w in (('Fő tul.', 8), ('Alap', 5), ('Faji', 4), ('Mód.', 4)):
            Label(frame_top, text = c, bd=bw, relief=RIDGE, width=w).grid(row=0,column=n,pady=1)
            n += 1
        self.spinboxok = {}
        n = 1
        for c in RES.fo_tulajdonsag_nevek:
            Label(frame_top, text=c,
                  bd=bw, width=6, relief=RAISED,
                  font="Courier").grid(row=n,column=0)
            Label(frame_top,width=4, bd=bw, relief=RIDGE,
                  textvariable=globz.kar.fo_tulajdonsagok[c]
                  ).grid(row=n,column=1)
            Label(frame_top,width=4,bd=bw,relief=RIDGE,
                  textvariable=globz.kar.fo_tulajdonsagok_faji[c]
                  ).grid(row=n,column=2,padx=3)
            Label(frame_top,width=4,bd=bw,relief=RIDGE,
                  textvariable=globz.kar.fo_tulajdonsag_mod[c]
                  ).grid(row=n,column=3,padx=3)
            n += 1

        # a maradék pontokat kijelző Label
        py = 5
        Label(frame_top,width=9,bd=bw,relief=RAISED,text='Elosztható:'
              ).grid(row=n,column=0,pady=py)
        Label(frame_top,width=3,bd=bw,relief=RIDGE, textvar=globz.kar.foTul_eloszthato
              ).grid(row=n,column=1,pady=py)

        Button(frame_top, width=9, bd=bw,
               text="Szerkesztés", command=self.edit
               ).grid(row=n, column=2, columnspan=4)

    def edit(self):
        import data.frame_foTul as ftm
        self.tl = Toplevel(self)
        self.tl.title("Fő tulajdonságok beállítása")
        
        self.frame = ftm.FoTul_beallitas(self.tl)
        self.frame.pack()
        Button(self.tl, text="Kész", font=("Courier", 16),
               command=self.kesz).pack(fill=X)

        self.tl.grab_set()

    def kesz(self):
        if not self.frame.check():
            tkmb.showerror("Vigyázat!",
                           "Az elosztható pontoknak nullának kell lenniük!")
            return
        else:
            self.tl.destroy()
        
        
if __name__ == '__main__':
    import karakter
    root = Tk()
    globz.rootwin = root
    globz.kar = karakter.Karakter(root)
    frame = Frame_foTul_kijelzo(root)
    frame.pack()
