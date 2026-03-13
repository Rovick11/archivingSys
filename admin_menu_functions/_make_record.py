def _make_record(self, record_id, title, category, created_at, status):
    return {
        "id": record_id,
        "title": title,
        "category": category,
        "created_at": created_at,
        "status": status,
    }
