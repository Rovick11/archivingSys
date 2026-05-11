import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class ArchivePage:
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
        
        # Categories
        self.categories = [
            "All Categories",
            "Health",
            "Education",
            "Infrastructure",
            "Finance",
            "Agriculture",
            "Social Services",
            "Public Safety",
            "Environment",
            "Trade & Industry",
            "Others"
        ]
        
        # Archived files list
        self.archived_files = []
        
        self.setup_ui()
    
    def setup_ui(self):
        """Main UI for Archive Page"""
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
            text="📦",
            font=("Segoe UI", 22),
            bg=self.colors["primary_light"],
            fg=self.colors["primary"]
        ).place(relx=0.5, rely=0.5, anchor="center")
        
        # Title text
        text_frame = tk.Frame(title_frame, bg="white")
        text_frame.pack(side="left")
        
        tk.Label(
            text_frame,
            text="Archived Files",
            font=("Segoe UI", 20, "bold"),
            fg=self.colors["text_dark"],
            bg="white"
        ).pack(anchor="w")
        
        tk.Label(
            text_frame,
            text="View archived PDF files and documents",
            font=("Segoe UI", 10),
            fg=self.colors["text_medium"],
            bg="white"
        ).pack(anchor="w")
        
        # ===== SEARCH AND FILTER SECTION =====
        search_filter = tk.Frame(main, bg="white", height=80)
        search_filter.pack(fill="x", pady=(0, 20))
        search_filter.pack_propagate(False)
        search_filter.config(highlightbackground=self.colors["border"], highlightthickness=1)
        
        # LEFT - Search
        left_frame = tk.Frame(search_filter, bg="white")
        left_frame.pack(side="left", padx=30, pady=15)
        
        search_container = tk.Frame(
            left_frame,
            bg="white",
            highlightbackground=self.colors["border"],
            highlightthickness=1
        )
        search_container.pack()
        
        tk.Label(
            search_container,
            text="🔍",
            font=("Segoe UI", 12),
            bg="white",
            fg=self.colors["text_medium"]
        ).pack(side="left", padx=(12, 5))
        
        self.search_entry = tk.Entry(
            search_container,
            font=("Segoe UI", 11),
            bg="white",
            fg=self.colors["text_light"],
            bd=0,
            width=35
        )
        self.search_entry.pack(side="left", padx=(0, 12), ipady=8)
        self.search_entry.insert(0, "Search by resolution no. or title...")
        self.search_entry.bind("<FocusIn>", self.clear_search_placeholder)
        self.search_entry.bind("<FocusOut>", self.set_search_placeholder)
        self.search_entry.bind("<KeyRelease>", self.search_archive)
        
        # RIGHT - Filter by Category
        right_frame = tk.Frame(search_filter, bg="white")
        right_frame.pack(side="right", padx=30)
        
        tk.Label(
            right_frame,
            text="Category:",
            font=("Segoe UI", 11),
            fg=self.colors["text_medium"],
            bg="white"
        ).pack(side="left", padx=(0, 10))
        
        self.category_var = tk.StringVar(value="All Categories")
        category_combo = ttk.Combobox(
            right_frame,
            textvariable=self.category_var,
            values=self.categories,
            state="readonly",
            width=18,
            font=("Segoe UI", 11)
        )
        category_combo.pack(side="left")
        category_combo.bind("<<ComboboxSelected>>", self.filter_by_category)
        
        # ===== ARCHIVE TABLE =====
        self.create_archive_table(main)
    
    def create_archive_table(self, parent):
        """Archive files table - view only, no ID column"""
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
            text="📋 Archived PDF Files",
            font=("Segoe UI", 13, "bold"),
            fg=self.colors["text_dark"],
            bg="#f8f9fa"
        ).pack(side="left", padx=20, pady=12)
        
        # Table frame
        table_frame = tk.Frame(table_container, bg="white")
        table_frame.pack(fill="both", expand=True, padx=1, pady=1)
        
        # Scrollbars
        v_scroll = ttk.Scrollbar(table_frame)
        v_scroll.pack(side="right", fill="y")
        
        h_scroll = ttk.Scrollbar(table_frame, orient="horizontal")
        h_scroll.pack(side="bottom", fill="x")
        
        # Treeview - No ID column
        columns = ("Resolution No.", "Title", "Category", "Date Archived", "Archived By", "Original File")
        self.tree = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings",
            yscrollcommand=v_scroll.set,
            xscrollcommand=h_scroll.set,
            height=14,
            selectmode="browse"
        )
        
        v_scroll.config(command=self.tree.yview)
        h_scroll.config(command=self.tree.xview)
        
        # Column configurations
        configs = [
            ("Resolution No.", 140, "center"),
            ("Title", 280, "w"),
            ("Category", 130, "center"),
            ("Date Archived", 110, "center"),
            ("Archived By", 100, "center"),
            ("Original File", 220, "w")
        ]
        
        for col, width, anchor in configs:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=width, anchor=anchor)
        
        self.tree.pack(fill="both", expand=True)
        
        # Tags for styling
        self.tree.tag_configure("evenrow", background="#f9f9f9")
        self.tree.tag_configure("oddrow", background="white")
        self.tree.tag_configure("placeholder", foreground=self.colors["text_light"])
        
        # Show placeholder
        self.show_placeholder()
        
        # Bind double-click to view details
        self.tree.bind("<Double-Button-1>", self.view_details)
    
    def show_placeholder(self):
        """Show placeholder when no archived files"""
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        self.tree.insert("", "end", values=(
            "No archived files", "No files in archive", "-", "-", "-", "-"
        ), tags=("placeholder",))
    
    def load_archive(self, items=None):
        """Load archived files into table"""
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        items_to_show = items if items is not None else self.archived_files
        
        if not items_to_show:
            self.show_placeholder()
            return
        
        for i, file in enumerate(items_to_show):
            tags = ["evenrow" if i % 2 == 0 else "oddrow"]
            
            values = (
                file.get("resolution_no", "-"),
                file.get("title", "-"),
                file.get("category", "-"),
                file.get("date_archived", "-"),
                file.get("archived_by", "-"),
                file.get("original_file", "-")
            )
            
            self.tree.insert("", "end", values=values, tags=tuple(tags))
    
    def view_details(self, event):
        """View archived file details - view only"""
        selected = self.tree.selection()
        if not selected:
            return
        
        item = self.tree.item(selected[0])
        values = item["values"]
        
        if values[0] == "No archived files":
            return
        
        resolution_no = values[0]
        file_item = next((f for f in self.archived_files if f["resolution_no"] == resolution_no), None)
        
        if file_item:
            details = (
                f"📄 Archived File Details\n\n"
                f"Resolution No.: {file_item['resolution_no']}\n"
                f"Title: {file_item['title']}\n"
                f"Category: {file_item['category']}\n"
                f"Date Archived: {file_item['date_archived']}\n"
                f"Archived By: {file_item['archived_by']}\n"
                f"Original File: {file_item['original_file']}\n"
            )
            
            if file_item.get('description'):
                details += f"\nDescription:\n{file_item['description']}"
            
            messagebox.showinfo("Archived File Details", details)
    
    def add_archived_file(self, resolution_no, title, category, original_file, description=""):
        """Add file to archive - called from resolutions page when file is removed"""
        new_item = {
            "id": len(self.archived_files) + 1,
            "resolution_no": resolution_no,
            "title": title,
            "category": category,
            "date_archived": datetime.now().strftime("%Y-%m-%d"),
            "archived_by": "admin",
            "original_file": original_file,
            "description": description
        }
        
        self.archived_files.append(new_item)
        self.load_archive()
    
    def search_archive(self, event=None):
        """Search archived files"""
        keyword = self.search_entry.get().lower()
        
        if keyword in ["", "search by resolution no. or title..."]:
            self.load_archive()
            return
        
        if not self.archived_files:
            return
        
        filtered = [
            f for f in self.archived_files
            if keyword in f.get("resolution_no", "").lower() or
               keyword in f.get("title", "").lower()
        ]
        
        self.load_archive(filtered)
    
    def filter_by_category(self, event=None):
        """Filter by category"""
        category = self.category_var.get()
        
        if not self.archived_files:
            return
        
        if category == "All Categories":
            self.load_archive()
            return
        
        filtered = [f for f in self.archived_files if f.get("category") == category]
        self.load_archive(filtered)
    
    def clear_search_placeholder(self, event):
        if self.search_entry.get() == "Search by resolution no. or title...":
            self.search_entry.delete(0, tk.END)
            self.search_entry.config(fg=self.colors["text_dark"])
    
    def set_search_placeholder(self, event):
        if not self.search_entry.get():
            self.search_entry.insert(0, "Search by resolution no. or title...")
            self.search_entry.config(fg=self.colors["text_light"])
    
    def show(self):
        """Show the archive page"""
        for widget in self.parent.winfo_children():
            widget.destroy()
        self.setup_ui()


# Test the application
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Archive Management")
    root.geometry("1200x700")
    
    app = ArchivePage(root)
    
    root.mainloop()