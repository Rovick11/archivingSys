import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class SettingsPage:
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
            "text_dark": "#1e1e1e",
            "text_medium": "#666666",
            "text_light": "#999999",
            "border": "#e0e0e0",
            "card_bg": "#ffffff"
        }
        
        # Admin info (display only)
        self.admin_info = {
            "username": "super_admin",
            "full_name": "Super Administrator",
            "email": "admin@archivingsystem.com",
            "role": "Super Admin",
            "member_since": "2024-01-01",
            "last_login": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        self.setup_ui()
    
    def setup_ui(self):
        """Main UI for Settings Page"""
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
            text="👤",
            font=("Segoe UI", 22),
            bg=self.colors["primary_light"],
            fg=self.colors["primary"]
        ).place(relx=0.5, rely=0.5, anchor="center")
        
        # Title text
        text_frame = tk.Frame(title_frame, bg="white")
        text_frame.pack(side="left")
        
        tk.Label(
            text_frame,
            text="My Profile",
            font=("Segoe UI", 20, "bold"),
            fg=self.colors["text_dark"],
            bg="white"
        ).pack(anchor="w")
        
        tk.Label(
            text_frame,
            text="View your account information and change password",
            font=("Segoe UI", 10),
            fg=self.colors["text_medium"],
            bg="white"
        ).pack(anchor="w")
        
        # ===== SINGLE CARD WITH TWO SECTIONS =====
        card = tk.Frame(main, bg="white", highlightbackground=self.colors["border"], highlightthickness=1)
        card.pack(fill="both", expand=True, padx=40, pady=20)
        
        # Left side - Profile Info
        left_frame = tk.Frame(card, bg="white", width=350)
        left_frame.pack(side="left", fill="y", padx=30, pady=25)
        left_frame.pack_propagate(False)
        
        # Right side - Change Password
        right_frame = tk.Frame(card, bg="white")
        right_frame.pack(side="right", fill="both", expand=True, padx=30, pady=25)
        
        # ===== LEFT SIDE: PROFILE INFO =====
        # Avatar
        avatar = tk.Frame(
            left_frame,
            bg=self.colors["primary_light"],
            width=100,
            height=100
        )
        avatar.pack(pady=(0, 20))
        avatar.pack_propagate(False)
        
        tk.Label(
            avatar,
            text="👤",
            font=("Segoe UI", 48),
            bg=self.colors["primary_light"],
            fg=self.colors["primary"]
        ).place(relx=0.5, rely=0.5, anchor="center")
        
        # Full Name
        tk.Label(
            left_frame,
            text=self.admin_info["full_name"],
            font=("Segoe UI", 18, "bold"),
            fg=self.colors["text_dark"],
            bg="white"
        ).pack(pady=(0, 5))
        
        # Username
        tk.Label(
            left_frame,
            text=f"@{self.admin_info['username']}",
            font=("Segoe UI", 11),
            fg=self.colors["accent"],
            bg="white"
        ).pack(pady=(0, 5))
        
        # Role Badge
        role_badge = tk.Frame(
            left_frame,
            bg=self.colors["primary_light"],
            padx=12,
            pady=4
        )
        role_badge.pack(pady=(0, 20))
        
        tk.Label(
            role_badge,
            text=self.admin_info["role"],
            font=("Segoe UI", 10, "bold"),
            fg=self.colors["primary"],
            bg=self.colors["primary_light"]
        ).pack()
        
        # Separator
        ttk.Separator(left_frame, orient="horizontal").pack(fill="x", pady=15)
        
        # Contact Details
        details_frame = tk.Frame(left_frame, bg="white")
        details_frame.pack(fill="x")
        
        # Email
        email_frame = tk.Frame(details_frame, bg="white")
        email_frame.pack(fill="x", pady=8)
        
        tk.Label(
            email_frame,
            text="📧",
            font=("Segoe UI", 12),
            fg=self.colors["text_medium"],
            bg="white",
            width=3
        ).pack(side="left")
        
        tk.Label(
            email_frame,
            text=self.admin_info["email"],
            font=("Segoe UI", 10),
            fg=self.colors["text_dark"],
            bg="white"
        ).pack(side="left", padx=(5, 0))
        
        # Member Since
        since_frame = tk.Frame(details_frame, bg="white")
        since_frame.pack(fill="x", pady=8)
        
        tk.Label(
            since_frame,
            text="📅",
            font=("Segoe UI", 12),
            fg=self.colors["text_medium"],
            bg="white",
            width=3
        ).pack(side="left")
        
        tk.Label(
            since_frame,
            text=f"Member since {self.admin_info['member_since']}",
            font=("Segoe UI", 10),
            fg=self.colors["text_dark"],
            bg="white"
        ).pack(side="left", padx=(5, 0))
        
        # Last Login
        login_frame = tk.Frame(details_frame, bg="white")
        login_frame.pack(fill="x", pady=8)
        
        tk.Label(
            login_frame,
            text="🕒",
            font=("Segoe UI", 12),
            fg=self.colors["text_medium"],
            bg="white",
            width=3
        ).pack(side="left")
        
        tk.Label(
            login_frame,
            text=f"Last login: {self.admin_info['last_login']}",
            font=("Segoe UI", 10),
            fg=self.colors["text_dark"],
            bg="white"
        ).pack(side="left", padx=(5, 0))
        
        # ===== RIGHT SIDE: CHANGE PASSWORD =====
        # Section Title
        tk.Label(
            right_frame,
            text="Change Password",
            font=("Segoe UI", 16, "bold"),
            fg=self.colors["primary"],
            bg="white"
        ).pack(anchor="w", pady=(0, 20))
        
        # Current Password
        current_frame = tk.Frame(right_frame, bg="white")
        current_frame.pack(fill="x", pady=10)
        
        tk.Label(
            current_frame,
            text="Current Password",
            font=("Segoe UI", 11),
            fg=self.colors["text_dark"],
            bg="white",
            width=15,
            anchor="w"
        ).pack(side="left")
        
        self.current_password = tk.Entry(
            current_frame,
            font=("Segoe UI", 11),
            bg="#f8f9fa",
            bd=1,
            relief="solid",
            highlightbackground=self.colors["border"],
            show="•",
            width=25
        )
        self.current_password.pack(side="left", padx=(10, 0), ipady=8, fill="x", expand=True)
        
        # New Password
        new_frame = tk.Frame(right_frame, bg="white")
        new_frame.pack(fill="x", pady=10)
        
        tk.Label(
            new_frame,
            text="New Password",
            font=("Segoe UI", 11),
            fg=self.colors["text_dark"],
            bg="white",
            width=15,
            anchor="w"
        ).pack(side="left")
        
        self.new_password = tk.Entry(
            new_frame,
            font=("Segoe UI", 11),
            bg="#f8f9fa",
            bd=1,
            relief="solid",
            highlightbackground=self.colors["border"],
            show="•",
            width=25
        )
        self.new_password.pack(side="left", padx=(10, 0), ipady=8, fill="x", expand=True)
        
        # Password Strength
        self.strength_label = tk.Label(
            right_frame,
            text="",
            font=("Segoe UI", 9),
            bg="white"
        )
        self.strength_label.pack(anchor="w", pady=(0, 5), padx=105)
        self.new_password.bind("<KeyRelease>", self.check_password_strength)
        
        # Confirm Password
        confirm_frame = tk.Frame(right_frame, bg="white")
        confirm_frame.pack(fill="x", pady=10)
        
        tk.Label(
            confirm_frame,
            text="Confirm Password",
            font=("Segoe UI", 11),
            fg=self.colors["text_dark"],
            bg="white",
            width=15,
            anchor="w"
        ).pack(side="left")
        
        self.confirm_password = tk.Entry(
            confirm_frame,
            font=("Segoe UI", 11),
            bg="#f8f9fa",
            bd=1,
            relief="solid",
            highlightbackground=self.colors["border"],
            show="•",
            width=25
        )
        self.confirm_password.pack(side="left", padx=(10, 0), ipady=8, fill="x", expand=True)
        
        # Password Hint
        hint_frame = tk.Frame(right_frame, bg="white")
        hint_frame.pack(fill="x", pady=(10, 15))
        
        tk.Label(
            hint_frame,
            text="ℹ️ Password must be at least 6 characters",
            font=("Segoe UI", 9),
            fg=self.colors["text_light"],
            bg="white"
        ).pack(anchor="w", padx=105)
        
        # Show Password Toggle
        show_frame = tk.Frame(right_frame, bg="white")
        show_frame.pack(fill="x", pady=(0, 20))
        
        self.show_password = tk.BooleanVar(value=False)
        show_check = tk.Checkbutton(
            show_frame,
            text="Show Password",
            variable=self.show_password,
            bg="white",
            font=("Segoe UI", 10),
            command=self.toggle_password_visibility
        )
        show_check.pack(anchor="w", padx=105)
        
        # Buttons
        button_frame = tk.Frame(right_frame, bg="white")
        button_frame.pack(pady=10)
        
        tk.Button(
            button_frame,
            text="🔑 Update Password",
            font=("Segoe UI", 11, "bold"),
            bg=self.colors["accent"],
            fg="white",
            padx=25,
            pady=10,
            cursor="hand2",
            relief="flat",
            command=self.change_password
        ).pack(side="left", padx=8)
        
        tk.Button(
            button_frame,
            text="🗑️ Clear",
            font=("Segoe UI", 11),
            bg="#f0f0f0",
            fg=self.colors["text_dark"],
            padx=25,
            pady=10,
            cursor="hand2",
            relief="flat",
            command=self.clear_password_fields
        ).pack(side="left", padx=8)
    
    def toggle_password_visibility(self):
        """Toggle password visibility"""
        show = self.show_password.get()
        show_char = "" if show else "•"
        
        self.current_password.config(show=show_char)
        self.new_password.config(show=show_char)
        self.confirm_password.config(show=show_char)
    
    def check_password_strength(self, event=None):
        """Check password strength"""
        password = self.new_password.get()
        
        if not password:
            self.strength_label.config(text="")
            return
        
        # Check strength
        strength = 0
        if len(password) >= 8:
            strength += 1
        if any(c.isupper() for c in password):
            strength += 1
        if any(c.isdigit() for c in password):
            strength += 1
        if any(c in "!@#$%^&*" for c in password):
            strength += 1
        
        if strength <= 1:
            text = "Weak"
            color = self.colors["danger"]
        elif strength <= 2:
            text = "Fair"
            color = self.colors["warning"]
        elif strength <= 3:
            text = "Good"
            color = "#FFA500"
        else:
            text = "Strong"
            color = self.colors["success"]
        
        self.strength_label.config(text=f"🔐 Password Strength: {text}", fg=color)
    
    def change_password(self):
        """Change user password"""
        current = self.current_password.get()
        new = self.new_password.get()
        confirm = self.confirm_password.get()
        
        # Validate
        if not current or not new or not confirm:
            messagebox.showwarning("Warning", "Please fill in all password fields!")
            return
        
        if new != confirm:
            messagebox.showerror("Error", "New password and confirm password do not match!")
            return
        
        if len(new) < 6:
            messagebox.showerror("Error", "Password must be at least 6 characters!")
            return
        
        # Simulate current password check
        if current != "admin123":
            messagebox.showerror("Error", "Current password is incorrect!")
            return
        
        messagebox.showinfo("Success", "Password changed successfully!")
        self.clear_password_fields()
    
    def clear_password_fields(self):
        """Clear all password fields"""
        self.current_password.delete(0, tk.END)
        self.new_password.delete(0, tk.END)
        self.confirm_password.delete(0, tk.END)
        self.strength_label.config(text="")
    
    def show(self):
        """Show the settings page"""
        for widget in self.parent.winfo_children():
            widget.destroy()
        self.setup_ui()


# Test the application
if __name__ == "__main__":
    root = tk.Tk()
    root.title("My Profile")
    root.geometry("1000x650")
    
    app = SettingsPage(root)
    
    root.mainloop()