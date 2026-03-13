def _format_record_row(self, record):
    return (
        record["id"],
        record["title"],
        record["category"],
        self._format_record_date(record["created_at"]),
        record["status"],
    )
