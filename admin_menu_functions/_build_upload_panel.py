import tkinter as tk
from tkinter import ttk


def _build_upload_panel(self, parent, view_name):
    ttk.Label(parent, text="Upload Panel", style="SectionTitle.TLabel").pack(anchor="w", padx=18, pady=(18, 2))
    ttk.Label(parent, text="Add a new document to the system.", style="SectionSub.TLabel").pack(anchor="w", padx=18)

    form = ttk.Frame(parent, style="Panel.TFrame")
    form.pack(fill="x", padx=18, pady=14)

    upload_title_var = tk.StringVar()
    upload_category_var = tk.StringVar(value="Select category")
    selected_file_var = tk.StringVar(value="No file selected")

    title_entry = ttk.Entry(form, textvariable=upload_title_var)
    title_entry.pack(fill="x", pady=(0, 10))
    title_entry.insert(0, "Document title")

    category_box = ttk.Combobox(
        form,
        textvariable=upload_category_var,
        values=["Select category", "Clearance", "Residency", "Permit", "Certificate"],
        state="readonly",
    )
    category_box.pack(fill="x", pady=(0, 10))

    drop = tk.Frame(form, bg="#f8fafc", highlightbackground="#cbd5e1", highlightthickness=1)
    drop.pack(fill="x", pady=(0, 12))
    drop.bind("<Button-1>", lambda _event, name=view_name: self.select_upload_file(name))
    drop_title = ttk.Label(drop, text="Drop file here or click to browse", style="SectionTitle.TLabel")
    drop_title.pack(anchor="center", pady=(18, 2))
    drop_types = ttk.Label(drop, text="PDF, JPG, PNG", style="SectionSub.TLabel")
    drop_types.pack(anchor="center", pady=(0, 6))
    drop_file = ttk.Label(drop, textvariable=selected_file_var, style="SectionSub.TLabel")
    drop_file.pack(anchor="center", pady=(0, 18))

    for widget in (drop_title, drop_types, drop_file):
        widget.bind("<Button-1>", lambda _event, name=view_name: self.select_upload_file(name))

    ttk.Button(form, text="Upload Now", style="Blue.TButton", command=self.upload_now).pack(fill="x")

    self.upload_views[view_name] = {
        "title_var": upload_title_var,
        "category_var": upload_category_var,
        "selected_file_var": selected_file_var,
        "selected_file_path": "",
    }
