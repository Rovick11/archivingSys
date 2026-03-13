from tkinter import ttk


def _build_layout(self):
    self.root.grid_columnconfigure(1, weight=1)
    self.root.grid_rowconfigure(0, weight=1)

    self.sidebar = ttk.Frame(self.root, style="Sidebar.TFrame", width=260)
    self.sidebar.grid(row=0, column=0, sticky="ns")
    self.sidebar.grid_propagate(False)
    self._build_sidebar()

    self.main = ttk.Frame(self.root, style="App.TFrame", padding=20)
    self.main.grid(row=0, column=1, sticky="nsew")
    self.main.grid_columnconfigure(0, weight=1)
    self.main.grid_rowconfigure(2, weight=1)
    self._build_main()
