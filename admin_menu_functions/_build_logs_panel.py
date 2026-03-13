import tkinter as tk
from tkinter import ttk


def _build_logs_panel(self, parent, view_name):
    ttk.Label(parent, text="System Logs", style="SectionTitle.TLabel").pack(anchor="w", padx=18, pady=(18, 2))
    ttk.Label(parent, text="Recent admin activities.", style="SectionSub.TLabel").pack(anchor="w", padx=18)

    container = ttk.Frame(parent, style="Panel.TFrame")
    container.pack(fill="both", expand=True, padx=18, pady=14)
    container.grid_rowconfigure(0, weight=1)
    container.grid_columnconfigure(0, weight=1)

    logs_list = tk.Listbox(
        container,
        font=("Segoe UI", 9),
        bg="#f8fafc",
        fg="#0f172a",
        bd=0,
        highlightthickness=1,
        highlightbackground="#dbe2ea",
        selectbackground="#dbeafe",
        activestyle="none",
    )
    logs_list.grid(row=0, column=0, sticky="nsew")

    scroll = ttk.Scrollbar(container, orient="vertical", command=logs_list.yview)
    logs_list.configure(yscrollcommand=scroll.set)
    scroll.grid(row=0, column=1, sticky="ns")
    self.logs_lists[view_name] = logs_list
