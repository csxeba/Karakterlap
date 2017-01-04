import abc
from tkinter import Frame


class FrameBase(abc.ABC, Frame):
    def __init__(self, master, **kwargs):
        Frame.__init__(master, **kwargs)
        self.master = master

    @abc.abstractmethod
    def check(self) -> bool:
        """Absztrakt metódus -> kötelező implementálni a leszármazottakban"""
        return True
