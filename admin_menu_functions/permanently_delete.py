from tkinter import messagebox


def permanently_delete(self):
    record = self._get_selected_deleted_record()
    if not record:
        messagebox.showwarning("No Selection", "Please select a deleted record to permanently delete.")
        return

    confirm = messagebox.askyesno("Permanently Delete", "This action cannot be undone. Continue?")
    if not confirm:
        return

    self.deleted_records = [item for item in self.deleted_records if item["id"] != record["id"]]
    self._load_archive_lists()
    self.log_entries.append(f'Permanently deleted {record["title"]}')
    self._load_logs()
    messagebox.showinfo("Permanently Delete", "Deleted record removed permanently.")
