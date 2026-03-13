import tkinter as tk
from tkinter import ttk


def _build_summary_cards(self):
    for i in range(4):
        self.summary_cards.grid_columnconfigure(i, weight=1)

    data = [
        ("Total Records", self.total_records_var),
        ("Uploaded Today", self.uploaded_today_var),
        ("Archived Files", self.archived_files_var),
        ("Last Backup", self.last_backup_var),
    ]

    for i, (title, value) in enumerate(data):
        card = tk.Frame(self.summary_cards, bg="#ffffff", highlightbackground="#dbe2ea", highlightthickness=1)
        card.grid(row=0, column=i, sticky="nsew", padx=(0 if i == 0 else 8, 0), pady=0)
        ttk.Label(card, text=title, style="CardTitle.TLabel").pack(anchor="w", padx=16, pady=(16, 4))
        if isinstance(value, tk.StringVar):
            ttk.Label(card, textvariable=value, style="CardValue.TLabel").pack(anchor="w", padx=16, pady=(0, 16))
        else:
            ttk.Label(card, text=value, style="CardValue.TLabel").pack(anchor="w", padx=16, pady=(0, 16))

    self._refresh_summary_cards()
