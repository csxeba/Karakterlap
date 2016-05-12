from tkinter import Frame


class FrameBase(Frame):
    def __init__(self, master, **kwargs):
        Frame.__init__(master, **kwargs)
        self.master = master

    def check(self) -> bool:
        return True
