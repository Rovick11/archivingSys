from tkinter import ttk


def _build_right_panels(self, parent, prefix):
    right = ttk.Frame(parent, style="App.TFrame")
    right.grid(row=0, column=1, sticky="nsew")
    right.grid_columnconfigure(0, weight=1)

    upload = self._create_box(right)
    upload.grid(row=0, column=0, sticky="ew", pady=(0, 10))
    self._build_upload_panel(upload, f"{prefix}_upload")

    logs = self._create_box(right)
    logs.grid(row=1, column=0, sticky="nsew", pady=(0, 10))
    right.grid_rowconfigure(1, weight=1)
    self._build_logs_panel(logs, f"{prefix}_logs")

    archive = self._create_box(right)
    archive.grid(row=2, column=0, sticky="ew")
    self._build_archive_panel(archive)
