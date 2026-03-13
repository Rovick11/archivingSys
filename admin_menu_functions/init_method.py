import tkinter as tk
from datetime import datetime, timedelta


def __init__(self, root):
    self.root = root
    self.root.title("Admin Dashboard")
    self.root.geometry("1400x860")
    self.root.minsize(1200, 760)
    self.root.configure(bg="#edf1f5")

    self.now = datetime.now()
    self.last_backup_time = self.now
    self.records = [
        self._make_record("DOC-001", "Barangay Clearance - Juan Dela Cruz", "Clearance", self.now - timedelta(days=5, hours=1), "Active"),
        self._make_record("DOC-002", "Certificate of Residency - Maria Santos", "Residency", self.now - timedelta(days=4, hours=2), "Archived"),
        self._make_record("DOC-003", "Business Permit - Pedro Reyes", "Permit", self.now - timedelta(days=3, hours=4), "Active"),
        self._make_record("DOC-004", "Indigency Certificate - Ana Lopez", "Certificate", self.now - timedelta(days=2, hours=3), "Pending Backup"),
        self._make_record("DOC-005", "Cedula - Mark Reyes", "Certificate", self.now - timedelta(days=1, hours=1), "Active"),
        self._make_record("DOC-006", "Barangay Permit - Lea Santos", "Permit", self.now - timedelta(hours=1), "Archived"),
    ]
    self.deleted_records = []

    self.log_entries = [
        "Uploaded Business Permit - Pedro Reyes",
        "Deleted duplicate residency record",
        "Applied filter: Category = Clearance",
        "Archived 12 inactive documents",
        "Backup completed for March records",
    ]
    self.nav_buttons = {}
    self.views = {}
    self.record_views = {}
    self.upload_views = {}
    self.logs_lists = {}
    self.archive_lists = {}
    self.deleted_lists = {}
    self.deleted_views = {}
    self.total_records_var = tk.StringVar()
    self.uploaded_today_var = tk.StringVar()
    self.archived_files_var = tk.StringVar()
    self.last_backup_var = tk.StringVar()
    self.current_view = "records"
    self.header_title_var = tk.StringVar()
    self.header_subtitle_var = tk.StringVar()
    self.view_meta = {
        "dashboard": ("Admin Dashboard", "Overview of records, uploads, logs, and backups."),
        "records": ("Records", "Filter, review, and manage uploaded records."),
        "upload": ("Upload Files", "Add a new document to the system."),
        "logs": ("System Logs", "Review recent admin activities."),
        "archive": ("Archive / Backup", "Manage archived files, restores, and backups."),
        "deleted": ("Deleted Files", "Review, restore, or permanently remove deleted records."),
    }

    self._setup_style()
    self._build_layout()
    self._load_records(self.records)
    self._load_logs()
    self._load_archive_lists()
    self.show_view(self.current_view)
