import tkinter as tk
from tkinter import ttk, messagebox
import sv_ttk

class UserLoginWindow:
    def __init__(self):
        # Create root window
        self.root = tk.Tk()
        self.root.title("Employee Archiving System - User Login")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        
        # Center window
        self.center_window()
        
        # Apply Sun Valley theme (same as super admin)
        sv_ttk.set_theme("light")
        
        # Color scheme (same as super admin)
        self.primary_color = "#2196F3"
        self.secondary_color = "#1976D2"
        
        # Password visibility flag
        self.password_visible = False
        
        # Setup UI
        self.setup_ui()
    
    def center_window(self):
        """Center the window on screen"""
        self.root.update_idletasks()
        w, h = 400, 500
        x = (self.root.winfo_screenwidth() // 2) - (w // 2)
        y = (self.root.winfo_screenheight() // 2) - (h // 2)
        self.root.geometry(f'{w}x{h}+{x}+{y}')
    
    def setup_ui(self):
        """Create all UI elements"""
        # Main container with padding (same as super admin)
        main = ttk.Frame(self.root, padding="40 30 40 30")
        main.pack(fill=tk.BOTH, expand=True)
        
        # Header section
        self.create_header(main)
        
        # Form fields
        self.create_form_fields(main)
        
        # Login button
        self.create_login_button(main)
        
        # Bind Enter key to login
        self.root.bind('<Return>', lambda e: self.login())
    
    def create_header(self, parent):
        """Create header section"""
        # Welcome title
        ttk.Label(parent, text="Welcome Back!", 
                 font=("Segoe UI", 24, "bold"), 
                 foreground=self.primary_color).pack(pady=(0, 5))
        
        # Subtitle - specific for user role
        ttk.Label(parent, text="Please sign in to Continue",
                 font=("Segoe UI", 10), 
                 foreground="#666666").pack(pady=(0, 30))
    
    def create_form_fields(self, parent):
        """Create username and password fields with show/hide"""
        # Username field
        ttk.Label(parent, text="Username",
                 font=("Segoe UI", 10)).pack(anchor=tk.W, pady=(0, 5))
        
        self.username = ttk.Entry(parent, font=("Segoe UI", 11))
        self.username.pack(fill=tk.X, pady=(0, 15))
        self.username.focus()
        
        # Password field with show/hide button container
        ttk.Label(parent, text="Password",
                 font=("Segoe UI", 10)).pack(anchor=tk.W, pady=(0, 5))
        
        # Frame to hold password entry and show/hide button
        password_frame = ttk.Frame(parent)
        password_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Password entry (initially hidden)
        self.password = ttk.Entry(password_frame, font=("Segoe UI", 11), show="•")
        self.password.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        # Show/Hide button
        self.toggle_btn = tk.Button(
            password_frame, 
            text="👁 Show", 
            font=("Segoe UI", 9),
            bg="white", 
            fg=self.primary_color,
            relief=tk.FLAT, 
            cursor="hand2",
            command=self.toggle_password
        )
        self.toggle_btn.pack(side=tk.RIGHT, padx=(5, 0))
        
        # Hover effect for toggle button
        self.toggle_btn.bind("<Enter>", lambda e: self.toggle_btn.config(bg="#f0f0f0"))
        self.toggle_btn.bind("<Leave>", lambda e: self.toggle_btn.config(bg="white"))
    
    def toggle_password(self):
        """Toggle password visibility"""
        if self.password_visible:
            # Hide password
            self.password.config(show="•")
            self.toggle_btn.config(text="👁 Show")
            self.password_visible = False
        else:
            # Show password
            self.password.config(show="")
            self.toggle_btn.config(text="🙈 Hide")
            self.password_visible = True
    
    def create_login_button(self, parent):
        """Create login button with hover effects"""
        self.login_btn = tk.Button(parent, text="LOGIN",
                                  font=("Segoe UI", 11, "bold"),
                                  bg=self.primary_color, fg="white",
                                  activebackground=self.secondary_color,
                                  activeforeground="white",
                                  relief=tk.FLAT, cursor="hand2", height=2,
                                  command=self.login)
        self.login_btn.pack(fill=tk.X, pady=(20, 0))
        
        # Hover effects
        self.login_btn.bind("<Enter>", self.on_enter)
        self.login_btn.bind("<Leave>", self.on_leave)
    
    def on_enter(self, e):
        """Hover effect - darker blue"""
        self.login_btn['background'] = self.secondary_color
    
    def on_leave(self, e):
        """Remove hover effect - back to primary blue"""
        self.login_btn['background'] = self.primary_color
    
    def login(self):
        """Handle login button click"""
        user = self.username.get().strip()
        pwd = self.password.get()
        
        # Validation
        if not user or not pwd:
            messagebox.showwarning("Warning", "Please enter both username and password!")
            return
        
        # ==============================================
        # TODO: Replace this with actual user validation
        # For now, demo credentials for USER role:
        # Username: user
        # Password: user123
        # ==============================================
        
        if user == "user" and pwd == "user123":
            messagebox.showinfo("Success", "Login successful! Welcome User!")
            self.root.destroy()  # Close login window
            
            # Open user dashboard (user.py)
            try:
                from user_achiving import UserDashboard
                dashboard = UserDashboard(username=user)
                dashboard.run()
            except ImportError as e:
                messagebox.showerror("Error", f"Dashboard not found: {e}")
            except Exception as e:
                messagebox.showerror("Error", f"Error opening dashboard: {e}")
        else:
            messagebox.showerror("Error", "Invalid username or password!")
    
    def run(self):
        """Run the application"""
        self.root.mainloop()


# For testing standalone
if __name__ == "__main__":
    app = UserLoginWindow()
    app.run()