from tkinter import ttk


def _build_header(self):
    header = ttk.Frame(self.main, style="App.TFrame")
    header.grid(row=0, column=0, sticky="ew", pady=(0, 16))
    header.grid_columnconfigure(0, weight=1)

    title_box = ttk.Frame(header, style="App.TFrame")
    title_box.grid(row=0, column=0, sticky="w")

    ttk.Label(title_box, textvariable=self.header_title_var, style="Heading.TLabel").pack(anchor="w")
    ttk.Label(title_box, textvariable=self.header_subtitle_var, style="SubHeading.TLabel").pack(anchor="w", pady=(4, 0))

    action_box = ttk.Frame(header, style="App.TFrame")
    action_box.grid(row=0, column=1, sticky="e")
    ttk.Button(action_box, text="Upload Record", style="Primary.TButton", command=self.upload_record).pack(side="left", padx=(0, 10))
    ttk.Button(action_box, text="Create Backup", style="Light.TButton", command=self.create_backup).pack(side="left")
