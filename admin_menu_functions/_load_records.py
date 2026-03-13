import tkinter as tk


def _load_records(self, records):
    visible_records = [record for record in records if record["status"] != "Archived"]
    sorted_records = self._sorted_records(visible_records)
    for record_view in self.record_views.values():
        tree = record_view["tree"]
        for item in tree.get_children():
            tree.delete(item)
        for record in sorted_records:
            tree.insert("", tk.END, values=self._format_record_row(record))
