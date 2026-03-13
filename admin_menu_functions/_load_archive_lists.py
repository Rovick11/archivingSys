import tkinter as tk


def _load_archive_lists(self):
    archived_records = [record for record in self._sorted_records() if record["status"] == "Archived"]
    for archive_list in self.archive_lists.values():
        archive_list.delete(0, tk.END)
        if not archived_records:
            archive_list.insert(tk.END, "No archived files.")
            continue
        for record in archived_records:
            archive_list.insert(
                tk.END,
                f'{record["id"]} | {record["title"]} | {self._format_record_date(record["created_at"])}'
            )

    deleted_records = self._sorted_records(self.deleted_records)
    for deleted_list in self.deleted_lists.values():
        deleted_list.delete(0, tk.END)
        if not deleted_records:
            deleted_list.insert(tk.END, "No deleted files.")
            continue
        for record in deleted_records:
            deleted_list.insert(
                tk.END,
                f'{record["id"]} | {record["title"]} | {self._format_record_date(record["created_at"])}'
            )
