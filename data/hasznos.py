# -*- coding: cp1250 -*-
"""Néhány kiegészítő osztály és függvény a dolgok leegyszerűsítése végett"""
from tkinter import *


def mod_IntVar(var, x):
    """Módosítja a megadott Tkinter IntVar objektum értékét a megadott x-szel"""
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
        except TclError:  # ha Frame vagy <active>-nál Spinbox (neki <normal>)
            try:
                c.configure(state='normal')
            except TclError:  # ha nem Spinbox, csak Frame lehet
                set_state(c, st)  # annak pedig vannak slave-jei...


def calc_szint(tp):
    """A megadott tp-ből kiszámolja a karakter szintjét"""
    return len([100 * 2 ** i for i in range(0, 21) if 100 * 2 ** i <= tp]) + 1
