import tkinter as tk
from tkinter import ttk


def _build_deleted_panel(self, parent, view_name):
    ttk.Label(parent, text="Deleted Files", style="SectionTitle.TLabel").pack(anchor="w", padx=18, pady=(18, 2))
    ttk.Label(parent, text="Restore or permanently delete removed records.", style="SectionSub.TLabel").pack(anchor="w", padx=18)

    deleted_wrap = ttk.Frame(parent, style="Panel.TFrame")
    deleted_wrap.pack(fill="both", expand=True, padx=18, pady=14)
    deleted_wrap.grid_rowconfigure(0, weight=1)
    deleted_wrap.grid_columnconfigure(0, weight=1)

    deleted_list = tk.Listbox(
        deleted_wrap,
        font=("Segoe UI", 9),
        bg="#f8fafc",
        fg="#0f172a",
        bd=0,
        highlightthickness=1,
        highlightbackground="#dbe2ea",
        selectbackground="#dbeafe",
        activestyle="none",
    )
    deleted_list.grid(row=0, column=0, sticky="nsew")

    deleted_scroll = ttk.Scrollbar(deleted_wrap, orient="vertical", command=deleted_list.yview)
    deleted_list.configure(yscrollcommand=deleted_scroll.set)
    deleted_scroll.grid(row=0, column=1, sticky="ns")

    actions = ttk.Frame(parent, style="Panel.TFrame")
    actions.pack(fill="x", padx=18, pady=(0, 18))
    ttk.Button(actions, text="Restore", style="MiniDark.TButton", command=self.restore_deleted).pack(side="left", padx=(0, 8))
    ttk.Button(actions, text="Permanently Delete", style="Danger.TButton", command=self.permanently_delete).pack(side="left")

    self.deleted_views[view_name] = {"listbox": deleted_list}
    self.deleted_lists[view_name] = deleted_list
