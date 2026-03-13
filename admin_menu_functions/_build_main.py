from tkinter import ttk


def _build_main(self):
    self._build_header()
    self.summary_cards = ttk.Frame(self.main, style="App.TFrame")
    self.summary_cards.grid(row=1, column=0, sticky="ew", pady=(0, 16))
    self._build_summary_cards()
    self._build_content()
