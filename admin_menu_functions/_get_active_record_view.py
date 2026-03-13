def _get_active_record_view(self):
    if self.current_view in self.record_views:
        return self.record_views[self.current_view]
    return self.record_views.get("records")
