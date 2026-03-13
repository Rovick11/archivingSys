from tkinter import messagebox


def view_selected(self):
    record = self._get_selected_record()
    if record:
        messagebox.showinfo(
            "View Selected",
            f'Viewing: {record["title"]} (ID: {record["id"]})\n'
            f'Status: {record["status"]}\n'
            f'Date: {self._format_record_date(record["created_at"])}'
        )
    else:
        messagebox.showwarning("No Selection", "Please select a record to view.")
