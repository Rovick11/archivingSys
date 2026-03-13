from tkinter import messagebox


def restore_deleted(self):
    record = self._get_selected_deleted_record()
    if not record:
        messagebox.showwarning("No Selection", "Please select a deleted record to restore.")
        return

    restored_record = record.copy()
    restored_record["status"] = "Active"
    self.records.append(restored_record)
    self.deleted_records = [item for item in self.deleted_records if item["id"] != record["id"]]
    self._load_records(self.records)
    self._load_archive_lists()
    self._refresh_summary_cards()
    self.log_entries.append(f'Restored deleted file {record["title"]}')
    self._load_logs()
    messagebox.showinfo("Restore", f'Restored: {record["title"]}')
