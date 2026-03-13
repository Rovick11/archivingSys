from tkinter import ttk


def _build_content(self):
    self.content = ttk.Frame(self.main, style="App.TFrame")
    self.content.grid(row=2, column=0, sticky="nsew")
    self.content.grid_columnconfigure(0, weight=1)
    self.content.grid_rowconfigure(0, weight=1)

    dashboard = ttk.Frame(self.content, style="App.TFrame")
    dashboard.grid(row=0, column=0, sticky="nsew")
    dashboard.grid_columnconfigure(0, weight=3)
    dashboard.grid_columnconfigure(1, weight=2)
    dashboard.grid_rowconfigure(0, weight=1)
    self._build_records_panel(dashboard, "dashboard")
    self._build_right_panels(dashboard, "dashboard")
    self.views["dashboard"] = dashboard

    records = ttk.Frame(self.content, style="App.TFrame")
    records.grid(row=0, column=0, sticky="nsew")
    records.grid_columnconfigure(0, weight=1)
    records.grid_rowconfigure(0, weight=1)
    self._build_records_panel(records, "records")
    self.views["records"] = records

    upload = ttk.Frame(self.content, style="App.TFrame")
    upload.grid(row=0, column=0, sticky="nsew")
    upload.grid_columnconfigure(0, weight=1)
    upload.grid_rowconfigure(0, weight=1)
    upload_box = self._create_box(upload)
    upload_box.grid(row=0, column=0, sticky="nsew")
    self._build_upload_panel(upload_box, "upload")
    self.views["upload"] = upload

    logs = ttk.Frame(self.content, style="App.TFrame")
    logs.grid(row=0, column=0, sticky="nsew")
    logs.grid_columnconfigure(0, weight=1)
    logs.grid_rowconfigure(0, weight=1)
    logs_box = self._create_box(logs)
    logs_box.grid(row=0, column=0, sticky="nsew")
    self._build_logs_panel(logs_box, "logs")
    self.views["logs"] = logs

    deleted = ttk.Frame(self.content, style="App.TFrame")
    deleted.grid(row=0, column=0, sticky="nsew")
    deleted.grid_columnconfigure(0, weight=1)
    deleted.grid_rowconfigure(0, weight=1)
    deleted_box = self._create_box(deleted)
    deleted_box.grid(row=0, column=0, sticky="nsew")
    self._build_deleted_panel(deleted_box, "deleted")
    self.views["deleted"] = deleted

    archive = ttk.Frame(self.content, style="App.TFrame")
    archive.grid(row=0, column=0, sticky="nsew")
    archive.grid_columnconfigure(0, weight=1)
    archive.grid_rowconfigure(0, weight=1)
    archive_box = self._create_box(archive)
    archive_box.grid(row=0, column=0, sticky="nsew")
    self._build_archive_panel(archive_box)
    self.views["archive"] = archive
