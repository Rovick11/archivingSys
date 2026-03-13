def _get_selected_deleted_record(self):
    deleted_view = self.deleted_views.get("deleted")
    if not deleted_view:
        return None

    deleted_list = deleted_view["listbox"]
    selection = deleted_list.curselection()
    if not selection:
        return None

    selected_line = deleted_list.get(selection[0])
    selected_id = selected_line.split(" | ")[0]
    for record in self.deleted_records:
        if record["id"] == selected_id:
            return record
    return None
