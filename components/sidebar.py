# components/sidebar.py
import tkinter as tk

class Sidebar:
    def __init__(self, parent, colors, change_page_callback):
        self.parent = parent
        self.colors = colors
        self.change_page = change_page_callback
        self.current_page = "Home"
        self.menu_buttons = {}  # <--- DAPAT NASA UNA ITO!
        
        self.sidebar = tk.Frame(parent, bg=self.colors['primary_blue'], width=250)
        self.sidebar.pack(side='left', fill='y')
        self.sidebar.pack_propagate(False)
        
        self.create_logo()
        self.create_menu()
    
    def create_logo(self):
        logo = tk.Frame(self.sidebar, bg=self.colors['primary_blue'], height=80)
        logo.pack(fill='x', pady=20)
        logo.pack_propagate(False)
        
        tk.Label(logo, text="📁", font=('Segoe UI', 40), 
                bg=self.colors['primary_blue'], 
                fg=self.colors['yellow']).pack()
    
    def create_menu(self):
        menu = tk.Frame(self.sidebar, bg=self.colors['primary_blue'])
        menu.pack(fill='both', expand=True, pady=20)
        
        items = [
            ("🏠", "Home"),
            ("👥", "Users"),
            ("📜", "Logs")
        ]
        
        for icon, text in items:
            btn = tk.Button(menu, text=f"{icon}  {text}",
                          font=('Segoe UI', 11),
                          bg=self.colors['primary_blue'],
                          fg='white', bd=0, anchor='w',
                          padx=15, pady=10, cursor='hand2',
                          command=lambda t=text: self.on_menu_click(t))
            btn.pack(fill='x', padx=15, pady=2)
            
            # Store button reference
            self.menu_buttons[text] = btn
            
            # Hover effects
            btn.bind('<Enter>', lambda e, b=btn: b.configure(bg=self.colors['secondary_blue']))
            btn.bind('<Leave>', lambda e, b=btn: self.on_leave(b))
    
    def on_menu_click(self, page_name):
        """Handle menu click"""
        self.change_page(page_name)
    
    def on_leave(self, button):
        """Handle mouse leave"""
        if hasattr(self, 'current_page'):
            btn_text = button.cget('text').split()[1]  # Get "Home" from "🏠 Home"
            if btn_text == self.current_page:
                button.configure(bg=self.colors['yellow'])
            else:
                button.configure(bg=self.colors['primary_blue'])
    
    def highlight_menu(self, page_name):
        """Highlight the active menu item"""
        self.current_page = page_name
        
        # Reset all buttons
        for btn in self.menu_buttons.values():
            btn.configure(bg=self.colors['primary_blue'])
        
        # Highlight current page
        if page_name in self.menu_buttons:
            self.menu_buttons[page_name].configure(bg=self.colors['yellow'])