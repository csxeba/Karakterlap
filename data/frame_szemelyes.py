# -*- coding: Utf-8 -*-
from tkinter import *
import tkinter.messagebox as tkmb

import data.resource as RES
import data.hasznos as hasznos
import data.update as update
import data.globz as globz

class Frame_szemelyes(Frame):
    def __init__(self, master, **kw):
        Frame.__init__(self, master, **kw)

        bw = 2.5
        self.configure(bg ="dark grey",relief=RAISED,borderwidth=20)

        frame = Frame(self,width=300,borderwidth=bw,relief=RAISED)
        frame.pack()
        
        Frame_adatok(frame).pack()
        Frame_fptp(self).pack()

class Frame_adatok(Frame):
    def __init__(self, master, **kw):
        Frame.__init__(self, master, **kw)

        bw = 2.5
        # A legfelső részén van a nevet kezelő panel
        name_frame = Frame(self)
        name_frame.pack()
        self.name_label = Label(name_frame,width=40,bd=bw,relief=RIDGE,bg='white',
                                textvariable=globz.kar.nev)
        self.name_label.bind("<Button-1>", self.name_popup)
        self.name_label.pack(side=TOP)
        Label(name_frame,width=40,bd=bw,relief=RAISED,text='Karakter neve'
              ).pack(side=BOTTOM)
        
        # Alatta a személyes adatokat kezelő panel
        f = Frame(self, bd=1)
        f.pack()
        self.szemelyes_labelek = {c: None for c in RES.szemelyes_adat_nevek}
        n = 0
        for c in RES.szemelyes_adat_nevek:
            Label(f,width=11,text=c,bd=bw,relief=RAISED
                  ).grid(row=n,column=0,sticky="news")
            self.szemelyes_labelek[c] = \
                Label(f,bd=4.5,relief=RIDGE,bg='white',width=43,
                      textvar=globz.kar.szemelyes_adatok[c])
            self.szemelyes_labelek[c].bind("<Button-1>", self.adat_popup)
            self.szemelyes_labelek[c].grid(row=n,column=1)

            if c in ("Kaszt altípus", "Iskola", "Isten", "Ország"):
                self.szemelyes_labelek[c].configure(bg="light grey")
            
            n += 1
        Label(f, width=11, text='Hátterek', bd=bw, relief=RAISED
              ).grid(row=n, column=0, sticky = 'news')
        self.hatterek_gomb = Button(f,width=43,text = "Hátterek kiválasztása",command = self.hatterek_popup)
        self.hatterek_gomb.grid(row=n, column=1)

        if not self.check():
            self.hatterek_gomb.configure(state=DISABLED)

        frame = Frame(self,width=300,borderwidth=bw,relief=RAISED)
        frame.pack(side = LEFT)

    def name_popup(self, x):
        name_tl = Toplevel(self)
        name_tl.title("Név beállítása")

        Label(name_tl, width=30, bd=2, relief=RIDGE,
              text="Add meg a karaktered nevét!").pack()
        name_entry = Entry(name_tl, width=35, textvariable=globz.kar.nev)
        name_entry.bind("<Return>", lambda x: name_tl.destroy())
        name_entry.pack()
        f = Frame(name_tl)
        f.pack()
        w = 10
        Button(f, text="OK", width=w,
               command=name_tl.destroy
               ).pack(side=RIGHT)

        name_tl.grab_set()

    def adat_popup(self, event):
        "Előkészíti és példányosítja a személyes adatok beállítását végző toplevelt"
        adatok = globz.kar.szemelyes_adatok
        labelek= self.szemelyes_labelek
        
        # Kinyerjük a beállítandó tulajdonság nevét tartalmazó stringet
        melyik = {val: key
                  for key, val in self.szemelyes_labelek.items()
                  }[event.widget]

        adatok[melyik].set(" ")
        
        kaszt = adatok["Kaszt"].get()
        if melyik == 'Kaszt':
            adatok['Kaszt altípus'].set(' ')
            adatok['Iskola'].set(' ')
            self.hatterek_gomb.configure(state=DISABLED)
            labelek['Kaszt altípus'].configure(bg="light grey")
            labelek['Iskola'].configure(bg="light grey")

        elif melyik in ('Iskola', 'Kaszt altípus'):
            if kaszt == ' ':
                tkmb.showerror("Hiba!", "Előbb kasztot kell választanod!")
                return
            if (melyik == 'Kaszt altípus') and (not RES.kaszt_altipusok[kaszt]):
                tkmb.showwarning("Figyelem!", "Ennek a kasztnak nincsenek altípusai!")
                return

        elif melyik == 'Vallás':
            adatok['Isten'].set(' ')
            labelek['Isten'].configure(bg="light grey")
        elif melyik == "Isten":
            if adatok["Vallás"].get() in ("", " "):
                tkmb.showerror("Hiba!", "Előbb vallást kell választanod!")
                return

        elif melyik == 'Szülőföld':
            adatok['Ország'].set(' ')
            labelek['Ország'].configure(bg="light grey")
        elif melyik == "Ország":
            if adatok["Szülőföld"].get() in ("", " "):
                tkmb.showerror("Hiba!", "Előbb szülőföldet kell választanod!")
                return

        self.tl = Adat_Toplevel(self, melyik)
        self.tl.grab_set()
        
    def hatterek_popup(self):
        tl = Hatterek_toplevel(self)
        tl.grab_set()

    def adat_OK(self):
        "Személyes adatokból jövő KAP levonások (Faj és Kaszt miatt jöhet)"
        adatok = globz.kar.szemelyes_adatok
        hatterek = globz.kar.hatterek
        iskola = adatok["Iskola"].get()
        labelek= self.szemelyes_labelek
        vallas = adatok["Vallás"].get()
        szulofold = adatok["Szülőföld"].get()
        
        levonasok = 0
        if adatok['Faj'].get() in [' ', '', 'Ember']:
            hatterek['Faj'].set(0)
        else:
            hatterek['Faj'].set(1)
            levonasok += 1

        kaszt = globz.kar.szemelyes_adatok["Kaszt"].get()
        if kaszt not in [' ', '']:
            levonasok += RES.kasztok_KAP[kaszt]
            hatterek['Klán, rend, iskola'].set(
                RES.kasztok_KAP[kaszt])
            labelek['Iskola'].configure(bg="white")
            if kaszt in ("Tolvaj", "Fejvadász"):
                labelek['Kaszt altípus'].configure(bg="white")
                if adatok["Kaszt altípus"].get() == "Nincs":
                    adatok["Kaszt altípus"].set(" ")
            else:
                labelek['Kaszt altípus'].configure(bg="light grey")
                adatok["Kaszt altípus"].set("Nincs")
        else:
            labelek['Kaszt altípus'].configure(bg="light grey")
            labelek['Iskola'].configure(bg="light grey")

        globz.kar.KAP_szintenkent = 50 - levonasok
        update.kap(globz.kar)

        if vallas in ("", " "):
            labelek["Isten"].configure(bg="light grey")
        else:
            labelek["Isten"].configure(bg="white")

        if szulofold in ("", " "):
            labelek["Ország"].configure(bg="light grey")
        else:
            labelek["Ország"].configure(bg="white")

        update.szemelyes_forrasok(globz.kar)
            
        if not self.check():
            return

        globz.kar.update()
        self.hatterek_gomb.configure(state=ACTIVE)

    def check(self):
        # A nevet be kell huzalozni ide!
        for chain, var in globz.kar.szemelyes_adatok.items():
            if var.get() == " ":
                return False
        return True

    def randomize(self):
        import random
        kar = globz.kar
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

        self.adat_OK()
        
    
