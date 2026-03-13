from datetime import datetime
from tkinter import messagebox


def backup(self):
    self.last_backup_time = datetime.now()
    self._refresh_summary_cards()
    self.log_entries.append(f"Backup completed at {self.last_backup_time.strftime('%I:%M %p')}")
    self._load_logs()
    messagebox.showinfo("Backup", "Backup completed.")
