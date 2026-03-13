import tkinter as tk

from admin_menu_functions import (
    app_init,
    apply_filters,
    archive,
    backup,
    create_backup,
    delete_selected,
    export_logs,
    permanently_delete,
    restore,
    restore_deleted,
    select_upload_file,
    show_view,
    upload_now,
    upload_record,
    view_selected,
    _build_archive_panel,
    _build_content,
    _build_deleted_panel,
    _build_header,
    _build_layout,
    _build_logs_panel,
    _build_main,
    _build_records_panel,
    _build_right_panels,
    _build_sidebar,
    _build_summary_cards,
    _build_upload_panel,
    _clear_placeholder,
    _create_box,
    _format_record_date,
    _format_record_row,
    _get_active_record_view,
    _get_active_upload_view,
    _get_selected_deleted_record,
    _get_selected_record,
    _load_archive_lists,
    _load_logs,
    _load_records,
    _make_record,
    _next_record_id,
    _refresh_summary_cards,
    _setup_style,
    _sorted_records,
)


class AdminDashboardApp:
    __init__ = app_init
    _setup_style = _setup_style
    _make_record = _make_record
    _format_record_date = _format_record_date
    _format_record_row = _format_record_row
    _sorted_records = _sorted_records
    _next_record_id = _next_record_id
    _build_layout = _build_layout
    _build_sidebar = _build_sidebar
    _build_main = _build_main
    _build_header = _build_header
    _build_summary_cards = _build_summary_cards
    _build_content = _build_content
    _build_records_panel = _build_records_panel
    _build_right_panels = _build_right_panels
    _create_box = _create_box
    show_view = show_view
    _build_upload_panel = _build_upload_panel
    _build_logs_panel = _build_logs_panel
    _build_deleted_panel = _build_deleted_panel
    _build_archive_panel = _build_archive_panel
    _clear_placeholder = _clear_placeholder
    _get_active_record_view = _get_active_record_view
    _get_active_upload_view = _get_active_upload_view
    select_upload_file = select_upload_file
    _get_selected_record = _get_selected_record
    _get_selected_deleted_record = _get_selected_deleted_record
    _load_records = _load_records
    _load_logs = _load_logs
    _load_archive_lists = _load_archive_lists
    _refresh_summary_cards = _refresh_summary_cards
    apply_filters = apply_filters
    upload_record = upload_record
    create_backup = create_backup
    view_selected = view_selected
    delete_selected = delete_selected
    upload_now = upload_now
    archive = archive
    restore = restore
    restore_deleted = restore_deleted
    permanently_delete = permanently_delete
    backup = backup
    export_logs = export_logs


def main():
    root = tk.Tk()
    app = AdminDashboardApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
