import tkinter as tk


def _load_logs(self):
    for logs_list in self.logs_lists.values():
        logs_list.delete(0, tk.END)
        for entry in self.log_entries:
            logs_list.insert(tk.END, f"• {entry}")
