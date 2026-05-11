# app.py - Dito ilagay ang actual app code
import ttkbootstrap as tb
from ttkbootstrap.constants import *

class App:
    def __init__(self):
        self.root = tb.Window(title="My App", themename="superhero")
        self.root.geometry("400x300")
        
    def run(self):
        self.root.mainloop()