import tkinter as tk
from tkinter import ttk, messagebox
import sv_ttk
from datetime import datetime
from PIL import Image, ImageTk, ImageDraw


class Dashboard:

    def __init__(self, user_type="super_admin"):

        self.root = tk.Tk()
        self.root.title("Archiving System")
        self.root.state("zoomed")
        self.root.minsize(1300, 700)

        sv_ttk.set_theme("light")

        # colors
        self.sidebar_color = "#f2f3f5"
        self.header_color = "#0b3a6f"
        self.main_bg = "#f5f6f7"
        self.accent_color = "#0b3a6f"
        
        # For dropdown menu
        self.menu_visible = False

        self.setup_ui()

    def setup_ui(self):
        container = tk.Frame(self.root)
        container.pack(fill="both", expand=True)
        self.create_sidebar(container)
        self.create_main(container)

    # ---------------- SIDEBAR ---------------- #

    def create_sidebar(self, parent):
        sidebar = tk.Frame(parent, bg=self.sidebar_color, width=280)
        sidebar.pack(side="left", fill="y")
        sidebar.pack_propagate(False)

        # Logo Section
        logo_frame = tk.Frame(sidebar, bg=self.sidebar_color)
        logo_frame.pack(fill="x", pady=(30, 10))

        # Logo image (try to load, fallback to icon)
        try:
            img = Image.open("header.png")
            size = min(img.size)
            img = img.crop((0, 0, size, size))
            img = img.resize((100, 100), Image.Resampling.LANCZOS)
            
            mask = Image.new('L', (100, 100), 0)
            draw = ImageDraw.Draw(mask)
            draw.ellipse((0, 0, 100, 100), fill=255)
            
            result = Image.new('RGBA', (100, 100), (0, 0, 0, 0))
            result.paste(img, (0, 0), mask)
            
            self.logo_photo = ImageTk.PhotoImage(result)
            
            tk.Label(
                logo_frame,
                image=self.logo_photo,
                bg=self.sidebar_color
            ).pack()
        except:
            tk.Label(
                logo_frame,
                text="🏢",
                font=("Segoe UI", 48),
                fg=self.header_color,
                bg=self.sidebar_color
            ).pack()

        # System Name
        tk.Label(
            logo_frame,
            text="ARCHIVING SYSTEM",
            font=("Segoe UI", 12, "bold"),
            fg=self.header_color,
            bg=self.sidebar_color
        ).pack(pady=(5, 0))

        ttk.Separator(sidebar).pack(fill="x", padx=15, pady=20)

        # Menu Items
        menu_items = [
            ("🏠", "Dashboard", self.show_dashboard),
            ("👥", "Manage User", self.show_users),
            ("📋", "Resolutions", self.show_resolutions),
            ("📁", "Archive", self.show_archive),
            ("📊", "System Logs", self.show_logs),
            ("⚙️", "Settings", self.show_settings)
        ]

        for icon, text, command in menu_items:
            btn = tk.Button(
                sidebar,
                text=f"{icon}  {text}",
                font=("Segoe UI", 12),
                bg=self.sidebar_color,
                fg="#333333",
                activebackground="#d4e3fd",
                activeforeground=self.header_color,
                bd=0,
                anchor="w",
                padx=25,
                pady=12,
                cursor="hand2",
                command=command
            )
            btn.pack(fill="x", padx=5)

        ttk.Separator(sidebar).pack(fill="x", padx=15, pady=20)

        # Logout Button
        tk.Button(
            sidebar,
            text="🚪 Logout",
            font=("Segoe UI", 12),
            bg=self.sidebar_color,
            fg="#dc3545",
            activebackground="#ffebee",
            activeforeground="#dc3545",
            bd=0,
            anchor="w",
            padx=25,
            pady=12,
            cursor="hand2",
            command=self.logout
        ).pack(fill="x", padx=5)

    # ---------------- MAIN AREA ---------------- #

    def create_main(self, parent):
        main = tk.Frame(parent, bg=self.main_bg)
        main.pack(side="left", fill="both", expand=True)

        # ===== HEADER WITH DROPDOWN =====
        header = tk.Frame(main, bg=self.header_color, height=70)
        header.pack(fill="x")
        header.pack_propagate(False)

        # Title label na pwedeng i-update
        self.header_title = tk.Label(
            header,
            text="Dashboard",
            font=("Segoe UI", 20, "bold"),
            fg="white",
            bg=self.header_color
        )
        self.header_title.pack(side="left", padx=20)

        # ===== PROFILE SECTION =====
        profile_frame = tk.Frame(header, bg=self.header_color)
        profile_frame.pack(side="right", padx=20)

        # Profile icon
        profile_icon = tk.Label(
            profile_frame,
            text="👤",
            font=("Segoe UI", 16),
            fg="white",
            bg=self.header_color
        )
        profile_icon.pack(side="left", padx=(0, 5))

        # Admin name
        tk.Label(
            profile_frame,
            text="Super Admin",
            font=("Segoe UI", 12),
            fg="white",
            bg=self.header_color
        ).pack(side="left", padx=(0, 5))

        # Dropdown arrow (▼) - ITO LANG ANG CLICKABLE
        dropdown_btn = tk.Label(
            profile_frame,
            text="▼",
            font=("Segoe UI", 10, "bold"),
            fg="white",
            bg=self.header_color,
            cursor="hand2"
        )
        dropdown_btn.pack(side="left")
        
        # Bind click event sa dropdown arrow LANG
        dropdown_btn.bind("<Button-1>", self.toggle_dropdown)

        # ===== DROPDOWN MENU (initially hidden) =====
        self.dropdown_menu = tk.Frame(
            self.root,
            bg="white",
            highlightbackground="#cccccc",
            highlightthickness=1
        )
        
        # Menu items
        menu_items = [
            ("👤 Profile", self.show_profile),
            ("⚙️ Settings", self.show_settings),
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
                pady=8,
                cursor="hand2"
            )
            item.pack(fill="x")
            
            # Hover effect
            item.bind("<Enter>", lambda e, i=item: i.config(bg="#f0f0f0"))
            item.bind("<Leave>", lambda e, i=item: i.config(bg="white"))
            item.bind("<Button-1>", lambda e, c=command: self.menu_item_click(c))
        
        # Bind click outside to close menu
        self.root.bind("<Button-1>", self.check_click_outside)
        
        # ===== MAIN CONTENT AREA (i-save ito) =====
        self.main_content = tk.Frame(main, bg=self.main_bg)
        self.main_content.pack(fill="both", expand=True, padx=40, pady=30)

        # Default view - Dashboard
        self.show_dashboard()

    # ---------------- DROPDOWN FUNCTIONS ---------------- #

    def toggle_dropdown(self, event=None):
        """Show or hide the dropdown menu"""
        if self.menu_visible:
            self.dropdown_menu.place_forget()
            self.menu_visible = False
        else:
            # Get position - sa kanang bahagi ng header
            x = self.root.winfo_width() - 180  # 180 pixels from right
            y = 70  # Below header
            self.dropdown_menu.place(x=x, y=y, width=150)
            self.menu_visible = True
            self.dropdown_menu.lift()
    
    def check_click_outside(self, event):
        """Close menu if click is outside the dropdown"""
        if self.menu_visible:
            # Check if click is outside the dropdown menu
            widget = event.widget
            if widget != self.dropdown_menu and not str(widget).startswith(str(self.dropdown_menu)):
                # Check if click is not on the dropdown arrow
                if hasattr(widget, 'cget') and widget.cget("text") != "▼":
                    self.dropdown_menu.place_forget()
                    self.menu_visible = False
    
    def menu_item_click(self, command):
        """Handle menu item click"""
        self.dropdown_menu.place_forget()
        self.menu_visible = False
        command()
    
    def show_profile(self):
        messagebox.showinfo("Profile", "Super Admin\nAdministrator")

    # ---------------- PAGE FUNCTIONS ---------------- #

    def show_dashboard(self):
        """Show dashboard content"""
        self.header_title.config(text="Dashboard")
        
        # Clear main content
        for widget in self.main_content.winfo_children():
            widget.destroy()
        
        # Show dashboard components
        self.create_welcome(self.main_content)
        self.create_stats(self.main_content)
        self.create_quick_actions(self.main_content)

    def show_users(self):
        """Show users management page"""
        self.header_title.config(text="User Management")
        
        # Clear main content
        for widget in self.main_content.winfo_children():
            widget.destroy()
        
        # Import and show Users page
        try:
            from pages.users import UsersPage
            users_page = UsersPage(self.main_content, self.header_color, self.main_bg)
        except ImportError:
            tk.Label(
                self.main_content,
                text="Users page not found.\nMake sure 'pages/users.py' exists.",
                font=("Segoe UI", 16),
                fg="red"
            ).pack(expand=True)
        except Exception as e:
            tk.Label(
                self.main_content,
                text=f"Error: {e}",
                font=("Segoe UI", 16),
                fg="red"
            ).pack(expand=True)

    def show_resolutions(self):
        """Show resolutions page"""
        self.header_title.config(text="Resolutions")
    
        for widget in self.main_content.winfo_children():
            widget.destroy()
    
        from pages.resolutions import ResolutionsPage
        resolutions_page = ResolutionsPage(self.main_content, self.header_color, self.main_bg)

    def show_archive(self):
        """Show archive page"""
        self.header_title.config(text="Archive")
        
        for widget in self.main_content.winfo_children():
            widget.destroy()
        
        from pages.archive import ArchivePage
        archive_page = ArchivePage(self.main_content, self.header_color, self.main_bg)

    def show_logs(self):
        """Show system logs page"""
        self.header_title.config(text="System Logs")
        
        for widget in self.main_content.winfo_children():
            widget.destroy()
        
        from pages.logs import LogsPage
        logs_page = LogsPage(self.main_content, self.header_color, self.main_bg)

    def show_settings(self):
        """Show settings page"""
        self.header_title.config(text="Settings")
        
        for widget in self.main_content.winfo_children():
            widget.destroy()
        
        from pages.settings import SettingsPage
        settings_page = SettingsPage(self.main_content, self.header_color, self.main_bg)

    # ---------------- WELCOME BACK ---------------- #

    def create_welcome(self, parent):
        welcome = tk.Frame(parent, bg="#e9ecef", height=100)
        welcome.pack(fill="x", pady=(0, 30))
        welcome.pack_propagate(False)

        # Left side - Welcome text
        left_frame = tk.Frame(welcome, bg="#e9ecef")
        left_frame.pack(side="left", padx=30, pady=15)

        tk.Label(
            left_frame,
            text="👋 Welcome Back,",
            font=("Segoe UI", 16),
            fg="#666666",
            bg="#e9ecef"
        ).pack(anchor="w")

        tk.Label(
            left_frame,
            text="Super Admin!",
            font=("Segoe UI", 28, "bold"),
            fg=self.header_color,
            bg="#e9ecef"
        ).pack(anchor="w")

        # Right side - Date
        date = datetime.now().strftime("%A, %B %d, %Y")
        tk.Label(
            welcome,
            text=f"📅 {date}",
            font=("Segoe UI", 12),
            fg="#666666",
            bg="#e9ecef"
        ).pack(side="right", padx=30)

    # ---------------- STATS CARDS (walang value) ---------------- #

    def create_stats(self, parent):
        stats_frame = tk.Frame(parent, bg=self.main_bg)
        stats_frame.pack(fill="x", pady=(0, 40))

        # Configure grid for 4 columns
        for i in range(4):
            stats_frame.columnconfigure(i, weight=1)

        stats_data = [
            ("📄", "Total Resolutions"),
            ("👥", "Total Users"),
            ("💾", "Archive Size"),
            ("⏳", "Pending Approval")
        ]

        for i, (icon, title) in enumerate(stats_data):
            self.create_stat_card(stats_frame, icon, title, i)

    def create_stat_card(self, parent, icon, title, column):
        """Create a stat card with icon but NO value"""
        card = tk.Frame(
            parent,
            bg="white",
            highlightbackground="#cfcfcf",
            highlightthickness=1,
            height=90
        )
        card.grid(row=0, column=column, padx=10, sticky="nsew")
        card.pack_propagate(False)

        # Center content vertically and horizontally
        content = tk.Frame(card, bg="white")
        content.place(relx=0.5, rely=0.5, anchor="center")

        # Icon and title in same line
        icon_label = tk.Label(
            content,
            text=icon,
            font=("Segoe UI", 14),
            bg="white"
        )
        icon_label.pack(side="left", padx=(0, 8))

        tk.Label(
            content,
            text=title,
            font=("Segoe UI", 11),
            fg="#666666",
            bg="white"
        ).pack(side="left")

    # ---------------- QUICK ACTIONS ---------------- #

    def create_quick_actions(self, parent):
        # Title
        tk.Label(
            parent,
            text="QUICK ACTIONS",
            font=("Segoe UI", 18, "bold"),
            fg=self.header_color,
            bg=self.main_bg
        ).pack(anchor="w", pady=(0, 20))

        # Actions Grid
        actions_frame = tk.Frame(parent, bg=self.main_bg)
        actions_frame.pack(fill="both", expand=True)

        for i in range(3):
            actions_frame.columnconfigure(i, weight=1)

        actions = [
            ("📤", "UPLOAD", "Upload new files", self.upload),
            ("👤", "ADD USER", "Create new user", self.add_user),
            ("📋", "VIEW LOGS", "View System Activities", self.view_logs)
        ]

        for i, (icon, title, desc, command) in enumerate(actions):
            card = tk.Frame(
                actions_frame,
                bg="white",
                highlightbackground=self.header_color,
                highlightthickness=2,
                height=150,
                cursor="hand2"
            )
            card.grid(row=0, column=i, padx=15, pady=10, sticky="nsew")
            card.pack_propagate(False)
            card.bind("<Button-1>", lambda e, c=command: c())

            # Center content
            content = tk.Frame(card, bg="white")
            content.place(relx=0.5, rely=0.5, anchor="center")

            tk.Label(
                content,
                text=icon,
                font=("Segoe UI", 28),
                bg="white"
            ).pack()

            tk.Label(
                content,
                text=title,
                font=("Segoe UI", 14, "bold"),
                fg=self.header_color,
                bg="white"
            ).pack()

            tk.Label(
                content,
                text=desc,
                font=("Segoe UI", 10),
                fg="#666666",
                bg="white"
            ).pack()

    # ---------------- ACTION FUNCTIONS ---------------- #

    def upload(self):
        messagebox.showinfo("Upload", "Upload Files")

    def add_user(self):
        self.show_users()  # Redirect to users page

    def view_logs(self):
        self.show_logs()

    def logout(self):
        if messagebox.askyesno("Logout", "Logout?"):
            self.root.destroy()
            from login import LoginWindow
            LoginWindow().run()

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = Dashboard()
    app.run()