import tkinter as tk
from tkinter import ttk


def _build_records_panel(self, parent, view_name):
    records_panel = tk.Frame(parent, bg="#ffffff", highlightbackground="#dbe2ea", highlightthickness=1)
    records_panel.grid(row=0, column=0, sticky="nsew", padx=(0, 10))
    records_panel.grid_rowconfigure(2, weight=1)
    records_panel.grid_columnconfigure(0, weight=1)

    header = ttk.Frame(records_panel, style="Panel.TFrame")
    header.grid(row=0, column=0, sticky="ew", padx=18, pady=(18, 10))

    ttk.Label(header, text="Records", style="SectionTitle.TLabel").pack(anchor="w")
    ttk.Label(header, text="Filter, review, upload, and delete records.", style="SectionSub.TLabel").pack(anchor="w", pady=(2, 0))

    filter_row = ttk.Frame(records_panel, style="Panel.TFrame")
    filter_row.grid(row=1, column=0, sticky="ew", padx=18, pady=(0, 12))
    filter_row.grid_columnconfigure(0, weight=2)
    filter_row.grid_columnconfigure(1, weight=1)
    filter_row.grid_columnconfigure(2, weight=1)
    filter_row.grid_columnconfigure(3, weight=0)

    search_var = tk.StringVar()
    category_var = tk.StringVar(value="All Categories")
    status_var = tk.StringVar(value="All Status")

    search_entry = ttk.Entry(filter_row, textvariable=search_var)
    search_entry.grid(row=0, column=0, sticky="ew", padx=(0, 8))
    search_entry.insert(0, "Search document name or ID")
    search_entry.bind("<FocusIn>", self._clear_placeholder)

    ttk.Combobox(
        filter_row,
        textvariable=category_var,
        values=["All Categories", "Clearance", "Residency", "Permit", "Certificate"],
        state="readonly",
    ).grid(row=0, column=1, sticky="ew", padx=8)

    ttk.Combobox(
        filter_row,
        textvariable=status_var,
        values=["All Status", "Active", "Pending Backup"],
        state="readonly",
    ).grid(row=0, column=2, sticky="ew", padx=8)

    ttk.Button(filter_row, text="Apply", style="Blue.TButton", command=self.apply_filters).grid(row=0, column=3, padx=(8, 0))

    table_wrap = ttk.Frame(records_panel, style="Panel.TFrame")
    table_wrap.grid(row=2, column=0, sticky="nsew", padx=18, pady=(0, 18))
    table_wrap.grid_rowconfigure(0, weight=1)
    table_wrap.grid_columnconfigure(0, weight=1)

    columns = ("id", "title", "category", "date", "status")
    tree = ttk.Treeview(table_wrap, columns=columns, show="headings", selectmode="browse")
    tree.grid(row=0, column=0, sticky="nsew")

    headings = {
        "id": "ID",
        "title": "Title",
        "category": "Category",
        "date": "Date",
        "status": "Status",
    }
    widths = {
        "id": 100,
        "title": 360,
        "category": 120,
        "date": 120,
        "status": 140,
    }

    for col in columns:
        tree.heading(col, text=headings[col], anchor="w")
        tree.column(col, width=widths[col], anchor="w")

    scrollbar = ttk.Scrollbar(table_wrap, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    scrollbar.grid(row=0, column=1, sticky="ns")

    actions = ttk.Frame(records_panel, style="Panel.TFrame")
    actions.grid(row=3, column=0, sticky="ew", padx=18, pady=(0, 18))
    ttk.Button(actions, text="View Selected", style="MiniDark.TButton", command=self.view_selected).pack(side="left", padx=(0, 8))
    ttk.Button(actions, text="Archive Selected", style="MiniDark.TButton", command=self.archive).pack(side="left", padx=(0, 8))
    ttk.Button(actions, text="Delete Selected", style="Danger.TButton", command=self.delete_selected).pack(side="left")

    self.record_views[view_name] = {
        "tree": tree,
        "search_var": search_var,
        "category_var": category_var,
        "status_var": status_var,
    }
