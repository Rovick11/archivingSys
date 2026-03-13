def _next_record_id(self):
    numeric_ids = [
        int(record["id"].split("-")[1])
        for record in self.records
        if record["id"].startswith("DOC-") and record["id"].split("-")[1].isdigit()
    ]
    next_number = max(numeric_ids, default=0) + 1
    return f"DOC-{next_number:03d}"
