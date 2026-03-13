from tkinter import messagebox


def delete_selected(self):
    record = self._get_selected_record()
    if record:
        confirm = messagebox.askyesno("Delete Selected", "Are you sure you want to delete the selected record?")
        if confirm:
            self.deleted_records.append(record.copy())
            self.records = [item for item in self.records if item["id"] != record["id"]]
            self._load_records(self.records)
            self._load_archive_lists()
            self._refresh_summary_cards()
            self.log_entries.append(f'Deleted {record["title"]}')
            self._load_logs()
            messagebox.showinfo("Deleted", "Record deleted successfully.")
    else:
        messagebox.showwarning("No Selection", "Please select a record to delete.")
