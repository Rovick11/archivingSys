import os
from tkinter import filedialog


def select_upload_file(self, view_name=None):
    target_view = view_name or self.current_view
    upload_view = self.upload_views.get(target_view)
    if not upload_view and target_view == "dashboard":
        upload_view = self.upload_views.get("dashboard_upload")
    if not upload_view:
        upload_view = self.upload_views.get("upload")
    if not upload_view:
        return

    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf"), ("Image files", "*.jpg *.png")])
    if file_path:
        upload_view["selected_file_path"] = file_path
        upload_view["selected_file_var"].set(os.path.basename(file_path))
