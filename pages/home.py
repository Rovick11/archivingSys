# pages/home.py
import tkinter as tk

class HomePage:
    def __init__(self, parent, colors):
        self.parent = parent
        self.colors = colors
        
        self.create_widgets()
    
    def create_widgets(self):
        # Welcome message
        welcome_frame = tk.Frame(self.parent, bg='white', relief='solid', bd=1)
        welcome_frame.pack(fill='x', pady=(0, 20))
        
        tk.Label(welcome_frame, 
                text="Welcome to Archiving System",
                font=('Segoe UI', 24, 'bold'),
                fg=self.colors['primary_blue'],
                bg='white').pack(pady=40)
        
        tk.Label(welcome_frame, 
                text="Select a module from the sidebar to get started",
                font=('Segoe UI', 12),
                fg=self.colors['gray'],
                bg='white').pack(pady=(0, 30))
        
        # Quick stats placeholders (no numbers)
        stats_frame = tk.Frame(self.parent, bg=self.colors['off_white'])
        stats_frame.pack(fill='x', pady=20)
        
        stat_cards = [
            ("📁 Archives", self.colors['secondary_blue']),
            ("👥 Users", self.colors['yellow']),
            ("📜 Logs", self.colors['primary_blue'])
        ]
        
        for i, (title, color) in enumerate(stat_cards):
            card = tk.Frame(stats_frame, bg='white', relief='solid', bd=1)
            card.pack(side='left', fill='both', expand=True, padx=5)
            
            tk.Label(card, text=title,
                    font=('Segoe UI', 14, 'bold'),
                    fg=color,
                    bg='white').pack(pady=20)
            
            tk.Label(card, text="Click to manage",
                    font=('Segoe UI', 10),
                    fg=self.colors['gray'],
                    bg='white').pack(pady=(0, 20))