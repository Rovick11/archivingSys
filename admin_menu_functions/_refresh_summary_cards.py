from datetime import datetime


def _refresh_summary_cards(self):
    today = datetime.now().date()
    total_records = len(self.records)
    uploaded_today = sum(1 for record in self.records if record["created_at"].date() == today)
    archived_files = sum(1 for record in self.records if record["status"] == "Archived")

    self.total_records_var.set(str(total_records))
    self.uploaded_today_var.set(str(uploaded_today))
    self.archived_files_var.set(str(archived_files))
    self.last_backup_var.set(self.last_backup_time.strftime("%b %d, %Y %I:%M %p"))
