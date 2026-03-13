from datetime import datetime
from tkinter import messagebox


def upload_now(self):
    upload_view = self._get_active_upload_view()
    if not upload_view:
        return

    title = upload_view["title_var"].get().strip()
    category = upload_view["category_var"].get()
    file_path = upload_view.get("selected_file_path")
    if title and category != "Select category":
        if file_path:
            upload_time = datetime.now()
            new_id = self._next_record_id()
            new_record = self._make_record(new_id, title, category, upload_time, "Active")
            self.records.append(new_record)
            self._load_records(self.records)
            self._load_archive_lists()
            self._refresh_summary_cards()
            self.log_entries.append(f"Uploaded {title}")
            self._load_logs()
            upload_view["selected_file_path"] = ""
            upload_view["selected_file_var"].set("No file selected")
            messagebox.showinfo("Upload", "Document uploaded successfully.")
        else:
            self.select_upload_file(self.current_view)
            if not upload_view.get("selected_file_path"):
                messagebox.showwarning("No File", "No file selected.")
    else:
        messagebox.showwarning("Invalid Input", "Please enter a title and select a category.")
