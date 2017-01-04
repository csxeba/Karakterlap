# -*- coding: cp1250 -*-
"""N�h�ny kieg�sz�t� oszt�ly �s f�ggv�ny a dolgok leegyszer�s�t�se v�gett"""
from tkinter import *


def mod_IntVar(var, x):
    """M�dos�tja a megadott Tkinter IntVar objektum �rt�k�t a megadott x-szel"""
    var.set(var.get() + x)


def slist(dic, values=False):
    if not values:
        li = list(dic.keys())
        li.sort()
    else:
        li = list(dic.values())
        li.sort()
    return li


def remove_key(dic, val):
    return {i: dic[i] for i in dic if i != val}


def set_state(widget, st):
    for c in widget.winfo_children():
        try:
            c.configure(state=st)
        except TclError:  # ha Frame vagy <active>-n�l Spinbox (neki <normal>)
            try:
                c.configure(state='normal')
            except TclError:  # ha nem Spinbox, csak Frame lehet
                set_state(c, st)  # annak pedig vannak slave-jei...


def calc_szint(tp):
    """A megadott tp-b�l kisz�molja a karakter szintj�t"""
    return len([100 * 2 ** i for i in range(0, 21) if 100 * 2 ** i <= tp]) + 1
