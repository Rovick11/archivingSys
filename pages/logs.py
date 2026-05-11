import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class LogsPage:
    def __init__(self, parent, header_color="#0b3a6f", main_bg="#f5f7fa"):
        self.parent = parent
        self.header_color = header_color
        self.main_bg = main_bg
        
        # Color palette
        self.colors = {
            "primary": "#0b3a6f",
            "primary_light": "#e8f0fe",
            "accent": "#1976D2",
            "success": "#2E7D32",
            "warning": "#ED6C02",
            "danger": "#D32F2F",
            "info": "#0288D1",
            "text_dark": "#1e1e1e",
            "text_medium": "#666666",
            "text_light": "#999999",
            "border": "#e0e0e0",
            "card_bg": "#ffffff"
        }
        
        # Log types with colors
        self.log_types = {
            "Login": self.colors["success"],
            "Logout": self.colors["text_medium"],
            "Upload": self.colors["info"],
            "Delete": self.colors["danger"],
            "Update": self.colors["warning"],
            "Archive": self.colors["primary"],
            "Restore": self.colors["success"],
            "User Create": self.colors["accent"],
            "User Update": self.colors["warning"],
            "User Delete": self.colors["danger"],
            "Settings Change": self.colors["primary"],
            "Backup": self.colors["info"]
        }
        
        # Empty logs list
        self.logs = []
        
        self.setup_ui()
    
    def setup_ui(self):
        """Main UI for Logs Page"""
        # Main container
        main = tk.Frame(self.parent, bg=self.main_bg)
        main.pack(fill="both", expand=True)
        
        # ===== HEADER SECTION =====
        header = tk.Frame(main, bg="white", height=85)
        header.pack(fill="x", pady=(0, 20))
        header.pack_propagate(False)
        header.config(highlightbackground=self.colors["border"], highlightthickness=1)
        
        # Title frame
        title_frame = tk.Frame(header, bg="white")
        title_frame.pack(side="left", padx=30, pady=20)
        
        # Icon frame
        icon_frame = tk.Frame(
            title_frame,
            bg=self.colors["primary_light"],
            width=45,
            height=45
        )
        icon_frame.pack(side="left", padx=(0, 15))
        icon_frame.pack_propagate(False)
        
        tk.Label(
            icon_frame,
            text="📋",
            font=("Segoe UI", 22),
            bg=self.colors["primary_light"],
            fg=self.colors["primary"]
        ).place(relx=0.5, rely=0.5, anchor="center")
        
        # Title text
        text_frame = tk.Frame(title_frame, bg="white")
        text_frame.pack(side="left")
        
        tk.Label(
            text_frame,
            text="System Logs",
            font=("Segoe UI", 20, "bold"),
            fg=self.colors["text_dark"],
            bg="white"
        ).pack(anchor="w")
        
        tk.Label(
            text_frame,
            text="View and monitor system activities",
            font=("Segoe UI", 10),
            fg=self.colors["text_medium"],
            bg="white"
        ).pack(anchor="w")
        
        # Refresh Button
        refresh_btn = tk.Button(
            header,
            text="🔄 Refresh",
            font=("Segoe UI", 11, "bold"),
            bg=self.colors["accent"],
            fg="white",
            padx=20,
            pady=10,
            cursor="hand2",
            relief="flat",
            command=self.refresh_logs
        )
        refresh_btn.pack(side="right", padx=30, pady=25)
        
        # ===== FILTERS SECTION =====
        filters_frame = tk.Frame(main, bg="white")
        filters_frame.pack(fill="x", pady=(0, 20))
        filters_frame.config(highlightbackground=self.colors["border"], highlightthickness=1)
        
        # First row - Search
        row1 = tk.Frame(filters_frame, bg="white")
        row1.pack(fill="x", padx=30, pady=(15, 10))
        
        tk.Label(
            row1,
            text="Search",
            font=("Segoe UI", 11),
            fg=self.colors["text_medium"],
            bg="white",
            width=8,
            anchor="w"
        ).pack(side="left")
        
        self.search_entry = tk.Entry(
            row1,
            font=("Segoe UI", 11),
            bg="#f8f9fa",
            bd=1,
            relief="solid",
            highlightbackground=self.colors["border"],
            width=50
        )
        self.search_entry.pack(side="left", padx=(10, 0), ipady=8)
        self.search_entry.insert(0, "Search by description, user, or type...")
        self.search_entry.bind("<FocusIn>", self.clear_search_placeholder)
        self.search_entry.bind("<FocusOut>", self.set_search_placeholder)
        self.search_entry.bind("<KeyRelease>", self.search_logs)
        
        # Second row - Filters
        row2 = tk.Frame(filters_frame, bg="white")
        row2.pack(fill="x", padx=30, pady=(5, 15))
        
        # Log Type
        tk.Label(
            row2,
            text="Log Type",
            font=("Segoe UI", 11),
            fg=self.colors["text_medium"],
            bg="white",
            width=8,
            anchor="w"
        ).pack(side="left")
        
        self.type_var = tk.StringVar(value="All Types")
        type_combo = ttk.Combobox(
            row2,
            textvariable=self.type_var,
            values=["All Types"] + list(self.log_types.keys()),
            state="readonly",
            width=18,
            font=("Segoe UI", 11)
        )
        type_combo.pack(side="left", padx=(10, 20))
        type_combo.bind("<<ComboboxSelected>>", self.filter_logs)
        
        # Date Range
        tk.Label(
            row2,
            text="Date Range",
            font=("Segoe UI", 11),
            fg=self.colors["text_medium"],
            bg="white",
            width=10,
            anchor="w"
        ).pack(side="left")
        
        self.date_var = tk.StringVar(value="All Time")
        date_combo = ttk.Combobox(
            row2,
            textvariable=self.date_var,
            values=["All Time", "Today", "Last 7 Days", "Last 30 Days", "This Month"],
            state="readonly",
            width=15,
            font=("Segoe UI", 11)
        )
        date_combo.pack(side="left", padx=(10, 20))
        date_combo.bind("<<ComboboxSelected>>", self.filter_by_date)
        
        # User
        tk.Label(
            row2,
            text="User",
            font=("Segoe UI", 11),
            fg=self.colors["text_medium"],
            bg="white",
            width=6,
            anchor="w"
        ).pack(side="left")
        
        self.user_var = tk.StringVar(value="All Users")
        user_combo = ttk.Combobox(
            row2,
            textvariable=self.user_var,
            values=["All Users"],
            state="readonly",
            width=15,
            font=("Segoe UI", 11)
        )
        user_combo.pack(side="left", padx=(10, 20))
        user_combo.bind("<<ComboboxSelected>>", self.filter_by_user)
        
        # Status
        tk.Label(
            row2,
            text="Status",
            font=("Segoe UI", 11),
            fg=self.colors["text_medium"],
            bg="white",
            width=7,
            anchor="w"
        ).pack(side="left")
        
        self.status_var = tk.StringVar(value="All")
        status_combo = ttk.Combobox(
            row2,
            textvariable=self.status_var,
            values=["All", "Success", "Failed"],
            state="readonly",
            width=12,
            font=("Segoe UI", 11)
        )
        status_combo.pack(side="left", padx=(10, 20))
        status_combo.bind("<<ComboboxSelected>>", self.filter_by_status)
        
        # Clear Filters Button
        clear_btn = tk.Button(
            row2,
            text="Clear Filters",
            font=("Segoe UI", 10),
            bg="#f0f0f0",
            fg=self.colors["text_dark"],
            padx=15,
            pady=4,
            cursor="hand2",
            relief="flat",
            command=self.clear_filters
        )
        clear_btn.pack(side="right")
        
        # ===== LOGS TABLE =====
        self.create_logs_table(main)
        
        # ===== STATUS BAR =====
        self.create_status_bar(main)
    
    def create_logs_table(self, parent):
        """Create logs table without ID column"""
        # Table container
        table_container = tk.Frame(parent, bg="white")
        table_container.pack(fill="both", expand=True, padx=30)
        table_container.config(highlightbackground=self.colors["border"], highlightthickness=1)
        
        # Table header
        header = tk.Frame(table_container, bg="#f8f9fa", height=50)
        header.pack(fill="x")
        header.pack_propagate(False)
        
        tk.Label(
            header,
            text="📋 Activity Logs",
            font=("Segoe UI", 13, "bold"),
            fg=self.colors["text_dark"],
            bg="#f8f9fa"
        ).pack(side="left", padx=20, pady=12)
        
        # Export Button
        export_btn = tk.Button(
            header,
            text="📥 Export",
            font=("Segoe UI", 10),
            bg=self.colors["success"],
            fg="white",
            padx=15,
            pady=4,
            cursor="hand2",
            relief="flat",
            command=self.export_logs
        )
        export_btn.pack(side="right", padx=20)
        
        # Table frame
        table_frame = tk.Frame(table_container, bg="white")
        table_frame.pack(fill="both", expand=True, padx=1, pady=1)
        
        # Scrollbars
        v_scroll = ttk.Scrollbar(table_frame)
        v_scroll.pack(side="right", fill="y")
        
        h_scroll = ttk.Scrollbar(table_frame, orient="horizontal")
        h_scroll.pack(side="bottom", fill="x")
        
        # Treeview - No ID column
        columns = ("Timestamp", "Type", "User", "Description", "IP Address", "Status")
        self.tree = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings",
            yscrollcommand=v_scroll.set,
            xscrollcommand=h_scroll.set,
            height=15,
            selectmode="browse"
        )
        
        v_scroll.config(command=self.tree.yview)
        h_scroll.config(command=self.tree.xview)
        
        # Column configurations
        configs = [
            ("Timestamp", 150, "center"),
            ("Type", 100, "center"),
            ("User", 120, "center"),
            ("Description", 400, "w"),
            ("IP Address", 120, "center"),
            ("Status", 80, "center")
        ]
        
        for col, width, anchor in configs:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=width, anchor=anchor)
        
        self.tree.pack(fill="both", expand=True)
        
        # Tags for styling
        self.tree.tag_configure("evenrow", background="#f9f9f9")
        self.tree.tag_configure("oddrow", background="white")
        self.tree.tag_configure("Success", foreground=self.colors["success"])
        self.tree.tag_configure("Failed", foreground=self.colors["danger"])
        self.tree.tag_configure("placeholder", foreground=self.colors["text_light"])
        
        # Show placeholder
        self.show_placeholder()
        
        # Bind double-click to view details
        self.tree.bind("<Double-Button-1>", self.view_log_details)
    
    def show_placeholder(self):
        """Show placeholder when no logs"""
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        self.tree.insert("", "end", values=(
            "No logs", "-", "-", "No activity logs found", "-", "-"
        ), tags=("placeholder",))
    
    def load_logs(self, logs=None):
        """Load logs into table"""
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        logs_to_show = logs if logs is not None else self.logs
        
        if not logs_to_show:
            self.show_placeholder()
            return
        
        for i, log in enumerate(logs_to_show):
            tag = "evenrow" if i % 2 == 0 else "oddrow"
            status_tag = log.get("status", "")
            
            values = (
                log.get("timestamp", "-"),
                log.get("type", "-"),
                log.get("user", "-"),
                log.get("description", "-"),
                log.get("ip_address", "-"),
                log.get("status", "-")
            )
            
            tags = [tag]
            if status_tag == "Success":
                tags.append("Success")
            elif status_tag == "Failed":
                tags.append("Failed")
            
            self.tree.insert("", "end", values=values, tags=tuple(tags))
    
    def create_status_bar(self, parent):
        """Create status bar"""
        status_bar = tk.Frame(parent, bg="white", height=40)
        status_bar.pack(fill="x", side="bottom", pady=(15, 0))
        status_bar.pack_propagate(False)
        status_bar.config(highlightbackground=self.colors["border"], highlightthickness=1)
        
        left = tk.Frame(status_bar, bg="white")
        left.pack(side="left", padx=25, pady=8)
        
        total = len(self.logs)
        last_update = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        tk.Label(
            left,
            text=f"📊 Total Logs: {total}",
            font=("Segoe UI", 10),
            fg=self.colors["text_medium"],
            bg="white"
        ).pack(side="left", padx=(0, 20))
        
        tk.Label(
            left,
            text=f"🕒 Last Updated: {last_update}",
            font=("Segoe UI", 10),
            fg=self.colors["text_medium"],
            bg="white"
        ).pack(side="left")
        
        right = tk.Frame(status_bar, bg="white")
        right.pack(side="right", padx=25, pady=8)
        
        tk.Label(
            right,
            text="✓ Logs are automatically recorded",
            font=("Segoe UI", 9),
            fg=self.colors["text_light"],
            bg="white"
        ).pack(side="left")
    
    def add_log(self, log_type, description, user, status="Success", ip_address="127.0.0.1"):
        """Add a new log entry"""
        new_log = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "type": log_type,
            "user": user,
            "description": description,
            "ip_address": ip_address,
            "status": status
        }
        
        self.logs.append(new_log)
        self.load_logs()
        self.create_status_bar(self.parent)
    
    def search_logs(self, event=None):
        """Search logs by keyword"""
        keyword = self.search_entry.get().lower()
        
        if keyword in ["", "search by description, user, or type..."]:
            self.load_logs()
            return
        
        if not self.logs:
            self.show_placeholder()
            return
        
        filtered = [
            l for l in self.logs
            if keyword in l.get("description", "").lower() or
               keyword in l.get("user", "").lower() or
               keyword in l.get("type", "").lower()
        ]
        
        if filtered:
            self.load_logs(filtered)
        else:
            for item in self.tree.get_children():
                self.tree.delete(item)
            self.tree.insert("", "end", values=(
                "No results", "-", "-", f"No matches found", "-", "-"
            ), tags=("placeholder",))
    
    def filter_logs(self, event=None):
        """Filter by log type"""
        self.apply_all_filters()
    
    def filter_by_date(self, event=None):
        """Filter by date range"""
        self.apply_all_filters()
    
    def filter_by_user(self, event=None):
        """Filter by user"""
        self.apply_all_filters()
    
    def filter_by_status(self, event=None):
        """Filter by status"""
        self.apply_all_filters()
    
    def apply_all_filters(self):
        """Apply all filters"""
        log_type = self.type_var.get()
        date_range = self.date_var.get()
        user = self.user_var.get()
        status = self.status_var.get()
        
        if not self.logs:
            self.show_placeholder()
            return
        
        filtered = self.logs.copy()
        
        # Filter by log type
        if log_type != "All Types":
            filtered = [l for l in filtered if l.get("type") == log_type]
        
        # Filter by user
        if user != "All Users":
            filtered = [l for l in filtered if l.get("user") == user]
        
        # Filter by status
        if status != "All":
            filtered = [l for l in filtered if l.get("status") == status]
        
        # Filter by date
        if date_range != "All Time":
            now = datetime.now()
            today = now.date()
            
            def filter_by_date_range(log):
                try:
                    log_date = datetime.strptime(log.get("timestamp", ""), "%Y-%m-%d %H:%M:%S").date()
                    
                    if date_range == "Today":
                        return log_date == today
                    elif date_range == "Last 7 Days":
                        return (today - log_date).days <= 7
                    elif date_range == "Last 30 Days":
                        return (today - log_date).days <= 30
                    elif date_range == "This Month":
                        return log_date.year == today.year and log_date.month == today.month
                except:
                    return True
                return True
            
            filtered = [l for l in filtered if filter_by_date_range(l)]
        
        if filtered:
            self.load_logs(filtered)
        else:
            for item in self.tree.get_children():
                self.tree.delete(item)
            self.tree.insert("", "end", values=(
                "No results", "-", "-", "No logs match the selected filters", "-", "-"
            ), tags=("placeholder",))
    
    def clear_filters(self):
        """Clear all filters"""
        self.type_var.set("All Types")
        self.date_var.set("All Time")
        self.user_var.set("All Users")
        self.status_var.set("All")
        self.search_entry.delete(0, tk.END)
        self.search_entry.insert(0, "Search by description, user, or type...")
        self.search_entry.config(fg=self.colors["text_light"])
        self.load_logs()
    
    def refresh_logs(self):
        """Refresh logs"""
        self.load_logs()
        self.create_status_bar(self.parent)
        messagebox.showinfo("Refresh", "Logs refreshed successfully!")
    
    def export_logs(self):
        """Export logs to file"""
        if not self.logs:
            messagebox.showwarning("Export", "No logs to export!")
            return
        
        messagebox.showinfo("Export", "Export functionality coming soon!")
    
    def view_log_details(self, event):
        """View log details"""
        selected = self.tree.selection()
        if not selected:
            return
        
        item = self.tree.item(selected[0])
        values = item["values"]
        
        if values[0] in ["No logs", "No results"]:
            return
        
        details = (
            f"📋 Log Details\n\n"
            f"Timestamp: {values[0]}\n"
            f"Type: {values[1]}\n"
            f"User: {values[2]}\n"
            f"Description: {values[3]}\n"
            f"IP Address: {values[4]}\n"
            f"Status: {values[5]}"
        )
        
        messagebox.showinfo("Log Details", details)
    
    def clear_search_placeholder(self, event):
        if self.search_entry.get() == "Search by description, user, or type...":
            self.search_entry.delete(0, tk.END)
            self.search_entry.config(fg=self.colors["text_dark"])
    
    def set_search_placeholder(self, event):
        if not self.search_entry.get():
            self.search_entry.insert(0, "Search by description, user, or type...")
            self.search_entry.config(fg=self.colors["text_light"])
    
    def show(self):
        """Show the logs page"""
        for widget in self.parent.winfo_children():
            widget.destroy()
        self.setup_ui()


# Test the application
if __name__ == "__main__":
    root = tk.Tk()
    root.title("System Logs")
    root.geometry("1300x750")
    
    app = LogsPage(root)
    
    root.mainloop()