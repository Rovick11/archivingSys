def _get_selected_record(self):
    record_view = self._get_active_record_view()
    if not record_view:
        return None

    tree = record_view["tree"]
    selected = tree.selection()
    if not selected:
        return None

    selected_values = tree.item(selected[0])["values"]
    if not selected_values:
        return None

    selected_id = selected_values[0]
    for record in self.records:
        if record["id"] == selected_id:
            return record
    return None