#####################################################################################################################

class Adat_Toplevel(Toplevel):
    def __init__(self, master, melyik):
        Toplevel.__init__(self, master)
        self.master = master
        self.geometry("+250+150")
        self.title(melyik)

        rb_frame = Frame(self)
        rb_frame.pack(fill=X)

        tupl = RES.szemelyes_adat_sz[melyik]
        w = max([len(x) for x in tupl])
        if w < 30: w = 30
        
        for chain in tupl:
            Radiobutton(rb_frame,text=chain,command=self.master.adat_OK,
                        width=w, anchor=W, indicatoron=0, justify=LEFT,
                        variable=\
                        globz.kar.szemelyes_adatok[melyik],
                        value=chain).pack(fill=X)

        gombok = Frame(self, bd=4, relief=RAISED)
        gombok.pack(fill=X)

        bw = 4
        Button(gombok, bd=bw, text="OK", font=16,
               command=self.destroy
               ).pack(fill=X)
        Button(gombok, bd=bw, text="Törlés", font=16,
               command=lambda: self.adat_reset(melyik)
               ).pack(fill=X)

    def adat_reset(self, melyik):
        globz.kar.szemelyes_adatok[melyik].set(' ')
        self.master.hatterek_gomb.configure(state=DISABLED)
        self.master.adat_OK()
        self.destroy()

