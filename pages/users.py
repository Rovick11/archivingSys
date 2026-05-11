import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class UsersPage:
    def __init__(self, parent, header_color="#0b3a6f", main_bg="#f5f7fa"):
        self.parent = parent
        self.header_color = header_color
        self.main_bg = main_bg
        
        # Professional color palette
        self.colors = {
            "primary": "#0b3a6f",
            "primary_light": "#e8f0fe",
            "accent": "#1976D2",
            "success": "#2E7D32",
            "warning": "#ED6C02",
            "danger": "#D32F2F",
            "text_dark": "#1e1e1e",
            "text_medium": "#666666",
            "text_light": "#999999",
            "border": "#e0e0e0",
            "card_bg": "#ffffff",
            "hover_bg": "#f5f5f5"
        }
        
        self.users = []
        self.main_frame = None
        
        self.setup_ui()
    
    def setup_ui(self):
        """Main UI for Users Page"""
        # Main container
        self.main_frame = tk.Frame(self.parent, bg=self.main_bg)
        self.main_frame.pack(fill="both", expand=True)
        
        # ===== HEADER SECTION =====
        header = tk.Frame(self.main_frame, bg="white", height=85)
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
            text="👥",
            font=("Segoe UI", 20),
            bg=self.colors["primary_light"],
            fg=self.colors["primary"]
        ).place(relx=0.5, rely=0.5, anchor="center")
        
        # Title text    
        text_frame = tk.Frame(title_frame, bg="white")
        text_frame.pack(side="left")
        
        tk.Label(
            text_frame,
            text="User Management",
            font=("Segoe UI", 20, "bold"),
            fg=self.colors["text_dark"],
            bg="white"
        ).pack(anchor="w")
        
        tk.Label(
            text_frame,
            text="Manage system users and permissions",
            font=("Segoe UI", 10),
            fg=self.colors["text_medium"],
            bg="white"
        ).pack(anchor="w")
        
        # Add User Button
        add_btn = tk.Button(
            header,
            text="+ Add New User",
            font=("Segoe UI", 11, "bold"),
            bg=self.colors["accent"],
            fg="white",
            padx=22,
            pady=10,
            cursor="hand2",
            relief="flat",
            activebackground="#1565C0",
            activeforeground="white",
            command=self.open_add_user_form
        )
        add_btn.pack(side="right", padx=30, pady=25)
        
        # ===== SEARCH AND FILTER SECTION =====
        search_filter = tk.Frame(self.main_frame, bg="white", height=80)
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
        self.search_entry.insert(0, "Search by username, name or email...")
        self.search_entry.bind("<FocusIn>", self.clear_search_placeholder)
        self.search_entry.bind("<FocusOut>", self.set_search_placeholder)
        self.search_entry.bind("<KeyRelease>", self.search_users)
        
        # RIGHT - Filter
        right_frame = tk.Frame(search_filter, bg="white")
        right_frame.pack(side="right", padx=30)
        
        tk.Label(
            right_frame,
            text="Filter:",
            font=("Segoe UI", 11),
            fg=self.colors["text_medium"],
            bg="white"
        ).pack(side="left", padx=(0, 10))
        
        self.filter_var = tk.StringVar(value="All Users")
        filter_combo = ttk.Combobox(
            right_frame,
            textvariable=self.filter_var,
            values=["All Users", "Admin", "Staff", "Viewer", "Active", "Inactive"],
            state="readonly",
            width=15,
            font=("Segoe UI", 11)
        )
        filter_combo.pack(side="left")
        filter_combo.bind("<<ComboboxSelected>>", self.filter_users)
        
        # ===== USERS TABLE (PANTAY SA SEARCH BAR) =====
        self.create_users_table()
    
    def create_users_table(self):
        """Users table with same padding as search bar"""
        # Table container with same padding as search/filter (padx=30)
        table_container = tk.Frame(self.main_frame, bg="white")
        table_container.pack(fill="both", expand=True, padx=30)
        table_container.config(highlightbackground=self.colors["border"], highlightthickness=1)
        
        # Table header
        header = tk.Frame(table_container, bg="#f8f9fa", height=50)
        header.pack(fill="x")
        header.pack_propagate(False)
        
        tk.Label(
            header,
            text="📋 User Directory",
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
        
        # Treeview
        columns = ("ID", "Username", "Full Name", "Email", "Type", "Department", "Status", "Last Login")
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
            ("ID", 50, "center"),
            ("Username", 120, "center"),
            ("Full Name", 150, "w"),
            ("Email", 200, "w"),
            ("Type", 100, "center"),
            ("Department", 120, "center"),
            ("Status", 100, "center"),
            ("Last Login", 140, "center")
        ]
        
        for col, width, anchor in configs:
            self.tree.heading(col, text=col, command=lambda c=col: self.sort_column(c))
            self.tree.column(col, width=width, anchor=anchor)
        
        self.tree.pack(fill="both", expand=True)
        
        # Tags for styling
        self.tree.tag_configure("evenrow", background="#f9f9f9")
        self.tree.tag_configure("oddrow", background="white")
        self.tree.tag_configure("active", foreground=self.colors["success"])
        self.tree.tag_configure("inactive", foreground=self.colors["text_light"])
        self.tree.tag_configure("admin", foreground=self.colors["primary"], font=("Segoe UI", 10, "bold"))
        self.tree.tag_configure("placeholder", foreground=self.colors["text_light"])
        
        # Show placeholder
        self.show_placeholder()
        
        # Bind double-click to edit
        self.tree.bind("<Double-Button-1>", self.edit_user)
    
    def show_placeholder(self):
        """Show placeholder when no users"""
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        self.tree.insert("", "end", values=(
            "-", "No users", "No users found", "-", "-", "-", "-", "-"
        ), tags=("placeholder",))
    
    def load_users(self, users=None):
        """Load users into table"""
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        users_to_show = users if users is not None else self.users
        
        if not users_to_show:
            self.show_placeholder()
            return
        
        for i, user in enumerate(users_to_show):
            tags = ["evenrow" if i % 2 == 0 else "oddrow"]
            status = user.get("status", "inactive")
            tags.append(status)
            
            user_type = user.get("user_type", "")
            if user_type == "admin":
                tags.append("admin")
            
            status_display = "Active" if status == "active" else "Inactive"
            
            values = (
                user.get("id", "-"),
                user.get("username", "-"),
                user.get("full_name", "-"),
                user.get("email", "-"),
                user.get("user_type", "-").title(),
                user.get("department", "-") or "-",
                status_display,
                user.get("last_login", "Never")
            )
            
            self.tree.insert("", "end", values=values, tags=tuple(tags))
    
    def clear_search_placeholder(self, event):
        if self.search_entry.get() == "Search by username, name or email...":
            self.search_entry.delete(0, tk.END)
            self.search_entry.config(fg=self.colors["text_dark"])
    
    def set_search_placeholder(self, event):
        if not self.search_entry.get():
            self.search_entry.insert(0, "Search by username, name or email...")
            self.search_entry.config(fg=self.colors["text_light"])
    
    def search_users(self, event=None):
        """Search users by keyword"""
        keyword = self.search_entry.get().lower()
        
        if keyword in ["", "search by username, name or email..."]:
            self.load_users()
            return
        
        if not self.users:
            self.show_placeholder()
            return
        
        filtered = [
            u for u in self.users
            if keyword in u.get("username", "").lower() or
               keyword in u.get("full_name", "").lower() or
               keyword in u.get("email", "").lower()
        ]
        
        if filtered:
            self.load_users(filtered)
        else:
            for item in self.tree.get_children():
                self.tree.delete(item)
            self.tree.insert("", "end", values=(
                "-", "No results", f"No matches found", "-", "-", "-", "-", "-"
            ), tags=("placeholder",))
    
    def filter_users(self, event=None):
        """Filter users by type or status"""
        filter_by = self.filter_var.get()
        
        if not self.users:
            self.show_placeholder()
            return
        
        if filter_by == "All Users":
            self.load_users()
            return
        
        if filter_by in ["Admin", "Staff", "Viewer"]:
            filtered = [u for u in self.users if u.get("user_type", "").lower() == filter_by.lower()]
        else:
            filtered = [u for u in self.users if u.get("status", "").lower() == filter_by.lower()]
        
        if filtered:
            self.load_users(filtered)
        else:
            for item in self.tree.get_children():
                self.tree.delete(item)
            self.tree.insert("", "end", values=(
                "-", "No results", f"No {filter_by.lower()} users", "-", "-", "-", "-", "-"
            ), tags=("placeholder",))
    
    def sort_column(self, col):
        """Sort treeview by column"""
        if not self.tree.get_children():
            return
        
        data = [(self.tree.set(child, col), child) for child in self.tree.get_children('')]
        data.sort()
        
        for index, (val, child) in enumerate(data):
            self.tree.move(child, '', index)
    
    def open_add_user_form(self):
        """Add user form with Save and Cancel buttons"""
        dialog = tk.Toplevel(self.parent)
        dialog.title("Add New User")
        dialog.geometry("500x650")
        dialog.resizable(False, False)
        dialog.grab_set()
        dialog.configure(bg="white")
        
        # Center the dialog
        dialog.update_idletasks()
        x = (dialog.winfo_screenwidth() // 2) - 250
        y = (dialog.winfo_screenheight() // 2) - 325
        dialog.geometry(f"+{x}+{y}")
        
        # Main container
        main = tk.Frame(dialog, bg="white", padx=30, pady=20)
        main.pack(fill="both", expand=True)
        
        # ===== HEADER =====
        tk.Label(
            main,
            text="➕ Add New User",
            font=("Segoe UI", 20, "bold"),
            fg=self.colors["accent"],
            bg="white"
        ).pack(pady=(0, 5))
        
        tk.Label(
            main,
            text="Fill in the user information below",
            font=("Segoe UI", 10),
            fg=self.colors["text_medium"],
            bg="white"
        ).pack(pady=(0, 20))
        
        # ===== FORM FIELDS =====
        form_frame = tk.Frame(main, bg="white")
        form_frame.pack(fill="both", expand=True)
        
        fields = [
            {"label": "Username", "type": "entry", "required": True},
            {"label": "Password", "type": "password", "required": True},
            {"label": "Full Name", "type": "entry", "required": True},
            {"label": "Email", "type": "entry", "required": True},
            {"label": "User Type", "type": "combobox", "options": ["Admin", "Staff", "Viewer"], "required": True},
            {"label": "Department", "type": "entry", "required": False},
            {"label": "Status", "type": "combobox", "options": ["Active", "Inactive"], "required": False}
        ]
        
        entries = {}
        
        for field in fields:
            row = tk.Frame(form_frame, bg="white")
            row.pack(fill="x", pady=6)
            
            label_text = field["label"]
            if field["required"]:
                label_text += " *"
            
            tk.Label(
                row,
                text=label_text,
                font=("Segoe UI", 11),
                fg=self.colors["text_dark"],
                bg="white",
                width=12,
                anchor="w"
            ).pack(side="left")
            
            if field["type"] == "entry":
                entry = tk.Entry(
                    row,
                    font=("Segoe UI", 11),
                    bg="#f8f9fa",
                    bd=1,
                    relief="solid",
                    highlightbackground=self.colors["border"]
                )
                entry.pack(side="left", fill="x", expand=True, ipady=6)
                entries[field["label"]] = entry
                
            elif field["type"] == "password":
                entry = tk.Entry(
                    row,
                    font=("Segoe UI", 11),
                    bg="#f8f9fa",
                    bd=1,
                    relief="solid",
                    highlightbackground=self.colors["border"],
                    show="•"
                )
                entry.pack(side="left", fill="x", expand=True, ipady=6)
                entries[field["label"]] = entry
                
            else:  # combobox
                combo = ttk.Combobox(
                    row,
                    values=field["options"],
                    state="readonly",
                    font=("Segoe UI", 11)
                )
                combo.pack(side="left", fill="x", expand=True)
                if field["label"] == "Status":
                    combo.set("Active")
                entries[field["label"]] = combo
        
        # ===== REQUIRED NOTE =====
        tk.Label(
            main,
            text="* Required fields",
            font=("Segoe UI", 9),
            fg=self.colors["text_light"],
            bg="white"
        ).pack(pady=(15, 10), anchor="w")
        
        # ===== BUTTONS =====
        button_frame = tk.Frame(main, bg="white")
        button_frame.pack(pady=20)
        
        # Save Button
        save_btn = tk.Button(
            button_frame,
            text="💾 Save User",
            font=("Segoe UI", 12, "bold"),
            bg=self.colors["accent"],
            fg="white",
            width=15,
            pady=8,
            cursor="hand2",
            relief="flat",
            activebackground="#1565C0",
            activeforeground="white",
            command=lambda: self.save_new_user(entries, dialog)
        )
        save_btn.pack(side="left", padx=10)
        
        # Cancel Button
        cancel_btn = tk.Button(
            button_frame,
            text="✕ Cancel",
            font=("Segoe UI", 12),
            bg="#e0e0e0",
            fg=self.colors["text_dark"],
            width=15,
            pady=8,
            cursor="hand2",
            relief="flat",
            activebackground="#d0d0d0",
            command=dialog.destroy
        )
        cancel_btn.pack(side="left", padx=10)
    
    def save_new_user(self, entries, dialog):
        """Save new user"""
        username = entries["Username"].get().strip()
        password = entries["Password"].get()
        full_name = entries["Full Name"].get().strip()
        email = entries["Email"].get().strip()
        user_type = entries["User Type"].get()
        department = entries["Department"].get().strip()
        status = entries["Status"].get()
        
        # Validate
        if not username:
            messagebox.showwarning("Required Field", "Username is required!")
            return
        if not password:
            messagebox.showwarning("Required Field", "Password is required!")
            return
        if not full_name:
            messagebox.showwarning("Required Field", "Full Name is required!")
            return
        if not email:
            messagebox.showwarning("Required Field", "Email is required!")
            return
        if not user_type:
            messagebox.showwarning("Required Field", "User Type is required!")
            return
        
        # Create user
        new_user = {
            "id": len(self.users) + 1,
            "username": username,
            "full_name": full_name,
            "email": email,
            "user_type": user_type.lower(),
            "department": department if department else None,
            "status": status.lower() if status else "active",
            "last_login": "Never"
        }
        
        self.users.append(new_user)
        self.load_users()
        
        messagebox.showinfo("Success", f"User '{username}' added successfully!")
        dialog.destroy()
    
    def edit_user(self, event):
        """Edit selected user"""
        selected = self.tree.selection()
        if not selected:
            return
        
        item = self.tree.item(selected[0])
        values = item["values"]
        
        if values[1] in ["No users", "No results"]:
            return
        
        user_id = values[0]
        user = next((u for u in self.users if u["id"] == user_id), None)
        
        if user:
            messagebox.showinfo(
                "Edit User",
                f"✏️ Edit User: {user['full_name']}\n\n"
                f"Username: {user['username']}\n"
                f"Email: {user['email']}\n"
                f"Type: {user['user_type'].title()}\n"
                f"Status: {user['status'].title()}\n\n"
                f"Edit functionality coming soon!"
            )
    
    def show(self):
        """Show the users page"""
        for widget in self.parent.winfo_children():
            widget.destroy()
        self.setup_ui()


# Test the application
if __name__ == "__main__":
    root = tk.Tk()
    root.title("User Management")
    root.geometry("1200x800")
    
    app = UsersPage(root)
    
    root.mainloop()