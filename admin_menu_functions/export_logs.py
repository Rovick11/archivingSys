from tkinter import filedialog, messagebox


def export_logs(self):
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            for log in self.log_entries:
                file.write(log + "\n")
        messagebox.showinfo("Export Logs", "Logs exported successfully.")