###########################################################################

class Hatterek_toplevel(Toplevel):
    def __init__(self, master):
        Toplevel.__init__(self, master)

        self.master = master
        res = RES.hatterek_resource
        
        f = Frame(self)
        f.pack()
        
        self.hatter_spinboxok = {} # kulcs a háttér neve (string), érték az azt beállító spinbox.
        for n, c in enumerate(hasznos.get_sorted_list(res)):
            Label(f,bd=3,relief=RIDGE,anchor=W,
                  width=17, text=c
                  ).grid(row=n,column=0,padx=2)

            self.hatter_spinboxok[c] = Spinbox(
                f,from_=0,to=res[c],width=8,exportselection=False,
                textvariable=globz.kar.hatterek[c],
                command=lambda arg=c: self.hatterek_sb(arg))
            
            self.hatter_spinboxok[c].grid(row=n, column=1)

            if c == "Manalátó":
                self.hatter_spinboxok[c].configure(from_=2)
            elif c in ("Faj", "Klán, rend, iskola"):
                self.hatter_spinboxok[c].configure(state=DISABLED)

        f = Frame(self, bd=3, relief=RIDGE)
        f.pack(fill=X)
        px = 2
        w = 8

        Button(f, text="Kész", font=14,
               command=self.destroy).pack(fill=X)

    def hatterek_sb(self, melyik=None):
        "ezt hívja az OK gomb és a spinboxokba kattintás is!"
        update.kap(globz.kar) # ez az elosztható KAP-ot frissíti

        # Ez az IF lehet, hogy felesleges. A fő tulajdonságok állításakor
        # lehetne mindjárt update-elni a hátterek alapján. (végülis csak
        # az adottságból vásárolt elosztható pontok miatt kell ez ide
        if melyik == 'Adottság':
            update.foTul(globz.kar)

