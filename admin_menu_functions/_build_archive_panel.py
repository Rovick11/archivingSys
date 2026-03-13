import tkinter as tk
from tkinter import ttk


def _build_archive_panel(self, parent):
    ttk.Label(parent, text="Archive / Backup", style="SectionTitle.TLabel").pack(anchor="w", padx=18, pady=(18, 2))
    ttk.Label(parent, text="Manage older files and secure copies.", style="SectionSub.TLabel").pack(anchor="w", padx=18)

    ttk.Label(parent, text="Archived Files", style="SectionTitle.TLabel").pack(anchor="w", padx=18, pady=(14, 6))
    archived_wrap = ttk.Frame(parent, style="Panel.TFrame")
    archived_wrap.pack(fill="both", expand=True, padx=18, pady=(0, 10))
    archived_wrap.grid_rowconfigure(0, weight=1)
    archived_wrap.grid_columnconfigure(0, weight=1)

    archived_list = tk.Listbox(
        archived_wrap,
        font=("Segoe UI", 9),
        bg="#f8fafc",
        fg="#0f172a",
        bd=0,
        highlightthickness=1,
        highlightbackground="#dbe2ea",
        selectbackground="#dbeafe",
        activestyle="none",
    )
    archived_list.grid(row=0, column=0, sticky="nsew")

    archived_scroll = ttk.Scrollbar(archived_wrap, orient="vertical", command=archived_list.yview)
    archived_list.configure(yscrollcommand=archived_scroll.set)
    archived_scroll.grid(row=0, column=1, sticky="ns")
    self.archive_lists[parent] = archived_list

    btns = ttk.Frame(parent, style="Panel.TFrame")
    btns.pack(fill="x", padx=18, pady=(0, 14))

    ttk.Button(btns, text="Restore", style="Light.TButton", command=self.restore).grid(row=0, column=0, sticky="ew", padx=(0, 6))
    ttk.Button(btns, text="Export Logs", style="Light.TButton", command=self.export_logs).grid(row=0, column=1, sticky="ew", padx=(6, 0))

    btns.grid_columnconfigure(0, weight=1)
    btns.grid_columnconfigure(1, weight=1)
