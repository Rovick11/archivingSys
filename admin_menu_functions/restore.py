from tkinter import messagebox


def restore(self):
    archived_records = [record for record in self.records if record["status"] == "Archived"]
    if not archived_records:
        messagebox.showwarning("Restore", "There are no archived records to restore.")
        return

    latest_archived = self._sorted_records(archived_records)[0]
    latest_archived["status"] = "Active"
    self._load_records(self.records)
    self._load_archive_lists()
    self._refresh_summary_cards()
    self.log_entries.append(f'Restored {latest_archived["title"]}')
    self._load_logs()
    messagebox.showinfo("Restore", f'Restored: {latest_archived["title"]}')
