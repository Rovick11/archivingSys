import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import sv_ttk
from datetime import datetime
from PIL import Image, ImageTk, ImageDraw
import os

class UserDashboard:
    def __init__(self, username="user"):
        self.username = username
        self.root = tk.Tk()
        self.root.title("Archiving System - User Portal")
        self.root.state("zoomed")
        self.root.minsize(1100, 600)
        
        # Apply Sun Valley theme
        sv_ttk.set_theme("light")
        
        # Colors
        self.header_color = "#0b3a6f"
        self.main_bg = "#f5f6f7"
        self.accent_color = "#0b3a6f"
        
        # For dropdown menu
        self.menu_visible = False
        
        # For hover effect
        self.current_hover_item = None
        
        # Setup UI
        self.setup_ui()
    
    def setup_ui(self):
        # Main container
        self.main_container = tk.Frame(self.root, bg=self.main_bg)
        self.main_container.pack(fill="both", expand=True)
        
        # Create header
        self.create_header()
        
        # Main content area
        self.main_content = tk.Frame(self.main_container, bg=self.main_bg)
        self.main_content.pack(fill="both", expand=True, padx=40, pady=30)
        
        # Default view - Documents
        self.show_documents()
    
    # ---------------- HEADER WITH DROPDOWN ---------------- #
    
    def create_header(self):
        """Create taller header with logo and profile dropdown"""
        header = tk.Frame(self.main_container, bg=self.header_color, height=120)
        header.pack(fill="x")
        header.pack_propagate(False)
        
        # Left side - Logo and System Name
        left_frame = tk.Frame(header, bg=self.header_color)
        left_frame.pack(side="left", padx=50)
        
        self.setup_logo(left_frame)
        
        # Title container (vertical stack)
        title_frame = tk.Frame(left_frame, bg=self.header_color)
        title_frame.pack(side="left", padx=(8, 0))
        
        # Main title
        tk.Label(
            title_frame,
            text="ARCHIVING SYSTEM",
            font=("Segoe UI", 22, "bold"),
            fg="white",
            bg=self.header_color
        ).pack(anchor="w")
        
        # Subtitle - Sanguniang Bayan ng Nasugbu
        tk.Label(
            title_frame,
            text="Sanguniang Bayan ng Nasugbu",
            font=("Segoe UI", 10),
            fg="#a8c8e8",
            bg=self.header_color
        ).pack(anchor="w", pady=(0, 0))
        
        # Right side - Profile with Dropdown
        right_frame = tk.Frame(header, bg=self.header_color)
        right_frame.pack(side="right", padx=50)
        
        # Profile icon
        tk.Label(
            right_frame,
            text="👤",
            font=("Segoe UI", 22),
            fg="white",
            bg=self.header_color
        ).pack(side="left", padx=(0, 10))
        
        # Username
        tk.Label(
            right_frame,
            text=self.username,
            font=("Segoe UI", 16),
            fg="white",
            bg=self.header_color
        ).pack(side="left", padx=(0, 8))
        
        # Dropdown button frame (para makuha ang position)
        self.dropdown_btn_frame = tk.Frame(right_frame, bg=self.header_color)
        self.dropdown_btn_frame.pack(side="left")
        
        # Dropdown arrow (ito ang clickable)
        self.dropdown_btn = tk.Label(
            self.dropdown_btn_frame,
            text="▼",
            font=("Segoe UI", 12, "bold"),
            fg="white",
            bg=self.header_color,
            cursor="hand2"
        )
        self.dropdown_btn.pack()
        
        # Bind click event
        self.dropdown_btn.bind("<Button-1>", self.toggle_dropdown)
        
        # Dropdown menu
        self.dropdown_menu = tk.Frame(
            self.root,
            bg="white",
            highlightbackground="#cccccc",
            highlightthickness=1
        )
        
        menu_items = [
            ("👤 Profile", self.show_profile),
            ("🚪 Logout", self.logout)
        ]
        
        for text, command in menu_items:
            item = tk.Label(
                self.dropdown_menu,
                text=text,
                font=("Segoe UI", 11),
                fg="#333333",
                bg="white",
                padx=20,
                pady=10,
                cursor="hand2"
            )
            item.pack(fill="x")
            
            item.bind("<Enter>", lambda e, i=item: i.config(bg="#f0f0f0"))
            item.bind("<Leave>", lambda e, i=item: i.config(bg="white"))
            item.bind("<Button-1>", lambda e, c=command: self.menu_item_click(c))
        
        self.root.bind("<Button-1>", self.check_click_outside)
    
    def toggle_dropdown(self, event=None):
        """Show or hide the dropdown menu - eksakto sa ilalim ng dropdown icon"""
        if self.menu_visible:
            self.dropdown_menu.place_forget()
            self.menu_visible = False
        else:
            # Kunin ang eksaktong position ng dropdown button
            x = self.dropdown_btn.winfo_rootx() - self.root.winfo_rootx()
            y = self.dropdown_btn.winfo_rooty() - self.root.winfo_rooty() + self.dropdown_btn.winfo_height()
            
            # I-adjust ang x para umusad pakaliwa (minus 100 pixels)
            x = x - 100
            
            # I-position ang menu sa ilalim ng button
            self.dropdown_menu.place(x=x, y=y, width=140)
            self.menu_visible = True
            self.dropdown_menu.lift()
    
    def check_click_outside(self, event):
        """Close menu if click is outside the dropdown"""
        if self.menu_visible:
            widget = event.widget
            if widget != self.dropdown_menu and not str(widget).startswith(str(self.dropdown_menu)):
                if not (hasattr(widget, 'cget') and widget.cget("text") == "▼"):
                    self.dropdown_menu.place_forget()
                    self.menu_visible = False
    
    def menu_item_click(self, command):
        """Handle menu item click"""
        self.dropdown_menu.place_forget()
        self.menu_visible = False
        command()
    
    def show_profile(self):
        """Show profile info"""
        messagebox.showinfo("Profile", 
            f"👤 User: {self.username}\n"
            f"📋 Role: User\n"
            f"📄 Access: View, Download, Print Documents")
    
    def setup_logo(self, parent):
        """Setup larger logo from logo.png or fallback"""
        logo_path = "logo.png"
        logo_container = tk.Frame(parent, bg=self.header_color)
        logo_container.pack(side="left")
        
        if os.path.exists(logo_path):
            try:
                img = Image.open(logo_path)
                size = min(img.size)
                img = img.crop((0, 0, size, size))
                img = img.resize((80, 80), Image.Resampling.LANCZOS)
                
                mask = Image.new('L', (80, 80), 0)
                draw = ImageDraw.Draw(mask)
                draw.ellipse((0, 0, 80, 80), fill=255)
                
                result = Image.new('RGBA', (80, 80), (0, 0, 0, 0))
                result.paste(img, (0, 0), mask)
                
                self.logo_photo = ImageTk.PhotoImage(result)
                
                tk.Label(
                    logo_container,
                    image=self.logo_photo,
                    bg=self.header_color
                ).pack()
                return
            except Exception as e:
                print(f"Error loading logo: {e}")
        
        # Fallback
        tk.Label(
            logo_container,
            text="📁",
            font=("Segoe UI", 48),
            fg="white",
            bg=self.header_color
        ).pack()
    
    # ---------------- MAIN PAGE ---------------- #
    
    def show_documents(self):
        """Show documents list"""
        for widget in self.main_content.winfo_children():
            widget.destroy()
        
        self.create_welcome_banner()
        self.create_search_bar()
        self.create_documents_table()
    
    # ---------------- WELCOME BANNER ---------------- #
    
    def create_welcome_banner(self):
        """Create welcome banner with date"""
        welcome = tk.Frame(self.main_content, bg="#e9ecef", height=100)
        welcome.pack(fill="x", pady=(0, 25))
        welcome.pack_propagate(False)
        
        left_frame = tk.Frame(welcome, bg="#e9ecef")
        left_frame.pack(side="left", padx=30, pady=15)
        
        tk.Label(
            left_frame,
            text="👋 Welcome,",
            font=("Segoe UI", 14),
            fg="#666666",
            bg="#e9ecef"
        ).pack(anchor="w")
        
        tk.Label(
            left_frame,
            text=f"{self.username}!",
            font=("Segoe UI", 26, "bold"),
            fg=self.header_color,
            bg="#e9ecef"
        ).pack(anchor="w")
        
        date = datetime.now().strftime("%A, %B %d, %Y")
        tk.Label(
            welcome,
            text=f"📅 {date}",
            font=("Segoe UI", 11),
            fg="#666666",
            bg="#e9ecef"
        ).pack(side="right", padx=30)
    
    # ---------------- SEARCH BAR ---------------- #
    
    def create_search_bar(self):
        """Create search bar"""
        search_frame = tk.Frame(self.main_content, bg=self.main_bg)
        search_frame.pack(fill="x", pady=(0, 20))
        
        search_row = tk.Frame(search_frame, bg=self.main_bg)
        search_row.pack(fill="x")
        
        self.search_entry = tk.Entry(
            search_row,
            font=("Segoe UI", 11),
            bg="white",
            relief=tk.SOLID,
            bd=1
        )
        self.search_entry.pack(side="left", fill="x", expand=True, padx=(0, 10), ipady=10)
        self.search_entry.bind("<KeyRelease>", self.on_search)
        
        search_btn = tk.Button(
            search_row,
            text="🔍 Search",
            font=("Segoe UI", 10, "bold"),
            bg=self.accent_color,
            fg="white",
            padx=25,
            pady=10,
            cursor="hand2",
            command=self.on_search
        )
        search_btn.pack(side="left")
        
        clear_btn = tk.Button(
            search_row,
            text="Clear",
            font=("Segoe UI", 10),
            bg="#6c757d",
            fg="white",
            padx=20,
            pady=10,
            cursor="hand2",
            command=self.clear_search
        )
        clear_btn.pack(side="left", padx=(5, 0))
        
        tk.Label(
            search_frame,
            text="💡 Search by filename",
            font=("Segoe UI", 9),
            fg="#888888",
            bg=self.main_bg
        ).pack(anchor="w", pady=(5, 0))
    
    def on_search(self, event=None):
        """Handle search"""
        keyword = self.search_entry.get().strip().lower()
        
        if not keyword:
            self.filtered_files = self.pdf_files.copy()
        else:
            self.filtered_files = [
                f for f in self.pdf_files
                if keyword in f["filename"].lower()
            ]
        
        self.refresh_table()
    
    def clear_search(self):
        """Clear search and show all"""
        self.search_entry.delete(0, tk.END)
        self.filtered_files = self.pdf_files.copy()
        self.refresh_table()
    
    # ---------------- DOCUMENTS TABLE WITH HOVER EFFECT ---------------- #
    
    def create_documents_table(self):
        """Create table with Filename, Date, Size, and Actions columns only"""
        table_frame = tk.Frame(self.main_content, bg=self.main_bg)
        table_frame.pack(fill="both", expand=True)
        
        columns = ("Filename", "Date", "Size", "Actions")
        
        scroll_y = ttk.Scrollbar(table_frame, orient="vertical")
        
        # I-configure ang style para sa bold font ng headings
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Segoe UI", 11, "bold"))
        
        self.tree = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings",
            height=15,
            yscrollcommand=scroll_y.set,
        )
        
        scroll_y.config(command=self.tree.yview)
        
        column_widths = {"Filename": 500, "Date": 120, "Size": 80, "Actions": 180}
        for col, width in column_widths.items():
            self.tree.heading(col, text=col)
            self.tree.column(col, width=width, anchor="w")
        
        self.tree.pack(side="left", fill="both", expand=True)
        scroll_y.pack(side="right", fill="y")
        
        self.load_sample_data()
        self.populate_table()
        
        # Setup hover effect
        self.setup_hover_effect()
        
        self.tree.bind("<Double-1>", self.on_filename_double_click)
        self.tree.bind("<ButtonRelease-1>", self.on_action_click)
    
    def setup_hover_effect(self):
        """Setup hover effect for table rows"""
        # Configure tag for hover effect (gray background)
        self.tree.tag_configure("hover", background="#e0e0e0")  # Light gray
        
        # Bind mouse motion to detect row hover
        self.tree.bind("<Motion>", self.on_mouse_motion)
    
    def on_mouse_motion(self, event):
        """Handle mouse motion to apply hover effect"""
        # Get the row under the mouse
        row_id = self.tree.identify_row(event.y)
        
        # If same row, do nothing
        if row_id == self.current_hover_item:
            return
        
        # Remove hover from previous row
        if self.current_hover_item:
            self.tree.item(self.current_hover_item, tags=())
        
        # Add hover to new row
        if row_id:
            self.tree.item(row_id, tags=("hover",))
            self.current_hover_item = row_id
        else:
            self.current_hover_item = None
    
    def load_sample_data(self):
        """Load sample PDF files data"""
        self.pdf_files = [
            {"filename": "employee_contract_2024.pdf", "date": "2024-01-15", "size": "2.3 MB"},
            {"filename": "performance_review_q1.pdf", "date": "2024-02-20", "size": "1.8 MB"},
            {"filename": "training_certificate.pdf", "date": "2024-03-10", "size": "0.9 MB"},
            {"filename": "salary_adjustment_2024.pdf", "date": "2024-01-05", "size": "1.2 MB"},
            {"filename": "leave_approval_form.pdf", "date": "2024-02-28", "size": "0.7 MB"},
            {"filename": "annual_report_2023.pdf", "date": "2024-01-30", "size": "5.1 MB"},
            {"filename": "clearance_form.pdf", "date": "2024-03-15", "size": "0.6 MB"},
            {"filename": "benefits_guide_2024.pdf", "date": "2024-01-10", "size": "3.2 MB"},
            {"filename": "disciplinary_action.pdf", "date": "2024-02-14", "size": "0.8 MB"},
            {"filename": "promotion_letter.pdf", "date": "2024-03-01", "size": "0.5 MB"},
        ]
        
        self.filtered_files = self.pdf_files.copy()
    
    def populate_table(self):
        """Populate table with documents"""
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for doc in self.filtered_files:
            action_text = "     ⬇️ Download                  🖨️ Print"
            
            self.tree.insert("", tk.END, values=(
                doc["filename"],
                doc["date"],
                doc["size"],
                action_text
            ))
    
    def on_filename_double_click(self, event):
        """Handle double-click on filename column to view document"""
        row_id = self.tree.identify_row(event.y)
        if not row_id:
            return
        
        column = self.tree.identify_column(event.x)
        
        if column == "#1":  # Filename column
            values = self.tree.item(row_id)['values']
            if values and values[0]:
                doc = next((d for d in self.filtered_files if d["filename"] == values[0]), None)
                if doc:
                    self.view_document(doc)
    
    def on_action_click(self, event):
        """Handle clicks on action buttons (Download/Print)"""
        row_id = self.tree.identify_row(event.y)
        if not row_id:
            return
        
        column = self.tree.identify_column(event.x)
        
        if column == "#4":  # Actions column
            values = self.tree.item(row_id)['values']
            if values and values[0]:
                doc = next((d for d in self.filtered_files if d["filename"] == values[0]), None)
                
                if doc:
                    cell_bbox = self.tree.bbox(row_id, column)
                    if cell_bbox:
                        click_x = event.x - cell_bbox[0]
                        
                        if click_x < 90:
                            self.download_document(doc)
                        else:
                            self.print_document(doc)
    
    def refresh_table(self):
        """Refresh table after search"""
        self.populate_table()
        # Reset hover item
        self.current_hover_item = None
    
    # ---------------- DOCUMENT ACTIONS ---------------- #
    
    def view_document(self, doc):
        """View selected document (triggered by double-click)"""
        messagebox.showinfo("View Document", 
            f"📄 {doc['filename']}\n"
            f"📅 Date: {doc['date']}\n"
            f"💾 Size: {doc['size']}\n\n"
            f"▶️ Opening PDF viewer...")
    
    def download_document(self, doc):
        """Download selected document"""
        file_path = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            initialfile=doc["filename"],
            filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")]
        )
        if file_path:
            messagebox.showinfo("Download", 
                f"✅ Downloading: {doc['filename']}\n"
                f"📁 Saved to: {file_path}")
    
    def print_document(self, doc):
        """Print selected document"""
        messagebox.showinfo("Print", 
            f"🖨️ Sending to printer: {doc['filename']}")
    
    # ---------------- LOGOUT ---------------- #
    
    def logout(self):
        if messagebox.askyesno("Logout", "Are you sure you want to logout?"):
            self.root.destroy()
            from login import UserLoginWindow
            login = UserLoginWindow()
            login.run()
    
    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = UserDashboard("John")
    app.run()