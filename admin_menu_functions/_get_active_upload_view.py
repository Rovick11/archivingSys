def _get_active_upload_view(self):
    if self.current_view in self.upload_views:
        return self.upload_views[self.current_view]
    if self.current_view == "dashboard":
        return self.upload_views.get("dashboard_upload")
    return self.upload_views.get("upload")
