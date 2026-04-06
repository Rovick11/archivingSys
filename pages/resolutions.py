import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from datetime import datetime
import os

class ResolutionsPage:
    def __init__(self, parent, header_color="#0b3a6f", main_bg="#f5f7fa"):
        self.parent = parent
        self.header_color = header_color
        self.main_bg = main_bg
        
        # Simple color palette - COMPLETE with all necessary colors
        self.colors = {
            "primary": "#0b3a6f",      # Dark blue
            "primary_light": "#e8f0fe", # Light blue
            "success": "#2E7D32",        # Green for Approved
            "warning": "#ED6C02",         # Orange for Pending
            "text_dark": "#333333",       # Dark text for labels
            "text_medium": "#666666",     # Medium text
            "text_light": "#999999",      # Light text for placeholders
            "border": "#e0e0e0"           # Border color
        }
        
        # Categories for resolutions
        self.categories = [
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
        
        # Empty resolutions list
        self.resolutions = []
        
        # Setup UI
        self.setup_ui()
    
    def setup_ui(self):
        """Main UI for Resolutions Page"""
        # Main container
        main = tk.Frame(self.parent, bg=self.main_bg)
        main.pack(fill="both", expand=True)
        
        # ===== HEADER SECTION =====
        header = tk.Frame(main, bg="white", height=85)
        header.pack(fill="x", pady=(0, 20))
        header.pack_propagate(False)
        header.config(highlightbackground=self.colors["border"], highlightthickness=1)
        
        # Title
        title_frame = tk.Frame(header, bg="white")
        title_frame.pack(side="left", padx=30, pady=20)
        
        tk.Label(
            title_frame,
            text="Resolutions Management",
            font=("Segoe UI", 20, "bold"),
            fg=self.colors["primary"],
            bg="white"
        ).pack(anchor="w")
        
        tk.Label(
            title_frame,
            text="Manage and track official resolutions",
            font=("Segoe UI", 10),
            fg=self.colors["text_medium"],
            bg="white"
        ).pack(anchor="w")
        
        # Action Buttons
        btn_frame = tk.Frame(header, bg="white")
        btn_frame.pack(side="right", padx=30)
        
        # Upload PDF Button
        upload_btn = tk.Button(
            btn_frame,
            text="Upload PDF",
            font=("Segoe UI", 11, "bold"),
            bg=self.colors["primary"],
            fg="white",
            padx=20,
            pady=10,
            cursor="hand2",
            relief="flat",
            command=self.upload_pdf
        )
        upload_btn.pack(side="left", padx=5)
        
        # Print Button
        print_btn = tk.Button(
            btn_frame,
            text="Print",
            font=("Segoe UI", 11, "bold"),
            bg="#555555",
            fg="white",
            padx=20,
            pady=10,
            cursor="hand2",
            relief="flat",
            command=self.print_resolution
        )
        print_btn.pack(side="left", padx=5)
        
        # ===== SEARCH AND FILTER SECTION =====
        search_filter = tk.Frame(main, bg="white", height=80)
        search_filter.pack(fill="x", pady=(0, 20))
        search_filter.pack_propagate(False)
        search_filter.config(highlightbackground=self.colors["border"], highlightthickness=1)
        
        # LEFT - Search
        left_frame = tk.Frame(search_filter, bg="white")
        left_frame.pack(side="left", padx=30, pady=15)
        
        # Search container
        search_container = tk.Frame(
            left_frame,
            bg="white",
            highlightbackground=self.colors["border"],
            highlightthickness=1
        )
        search_container.pack()
        
        self.search_entry = tk.Entry(
            search_container,
            font=("Segoe UI", 11),
            bg="white",
            fg=self.colors["text_light"],
            bd=0,
            width=35,
            insertwidth=1
        )
        self.search_entry.pack(side="left", padx=12, ipady=8)
        self.search_entry.insert(0, "Search by resolution no. or title...")
        self.search_entry.bind("<FocusIn>", self.clear_search_placeholder)
        self.search_entry.bind("<FocusOut>", self.set_search_placeholder)
        self.search_entry.bind("<KeyRelease>", self.search_resolutions)
        
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
            values=["All Categories"] + self.categories,
            state="readonly",
            width=18,
            font=("Segoe UI", 11)
        )
        category_combo.pack(side="left", padx=(0, 15))
        category_combo.bind("<<ComboboxSelected>>", self.filter_by_category)
        
        # Filter by Status
        tk.Label(
            right_frame,
            text="Status:",
            font=("Segoe UI", 11),
            fg=self.colors["text_medium"],
            bg="white"
        ).pack(side="left", padx=(0, 10))
        
        self.status_var = tk.StringVar(value="All")
        status_combo = ttk.Combobox(
            right_frame,
            textvariable=self.status_var,
            values=["All", "Approved", "Pending", "Archived"],
            state="readonly",
            width=12,
            font=("Segoe UI", 11)
        )
        status_combo.pack(side="left")
        status_combo.bind("<<ComboboxSelected>>", self.filter_by_status)
        
        # ===== STATS CARDS =====
        self.create_stats_cards(main)
        
        # ===== RESOLUTIONS TABLE =====
        self.create_resolutions_table(main)
        
        # ===== STATUS BAR =====
        self.create_status_bar(main)
    
    def create_stats_cards(self, parent):
        """Statistics cards for resolutions"""
        stats_frame = tk.Frame(parent, bg=self.main_bg)
        stats_frame.pack(fill="x", padx=30, pady=(0, 20))
        
        # Clear existing widgets
        for widget in stats_frame.winfo_children():
            widget.destroy()
        
        # Configure grid
        for i in range(4):
            stats_frame.columnconfigure(i, weight=1)
        
        # Calculate stats from actual data
        total = len(self.resolutions)
        approved = sum(1 for r in self.resolutions if r.get("status") == "Approved")
        pending = sum(1 for r in self.resolutions if r.get("status") == "Pending")
        categories_count = len(set(r.get("category") for r in self.resolutions)) if self.resolutions else 0
        
        stats = [
            {"label": "Total Resolutions", "value": str(total)},
            {"label": "Approved", "value": str(approved)},
            {"label": "Pending", "value": str(pending)},
            {"label": "Categories", "value": str(categories_count)}
        ]
        
        for i, stat in enumerate(stats):
            card = tk.Frame(
                stats_frame,
                bg="white",
                highlightbackground=self.colors["border"],
                highlightthickness=1,
                height=75
            )
            card.grid(row=0, column=i, padx=8, sticky="nsew")
            card.pack_propagate(False)
            
            # Content
            content = tk.Frame(card, bg="white")
            content.place(relx=0.5, rely=0.5, anchor="center")
            
            # Label
            tk.Label(
                content,
                text=stat["label"],
                font=("Segoe UI", 10),
                fg=self.colors["text_medium"],
                bg="white"
            ).pack()
            
            # Value
            value_color = self.colors["primary"] if stat["value"] != "0" else self.colors["text_light"]
            tk.Label(
                content,
                text=stat["value"],
                font=("Segoe UI", 18, "bold"),
                fg=value_color,
                bg="white"
            ).pack()
    
    def create_resolutions_table(self, parent):
        """Resolutions table"""
        # Table container
        table_container = tk.Frame(parent, bg="white")
        table_container.pack(fill="both", expand=True, padx=30)
        table_container.config(highlightbackground=self.colors["border"], highlightthickness=1)
        
        # Table header
        header = tk.Frame(table_container, bg="#f8f9fa", height=45)
        header.pack(fill="x")
        header.pack_propagate(False)
        
        tk.Label(
            header,
            text="Resolutions List",
            font=("Segoe UI", 13, "bold"),
            fg=self.colors["primary"],
            bg="#f8f9fa"
        ).pack(side="left", padx=20, pady=10)
        
        # Table frame
        table_frame = tk.Frame(table_container, bg="white")
        table_frame.pack(fill="both", expand=True, padx=1, pady=1)
        
        # Scrollbars
        v_scroll = ttk.Scrollbar(table_frame)
        v_scroll.pack(side="right", fill="y")
        
        h_scroll = ttk.Scrollbar(table_frame, orient="horizontal")
        h_scroll.pack(side="bottom", fill="x")
        
        # Treeview
        columns = ("Resolution No.", "Title", "Category", "Date Filed", "Status", "File")
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
            ("Resolution No.", 130, "center"),
            ("Title", 300, "w"),
            ("Category", 130, "center"),
            ("Date Filed", 100, "center"),
            ("Status", 100, "center"),
            ("File", 200, "w")
        ]
        
        for col, width, anchor in configs:
            self.tree.heading(col, text=col, command=lambda c=col: self.sort_column(c))
            self.tree.column(col, width=width, anchor=anchor)
        
        self.tree.pack(fill="both", expand=True)
        
        # Tags for styling
        self.tree.tag_configure("evenrow", background="#f9f9f9")
        self.tree.tag_configure("oddrow", background="white")
        self.tree.tag_configure("Approved", foreground=self.colors["success"])
        self.tree.tag_configure("Pending", foreground=self.colors["warning"])
        self.tree.tag_configure("Archived", foreground="#666666")
        self.tree.tag_configure("placeholder", foreground=self.colors["text_light"])
        
        # Load initial data
        self.load_resolutions()
        
        # Bind double-click to view
        self.tree.bind("<Double-Button-1>", self.view_resolution)
    
    def load_resolutions(self, resolutions=None):
        """Load resolutions into table"""
        # Clear existing items
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        resolutions_to_show = resolutions if resolutions is not None else self.resolutions
        
        if not resolutions_to_show:
            # Show empty message
            self.tree.insert("", "end", values=(
                "No resolutions", "", "", "", "", ""
            ), tags=("placeholder",))
            return
        
        for i, res in enumerate(resolutions_to_show):
            # Alternating row colors
            row_tag = "evenrow" if i % 2 == 0 else "oddrow"
            
            # Status tag for coloring
            status = res.get("status", "")
            status_tag = status if status in ["Approved", "Pending", "Archived"] else ""
            
            # Combine tags
            tags = [row_tag]
            if status_tag:
                tags.append(status_tag)
            
            values = (
                res.get("resolution_no", "—"),
                res.get("title", "—"),
                res.get("category", "—"),
                res.get("date_filed", "—"),
                res.get("status", "—"),
                res.get("file", "—")
            )
            
            self.tree.insert("", "end", values=values, tags=tuple(tags))
    
    def upload_pdf(self):
        """Upload PDF file - ONLY PDF ALLOWED"""
        file_path = filedialog.askopenfilename(
            title="Select PDF File",
            filetypes=[("PDF files", "*.pdf")]
        )
        
        if file_path:
            # STRICT PDF validation
            if not file_path.lower().endswith('.pdf'):
                messagebox.showerror("Invalid File", "Only PDF files are allowed!")
                return
            
            # Get filename
            filename = os.path.basename(file_path)
            
            # Open upload form
            self.open_upload_form(filename)
    
    def open_upload_form(self, filename):
        """Open form to upload resolution details with Save and Cancel buttons"""
        dialog = tk.Toplevel(self.parent)
        dialog.title("Upload Resolution")
        dialog.geometry("500x600")
        dialog.resizable(False, False)
        dialog.grab_set()
        dialog.configure(bg="white")
        
        # Center dialog
        dialog.update_idletasks()
        x = (dialog.winfo_screenwidth() // 2) - (500 // 2)
        y = (dialog.winfo_screenheight() // 2) - (600 // 2)
        dialog.geometry(f"+{x}+{y}")
        
        # Main container
        main = tk.Frame(dialog, bg="white", padx=30, pady=20)
        main.pack(fill="both", expand=True)
        
        # Title
        tk.Label(
            main,
            text="Upload Resolution",
            font=("Segoe UI", 18, "bold"),
            fg=self.colors["primary"],
            bg="white"
        ).pack(pady=(0, 5))
        
        tk.Label(
            main,
            text=f"File: {filename}",
            font=("Segoe UI", 10),
            fg=self.colors["text_medium"],
            bg="white"
        ).pack(pady=(0, 20))
        
        # Form fields
        fields = [
            ("Resolution No.:", "entry", True),
            ("Title:", "entry", True),
            ("Category:", "combobox", self.categories),
            ("Date Filed:", "entry", True, "YYYY-MM-DD"),
            ("Status:", "combobox", ["Approved", "Pending", "Archived"])
        ]
        
        entries = {}
        
        for field in fields:
            # Field row
            row = tk.Frame(main, bg="white")
            row.pack(fill="x", pady=8)
            
            # Label
            label_text = field[0]
            if field[2] is True:  # Required field
                label_text += " *"
            
            tk.Label(
                row,
                text=label_text,
                font=("Segoe UI", 11),
                fg=self.colors["text_dark"],  # text_dark is now defined
                bg="white",
                width=12,
                anchor="w"
            ).pack(side="left")
            
            # Input field
            if field[1] == "entry":
                entry = tk.Entry(
                    row,
                    font=("Segoe UI", 11),
                    bg="#f8f9fa",
                    bd=1,
                    relief="solid",
                    highlightbackground=self.colors["border"]
                )
                entry.pack(side="left", fill="x", expand=True, padx=(5, 0), ipady=6)
                
                # Add placeholder for Date Filed
                if len(field) > 3 and field[3] == "YYYY-MM-DD":
                    entry.insert(0, "YYYY-MM-DD")
                    entry.bind("<FocusIn>", lambda e, ent=entry: self.clear_date_placeholder(e, ent))
                    entry.bind("<FocusOut>", lambda e, ent=entry: self.set_date_placeholder(e, ent))
                
                entries[field[0]] = entry
                
            else:  # combobox
                combo = ttk.Combobox(
                    row,
                    values=field[2],
                    state="readonly",
                    font=("Segoe UI", 11)
                )
                combo.pack(side="left", fill="x", expand=True, padx=(5, 0))
                entries[field[0]] = combo
        
        # Required note
        tk.Label(
            main,
            text="* Required fields",
            font=("Segoe UI", 9),
            fg=self.colors["text_light"],
            bg="white"
        ).pack(anchor="w", pady=(15, 20))
        
        # ===== BUTTONS (SAVE & CANCEL) =====
        button_frame = tk.Frame(main, bg="white")
        button_frame.pack(pady=10)
        
        # Save Button
        save_btn = tk.Button(
            button_frame,
            text="Save",
            font=("Segoe UI", 11, "bold"),
            bg=self.colors["primary"],
            fg="white",
            padx=30,
            pady=8,
            cursor="hand2",
            relief="flat",
            width=10,
            command=lambda: self.save_resolution(entries, filename, dialog)
        )
        save_btn.pack(side="left", padx=10)
        
        # Cancel Button
        cancel_btn = tk.Button(
            button_frame,
            text="Cancel",
            font=("Segoe UI", 11),
            bg="#f0f0f0",
            fg="#333333",
            padx=30,
            pady=8,
            cursor="hand2",
            relief="flat",
            width=10,
            command=dialog.destroy
        )
        cancel_btn.pack(side="left", padx=10)
    
    def save_resolution(self, entries, filename, dialog):
        """Save resolution to list and refresh display"""
        # Get values
        resolution_no = entries["Resolution No.:"].get().strip()
        title = entries["Title:"].get().strip()
        category = entries["Category:"].get()
        date_filed = entries["Date Filed:"].get().strip()
        status = entries["Status:"].get()
        
        # Validate required fields
        if not resolution_no:
            messagebox.showwarning("Required", "Resolution No. is required!")
            return
        if not title:
            messagebox.showwarning("Required", "Title is required!")
            return
        if not category:
            messagebox.showwarning("Required", "Category is required!")
            return
        if not date_filed or date_filed == "YYYY-MM-DD":
            messagebox.showwarning("Required", "Date Filed is required!")
            return
        if not status:
            messagebox.showwarning("Required", "Status is required!")
            return
        
        # Create new resolution
        new_res = {
            "resolution_no": resolution_no,
            "title": title,
            "category": category,
            "date_filed": date_filed,
            "status": status,
            "file": filename
        }
        
        # Add to list
        self.resolutions.append(new_res)
        
        # Refresh the display
        self.load_resolutions()              # Refresh table
        self.create_stats_cards(self.parent) # Refresh stats
        self.create_status_bar(self.parent)  # Refresh status bar
        
        # Close dialog and show success
        dialog.destroy()
        messagebox.showinfo("Success", f"Resolution '{resolution_no}' uploaded successfully!")
    
    def print_resolution(self):
        """Print selected resolution"""
        selected = self.tree.selection()
        if not selected:
            messagebox.showinfo("Print", "Please select a resolution to print")
            return
        
        item = self.tree.item(selected[0])
        values = item["values"]
        
        if values[0] == "No resolutions":
            return
        
        # Print confirmation
        messagebox.showinfo(
            "Print",
            f"Printing resolution:\n\n{values[0]} - {values[1]}"
        )
    
    def view_resolution(self, event):
        """View resolution details"""
        selected = self.tree.selection()
        if not selected:
            return
        
        item = self.tree.item(selected[0])
        values = item["values"]
        
        if values[0] == "No resolutions":
            return
        
        # Find resolution
        resolution_no = values[0]
        res = next((r for r in self.resolutions if r["resolution_no"] == resolution_no), None)
        
        if res:
            details = (
                f"Resolution Details\n\n"
                f"Number: {res['resolution_no']}\n"
                f"Title: {res['title']}\n"
                f"Category: {res['category']}\n"
                f"Date Filed: {res['date_filed']}\n"
                f"Status: {res['status']}\n"
                f"File: {res['file']}"
            )
            messagebox.showinfo("Resolution Details", details)
    
    def search_resolutions(self, event=None):
        """Search resolutions"""
        keyword = self.search_entry.get().lower()
        
        if keyword in ["", "search by resolution no. or title..."]:
            self.load_resolutions()
            return
        
        if not self.resolutions:
            return
        
        filtered = [
            r for r in self.resolutions
            if keyword in r.get("resolution_no", "").lower() or
               keyword in r.get("title", "").lower()
        ]
        
        self.load_resolutions(filtered)
    
    def filter_by_category(self, event=None):
        """Filter by category"""
        category = self.category_var.get()
        status = self.status_var.get()
        
        if not self.resolutions:
            return
        
        filtered = self.resolutions.copy()
        
        if category != "All Categories":
            filtered = [r for r in filtered if r.get("category") == category]
        
        if status != "All":
            filtered = [r for r in filtered if r.get("status") == status]
        
        self.load_resolutions(filtered)
    
    def filter_by_status(self, event=None):
        """Filter by status"""
        self.filter_by_category()
    
    def sort_column(self, col):
        """Sort treeview by column"""
        if not self.tree.get_children():
            return
        
        data = []
        for child in self.tree.get_children(''):
            val = self.tree.set(child, col)
            data.append((val, child))
        
        data.sort()
        
        for index, (val, child) in enumerate(data):
            self.tree.move(child, '', index)
    
    def create_status_bar(self, parent):
        """Status bar at bottom"""
        # Remove old status bar if exists
        for widget in parent.winfo_children():
            if isinstance(widget, tk.Frame) and widget.winfo_y() > 400:
                if widget.winfo_height() == 40:
                    widget.destroy()
        
        status_bar = tk.Frame(parent, bg="white", height=40)
        status_bar.pack(fill="x", side="bottom", pady=(15, 0))
        status_bar.pack_propagate(False)
        status_bar.config(highlightbackground=self.colors["border"], highlightthickness=1)
        
        # Left stats
        left = tk.Frame(status_bar, bg="white")
        left.pack(side="left", padx=25)
        
        total = len(self.resolutions)
        
        tk.Label(
            left,
            text=f"Total Resolutions: {total}",
            font=("Segoe UI", 10),
            fg=self.colors["text_medium"],
            bg="white"
        ).pack(side="left")
        
        # Right - Last update
        right = tk.Frame(status_bar, bg="white")
        right.pack(side="right", padx=25)
        
        tk.Label(
            right,
            text=datetime.now().strftime("%I:%M %p"),
            font=("Segoe UI", 10),
            fg=self.colors["text_medium"],
            bg="white"
        ).pack(side="left")
    
    # ---------------- HELPER FUNCTIONS ---------------- #
    
    def clear_search_placeholder(self, event):
        if self.search_entry.get() == "Search by resolution no. or title...":
            self.search_entry.delete(0, tk.END)
            self.search_entry.config(fg=self.colors["text_dark"])
    
    def set_search_placeholder(self, event):
        if not self.search_entry.get():
            self.search_entry.insert(0, "Search by resolution no. or title...")
            self.search_entry.config(fg=self.colors["text_light"])
    
    def clear_date_placeholder(self, event, entry):
        if entry.get() == "YYYY-MM-DD":
            entry.delete(0, tk.END)
            entry.config(fg=self.colors["text_dark"])
    
    def set_date_placeholder(self, event, entry):
        if not entry.get():
            entry.insert(0, "YYYY-MM-DD")
            entry.config(fg=self.colors["text_light"])
    
    def show(self):
        """Show the resolutions page"""
        for widget in self.parent.winfo_children():
            widget.destroy()
        self.setup_ui()