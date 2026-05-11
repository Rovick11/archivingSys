# pages/profile.py
import tkinter as tk
from tkinter import messagebox

class ProfilePage:
    def __init__(self, parent, colors):
        self.parent = parent
        self.colors = colors
        
        self.create_widgets()
    
    def create_widgets(self):
        # Profile card
        profile_card = tk.Frame(self.parent, bg='white', relief='solid', bd=1)
        profile_card.pack(fill='x', pady=(0, 20))
        
        # Profile header
        tk.Label(profile_card, 
                text="My Profile",
                font=('Segoe UI', 18, 'bold'),
                fg=self.colors['primary_blue'],
                bg='white').pack(anchor='w', padx=30, pady=20)
        
        # Profile info
        info_frame = tk.Frame(profile_card, bg='white')
        info_frame.pack(fill='x', padx=30, pady=(0, 30))
        
        # Avatar
        avatar = tk.Label(info_frame, 
                         text="👤",
                         font=('Segoe UI', 48),
                         bg='white',
                         fg=self.colors['secondary_blue'])
        avatar.pack(side='left', padx=(0, 30))
        
        # Details
        details = tk.Frame(info_frame, bg='white')
        details.pack(side='left', fill='both', expand=True)
        
        fields = [
            ("Username:", "superadmin"),
            ("Email:", "admin@archiving.com"),
            ("Role:", "Super Administrator"),
            ("Last Login:", "Not available")
        ]
        
        for i, (label, value) in enumerate(fields):
            row = tk.Frame(details, bg='white')
            row.pack(fill='x', pady=5)
            
            tk.Label(row, 
                    text=label,
                    font=('Segoe UI', 11, 'bold'),
                    width=15,
                    anchor='w',
                    bg='white').pack(side='left')
            
            tk.Label(row, 
                    text=value,
                    font=('Segoe UI', 11),
                    anchor='w',
                    bg='white').pack(side='left', padx=10)
        
        # Edit button
        tk.Button(profile_card, 
                 text="Edit Profile",
                 bg=self.colors['secondary_blue'],
                 fg='white',
                 font=('Segoe UI', 11),
                 bd=0,
                 padx=30,
                 pady=8,
                 cursor='hand2',
                 command=lambda: messagebox.showinfo("Edit Profile", "Edit profile form will appear here")).pack(anchor='e', padx=30, pady=(0, 20))