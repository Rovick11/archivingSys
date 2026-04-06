import tkinter as tk
from tkinter import ttk, messagebox
import sv_ttk

class LoginWindow:
    def __init__(self):
        # Create root window
        self.root = tk.Tk()
        self.root.title("Login System - Modern UI")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        
        # Center window
        self.center_window()
        
        # Apply Sun Valley theme
        sv_ttk.set_theme("light")
        
        # Color scheme
        self.primary_color = "#2196F3"
        self.secondary_color = "#1976D2"
        
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
        # Main container with padding
        main = ttk.Frame(self.root, padding="40 30 40 30")
        main.pack(fill=tk.BOTH, expand=True)
        
        # Header
        self.create_header(main)
        
        # Form fields
        self.create_form_fields(main)
        
        # Login button
        self.create_login_button(main)
        
        # Links
        self.create_links(main)
        
        # Bind Enter key
        self.root.bind('<Return>', lambda e: self.login())
    
    def create_header(self, parent):
        """Create header section"""
        # Welcome title
        ttk.Label(parent, text="Welcome Back!", 
                 font=("Segoe UI", 24, "bold"), 
                 foreground=self.primary_color).pack(pady=(0, 5))
        
        # Subtitle
        ttk.Label(parent, text="Please sign in to continue",
                 font=("Segoe UI", 10), 
                 foreground="#666666").pack(pady=(0, 30))
    
    def create_form_fields(self, parent):
        """Create username and password fields"""
        # Username/Email field
        ttk.Label(parent, text="Username or Email",
                 font=("Segoe UI", 10)).pack(anchor=tk.W, pady=(0, 5))
        
        self.username = ttk.Entry(parent, font=("Segoe UI", 11))
        self.username.pack(fill=tk.X, pady=(0, 15))
        self.username.focus()
        
        # Password field
        ttk.Label(parent, text="Password",
                 font=("Segoe UI", 10)).pack(anchor=tk.W, pady=(0, 5))
        
        self.password = ttk.Entry(parent, font=("Segoe UI", 11), show="•")
        self.password.pack(fill=tk.X, pady=(0, 10))
        
        # Remember me checkbox
        self.remember = tk.BooleanVar()
        ttk.Checkbutton(parent, text="Remember me",
                       variable=self.remember).pack(anchor=tk.W, pady=(5, 20))
    
    def create_login_button(self, parent):
        """Create login button with hover effects"""
        self.login_btn = tk.Button(parent, text="LOGIN",
                                  font=("Segoe UI", 11, "bold"),
                                  bg=self.primary_color, fg="white",
                                  activebackground=self.secondary_color,
                                  activeforeground="white",
                                  relief=tk.FLAT, cursor="hand2", height=2,
                                  command=self.login)
        self.login_btn.pack(fill=tk.X, pady=(0, 15))
        
        # Hover effects
        self.login_btn.bind("<Enter>", self.on_enter)
        self.login_btn.bind("<Leave>", self.on_leave)
    
    def create_links(self, parent):
        """Create forgot password and sign up links"""
        # Forgot password
        forgot = tk.Label(parent, text="Forgot Password?",
                         font=("Segoe UI", 10), fg=self.primary_color,
                         bg="white", cursor="hand2")
        forgot.pack(pady=(0, 5))
        forgot.bind("<Button-1>", lambda e: self.forgot())
        
        # Footer with sign up
        footer = ttk.Frame(parent)
        footer.pack(pady=(20, 0))
        
        ttk.Label(footer, text="Don't have an account? ",
                 font=("Segoe UI", 10), foreground="#666666").pack(side=tk.LEFT)
        
        signup = tk.Label(footer, text="Sign Up",
                         font=("Segoe UI", 10, "bold"),
                         fg=self.primary_color, bg="white", cursor="hand2")
        signup.pack(side=tk.LEFT)
        signup.bind("<Button-1>", lambda e: self.signup())
    
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
        
        # Demo credentials
        if user == "admin" and pwd == "admin123":
            messagebox.showinfo("Success", "Login successful! Welcome Super Admin!")
            self.root.destroy()  # Close login window
            
            # Open dashboard
            try:
                from dashboard import Dashboard
                dashboard = Dashboard(user_type="super_admin")
                dashboard.run()
            except ImportError as e:
                messagebox.showerror("Error", f"Dashboard not found: {e}")
            except Exception as e:
                messagebox.showerror("Error", f"Error opening dashboard: {e}")
        else:
            messagebox.showerror("Error", "Invalid username or password!")
    
    def forgot(self):
        """Handle forgot password click"""
        messagebox.showinfo("Forgot Password", 
                           "Password reset link would be sent to your email.\n\n"
                           "(This is a demo feature)")
    
    def signup(self):
        """Handle sign up click"""
        messagebox.showinfo("Sign Up", 
                           "Sign up form would open here.\n\n"
                           "(This is a demo feature)")
    
    def run(self):
        """Run the application"""
        self.root.mainloop()


# For testing standalone
if __name__ == "__main__":
    app = LoginWindow()
    app.run()