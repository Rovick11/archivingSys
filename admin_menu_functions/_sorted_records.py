def _sorted_records(self, records=None):
    source = self.records if records is None else records
    return sorted(source, key=lambda record: record["created_at"], reverse=True)
