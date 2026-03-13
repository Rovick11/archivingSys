import tkinter as tk
from tkinter import ttk


def _build_sidebar(self):
    top = ttk.Frame(self.sidebar, style="Sidebar.TFrame", padding=(18, 24))
    top.pack(fill="x")

    ttk.Label(top, text="ADMIN PANEL", style="SidebarSmall.TLabel").pack(anchor="w")
    ttk.Label(top, text="Document Management", style="SidebarTitle.TLabel").pack(anchor="w", pady=(6, 18))

    nav = ttk.Frame(self.sidebar, style="Sidebar.TFrame", padding=(14, 4))
    nav.pack(fill="x")

    buttons = [
        ("Dashboard", "dashboard"),
        ("Records", "records"),
        ("Upload Files", "upload"),
        ("Deleted Files", "deleted"),
        ("System Logs", "logs"),
        ("Archive / Backup", "archive"),
    ]

    for text, view_name in buttons:
        button = ttk.Button(nav, text=text, style="Nav.TButton", command=lambda name=view_name: self.show_view(name))
        button.pack(fill="x", pady=5)
        self.nav_buttons[view_name] = button

    spacer = ttk.Frame(self.sidebar, style="Sidebar.TFrame")
    spacer.pack(expand=True, fill="both")

    user_box = tk.Frame(self.sidebar, bg="#1e293b", bd=0, highlightthickness=0)
    user_box.pack(fill="x", padx=16, pady=18)
    ttk.Label(user_box, text="Logged in as", style="SidebarSmall.TLabel").pack(anchor="w", padx=14, pady=(14, 4))
    ttk.Label(user_box, text="Admin User", style="SidebarUser.TLabel").pack(anchor="w", padx=14)
    ttk.Label(user_box, text="Role: Admin", style="SidebarSmall.TLabel").pack(anchor="w", padx=14, pady=(2, 14))