class Frame_fptp(Frame):
    def __init__(self, master, **kw):
        Frame.__init__(self, master, **kw)

        bw = 2.5
        kar = globz.kar
        self.configure(bd=bw, relief=RAISED)
        
        frame_tp = Frame(self, bd=bw, relief=RAISED)
        frame_tp.pack(side=LEFT)      

        Label(frame_tp,textvar=globz.kar.szint,bg='light yellow',borderwidth=bw,relief=RIDGE,font=("Courier", 20), width = 3
              ).pack(side=TOP)

        f = Frame(frame_tp)
        f.pack(side=TOP)

        n = 0
        for c in ("TP:", "KAP:"):
            Label(f, text = c).grid(row=n, column=0, pady= 2, sticky = W)
            n += 1

        px,py = 10,4
        self.TP_entry = Entry(f, width = 5, bd=bw, relief=RAISED)
        self.TP_entry.bind("<Return>", self.set_TP)
        self.TP_entry.grid(row=0, column=1, pady= py, padx = px)
        Label(f, width = 5, bd=bw, relief=RAISED, textvar = globz.kar.KAP).grid(row=1, column=1, padx = px, pady = py)

        #Az életerőt kezelő panel
        frame = Frame(self, bd=bw, relief=RAISED)
        frame.pack(side = RIGHT)

        py, px, fs, w = 2, 5, 14, 8
        fo = 'Droid Sans Mono'
        frame_fp_ep = Frame(frame)
        frame_fp_ep.pack()
        for c in (('Ép akt:',0,0), ('Ép max:',1,0), ('Fp akt:',0,2), ('Fp max:',1,2)):
            Label(frame_fp_ep, text = c[0], bd=bw, relief=RIDGE, font=(fo, fs), width=w
                  ).grid(row=c[1],column=c[2], pady=py, padx = px)

        for c in ((globz.kar.ep_akt,0,1), (globz.kar.ep_max,1,1),
                  (globz.kar.fp_akt,0,3), (globz.kar.fp_max,1,3)):
            Label(frame_fp_ep, textvar = c[0], bd = bw, relief = RIDGE,
                  font=(fo,fs)).grid(row=c[1], column=c[2], pady=py, padx = px)

        f = Frame(frame, bd = bw, relief = RIDGE)
        f.pack()
        Label(f, text = "Elköltött KAP:").grid(row=0, column=0)
        Label(f, bd = bw, relief = RIDGE, width = 3, textvar = globz.kar.fp_KAP).grid(row=0, column=1)

        px = 2
        n=2
        w = 6
        for c in (('+1', 1),('+5', 5), ('Nulláz', 'mégse' )):
            Button(f, text=c[0], width=w, command= lambda arg=c[1]: self.fp_nov(arg)
                   ).grid(row=0,column=n,padx = px)
            n += 1

    def set_TP(self, x):
        TP = self.TP_entry.get()
        if not TP: TP = 0
        try: TP = int(TP) # Ez sajnos elkerülhetetlen.
        except ValueError:
            tkmb.showerror('Rossz adat!', 'A TP egy természetes szám kell, hogy legyen!')
        if TP < 0:
            tkmb.showerror('Rossz adat!', 'A TP egy természetes szám kell, hogy legyen!')
        else: globz.kar.TP.set(TP) # Ha miden OK, átadjuk az új TP értéket a Karakter objektumnak,

        # és frissítjük a kijelzett szint-értéket.
        self.TP_entry.delete(0, END)
        self.TP_entry.insert(0, str(globz.kar.TP.get()))

        volt = globz.kar.szint.get()
        globz.kar.szint.set(hasznos.calc_szint(globz.kar.TP.get()))
        lett = globz.kar.szint.get()

        if volt != lett: update.szintlepes(kar, volt, lett)

    def fp_nov(self, x): # fájdalomtűrés???
        raise RuntimeError("Ez a metódus szar. Újra kell írni.")

        # csak a KAP változókat szabad módosítani, méghozzá az elköltött
        # KAP-ok számával, nem a belőlük vásárolt pontok mennyiségével!
        if type(x) == type(1):
            hasznos.mod_IntVar(globz.kar.fp_max, x)
            hasznos.mod_IntVar(globz.kar.fp_KAP, x)
            hasznos.mod_IntVar(globz.kar.KAP, -x)
        else:
            hasznos.mod_IntVar(globz.kar.KAP, globz.kar.fp_KAP.get())
            globz.kar.fp_KAP.set(0)
            globz.kar.fp_max.set(globz.kar.fo_tulajdonsagok['ÁLL'].get() +\
                                globz.kar.fo_tulajdonsagok['AKE'].get())

if __name__ == '__main__':
    import karakter
    root = Tk()
    root.geometry("+250+250")
    globz.kar = karakter.Karakter(root)
    fr = Frame_szemelyes(root)
    fr.pack()
    root.title("frame_top_mid")
    root.mainloop()
        
