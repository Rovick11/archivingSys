from tkinter import messagebox


def archive(self):
    record = self._get_selected_record()
    if not record:
        messagebox.showwarning("No Selection", "Please select a record to archive.")
        return

    record["status"] = "Archived"
    self._load_records(self.records)
    self._load_archive_lists()
    self._refresh_summary_cards()
    self.log_entries.append(f'Archived {record["title"]}')
    self._load_logs()
    messagebox.showinfo("Archive", "Record archived successfully.")
