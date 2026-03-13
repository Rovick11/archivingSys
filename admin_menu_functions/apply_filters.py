def apply_filters(self):
    record_view = self._get_active_record_view()
    if not record_view:
        return

    query = record_view["search_var"].get().strip().lower()
    category = record_view["category_var"].get()
    status = record_view["status_var"].get()

    filtered = []
    for record in self.records:
        if record["status"] == "Archived":
            continue

        rec_id = record["id"]
        title = record["title"]
        rec_category = record["category"]
        rec_status = record["status"]

        matches_query = (
            not query
            or query == "search document name or id"
            or query in rec_id.lower()
            or query in title.lower()
        )
        matches_category = category == "All Categories" or rec_category == category
        matches_status = status == "All Status" or rec_status == status

        if matches_query and matches_category and matches_status:
            filtered.append(record)

    self._load_records(filtered)
