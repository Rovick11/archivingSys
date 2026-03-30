import os
import json
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from datetime import datetime

class TTKArchivingSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("TTK Archiving System - Sangguniang Bayan")
        self.root.geometry("1100x650")
        self.root.configure(bg='#f0f0f0')

        self.current_user = None
        self.current_category = None
        self.selected_file = None
        self.documents = []

        self.base_dir = os.getcwd()
        self.data_dir = os.path.join(self.base_dir, "data")
        self.archives_dir = os.path.join(self.base_dir, "archives")

        os.makedirs(self.data_dir, exist_ok=True)
        os.makedirs(self.archives_dir, exist_ok=True)

        # Only Resolutions and Ordinances folders remain
        for folder in ['Resolutions', 'Ordinances']:
            os.makedirs(os.path.join(self.archives_dir, folder), exist_ok=True)

        self.load_data()
        self.show_login()

    def load_data(self):
        docs_file = os.path.join(self.data_dir, "documents.json")
        if os.path.exists(docs_file):
            try:
                with open(docs_file, 'r', encoding='utf-8') as f:
                    self.documents = json.load(f)
            except json.JSONDecodeError:
                messagebox.showerror("Error", "Failed to load documents.json. File may be corrupted.")
                self.documents = []
        else:
            # Add 3 sample documents per category (only Resolutions and Ordinances)
            self.documents = []
            
            # Resolutions (3 files)
            resolutions = [
                {"id": 1, "filename": "Resolution No. 2024-001.pdf", "file_type": "pdf", "category": "Resolutions", 
                 "file_path": "", "file_size": 102400, "tags": "budget, appropriation", 
                 "uploaded_at": "2024-01-15 10:30:00", "description": "Annual Budget Resolution"},
                {"id": 2, "filename": "Resolution No. 2024-025.pdf", "file_type": "pdf", "category": "Resolutions", 
                 "file_path": "", "file_size": 156800, "tags": "infrastructure, road", 
                 "uploaded_at": "2024-02-20 14:15:00", "description": "Road Concreting Resolution"},
                {"id": 3, "filename": "Resolution No. 2024-050.pdf", "file_type": "pdf", "category": "Resolutions", 
                 "file_path": "", "file_size": 89300, "tags": "health, medical", 
                 "uploaded_at": "2024-03-10 09:45:00", "description": "Health Center Funding"}
            ]
            
            # Ordinances (3 files)
            ordinances = [
                {"id": 4, "filename": "Ordinance No. 2024-005.pdf", "file_type": "pdf", "category": "Ordinances", 
                 "file_path": "", "file_size": 204800, "tags": "health, sanitation", 
                 "uploaded_at": "2024-01-05 11:20:00", "description": "Sanitation Ordinance"},
                {"id": 5, "filename": "Ordinance No. 2024-012.pdf", "file_type": "pdf", "category": "Ordinances", 
                 "file_path": "", "file_size": 178900, "tags": "peace, order", 
                 "uploaded_at": "2024-02-12 13:30:00", "description": "Curfew Ordinance"},
                {"id": 6, "filename": "Ordinance No. 2024-020.pdf", "file_type": "pdf", "category": "Ordinances", 
                 "file_path": "", "file_size": 234500, "tags": "environment, waste", 
                 "uploaded_at": "2024-03-18 15:45:00", "description": "Solid Waste Management"}
            ]
            
            self.documents.extend(resolutions)
            self.documents.extend(ordinances)
            
            self.save_data()

    def save_data(self):
        docs_file = os.path.join(self.data_dir, "documents.json")
        with open(docs_file, 'w', encoding='utf-8') as f:
            json.dump(self.documents, f, indent=2, ensure_ascii=False)

    def show_login(self):
        self.login_window = tk.Toplevel(self.root)
        self.login_window.title("Login - TTK Archiving System")
        self.login_window.geometry("380x300")
        self.login_window.configure(bg='#2c3e50')
        self.login_window.transient(self.root)
        self.login_window.grab_set()

        self.login_window.update_idletasks()
        x = (self.login_window.winfo_screenwidth() // 2) - 190
        y = (self.login_window.winfo_screenheight() // 2) - 150
        self.login_window.geometry(f"+{x}+{y}")

        frame = tk.Frame(self.login_window, bg='#34495e', padx=30, pady=30)
        frame.pack(expand=True, fill=tk.BOTH)

        tk.Label(frame, text="Archiving System", 
                font=('Arial', 16, 'bold'),
                fg='white', bg='#34495e').pack(pady=(0, 15))

        tk.Label(frame, text="Sangguniang Bayan ng Nasugbu",
                font=('Arial', 10), fg='#bdc3c7', bg='#34495e').pack(pady=(0, 25))

        tk.Label(frame, text="Username:", fg='white', bg='#34495e',
                font=('Arial', 10)).pack(anchor='w')
        self.username_entry = tk.Entry(frame, font=('Arial', 11), width=25)
        self.username_entry.pack(pady=(5, 12))

        tk.Label(frame, text="Password:", fg='white', bg='#34495e',
                font=('Arial', 10)).pack(anchor='w')
        self.password_entry = tk.Entry(frame, show="*", font=('Arial', 11), width=25)
        self.password_entry.pack(pady=(5, 20))

        tk.Button(frame, text="Login", command=self.do_login,
                 bg='#3498db', fg='white', font=('Arial', 10, 'bold'),
                 width=20, pady=5).pack()

        tk.Label(frame, text="Demo Account: employee / user123",
                font=('Arial', 8), fg='#95a5a6', bg='#34495e').pack(pady=(15, 0))

        self.username_entry.bind('<Return>', lambda e: self.password_entry.focus())
        self.password_entry.bind('<Return>', lambda e: self.do_login())

    def do_login(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        if username == "employee" and password == "user123":
            self.current_user = username
            self.login_window.destroy()
            self.create_main_ui()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password!")

    def create_main_ui(self):
        self.root.configure(bg='#f0f0f0')
        self.root.deiconify()

        # Header
        header = tk.Frame(self.root, bg='#2c3e50', height=80)
        header.pack(fill=tk.X)
        header.pack_propagate(False)

        tk.Label(header, text="Sangguniang Bayan Archiving System",
                font=('Arial', 18, 'bold'), fg='white', bg='#2c3e50').pack(side=tk.LEFT, padx=20, pady=20)

        tk.Label(header, text=f"Welcome, {self.current_user}",
                font=('Arial', 11), fg='white', bg='#2c3e50').pack(side=tk.RIGHT, padx=20)

        # Toolbar
        toolbar = tk.Frame(self.root, bg='#ecf0f1', height=40)
        toolbar.pack(fill=tk.X)
        toolbar.pack_propagate(False)

        tk.Label(toolbar, text="Search:", bg='#ecf0f1', font=('Arial', 10)).pack(side=tk.LEFT, padx=(10, 5))
        self.search_entry = tk.Entry(toolbar, width=30)
        self.search_entry.pack(side=tk.LEFT, padx=5)
        tk.Button(toolbar, text="Search", command=self.search_files,
                 bg='#3498db', fg='white').pack(side=tk.LEFT, padx=5)

        tk.Frame(toolbar, width=2, bg='#bdc3c7').pack(side=tk.LEFT, padx=15, fill=tk.Y, pady=8)

        tk.Button(toolbar, text="View", command=self.view_file,
                 bg='#2ecc71', fg='white').pack(side=tk.LEFT, padx=2)
        tk.Button(toolbar, text="Download", command=self.download_file,
                 bg='#3498db', fg='white').pack(side=tk.LEFT, padx=2)
        tk.Button(toolbar, text="Print", command=self.print_file,
                 bg='#e74c3c', fg='white').pack(side=tk.LEFT, padx=2)

        tk.Button(toolbar, text="Topology Analysis", command=self.show_topology,
                 bg='#9b59b6', fg='white').pack(side=tk.RIGHT, padx=10)

        # Main content
        main_frame = tk.Frame(self.root, bg='white')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Left panel - Categories
        left_frame = tk.Frame(main_frame, bg='#f8f9fa', width=220, relief=tk.SUNKEN, bd=1)
        left_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 5))
        left_frame.pack_propagate(False)

        tk.Label(left_frame, text="DOCUMENT CATEGORIES", 
                font=('Arial', 11, 'bold'),
                bg='#f8f9fa', fg='#2c3e50').pack(pady=(15, 10))

        tk.Frame(left_frame, height=2, bg='#3498db').pack(fill=tk.X, padx=15)

        # Only Resolutions and Ordinances categories remain
        self.categories = ['Resolutions', 'Ordinances']

        for cat in self.categories:
            btn_frame = tk.Frame(left_frame, bg='#f8f9fa')
            btn_frame.pack(fill=tk.X, padx=15, pady=5)

            btn = tk.Button(btn_frame, text=cat, command=lambda c=cat: self.open_folder(c),
                          font=('Arial', 10), bg='white', fg='#2c3e50',
                          anchor='w', padx=10, relief=tk.FLAT)
            btn.pack(side=tk.LEFT, fill=tk.X, expand=True)

            count = len([d for d in self.documents if d.get('category') == cat])
            tk.Label(btn_frame, text=f"({count})", bg='#f8f9fa', fg='#7f8c8d').pack(side=tk.RIGHT)

        # Right panel - Document list
        right_frame = tk.Frame(main_frame, bg='white')
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Path bar
        path_frame = tk.Frame(right_frame, bg='#f8f9fa', height=30)
        path_frame.pack(fill=tk.X)
        path_frame.pack_propagate(False)

        self.path_label = tk.Label(path_frame, text="Home", bg='#f8f9fa', fg='#3498db', padx=10)
        self.path_label.pack(side=tk.LEFT)

        # Treeview
        list_frame = tk.Frame(right_frame, bg='white')
        list_frame.pack(fill=tk.BOTH, expand=True, pady=5)

        columns = ('Name', 'Type', 'Date', 'Tags')
        self.tree = ttk.Treeview(list_frame, columns=columns, show='headings', height=18)

        self.tree.heading('Name', text='File Name')
        self.tree.heading('Type', text='Type')
        self.tree.heading('Date', text='Date Added')
        self.tree.heading('Tags', text='Tags')

        self.tree.column('Name', width=380)
        self.tree.column('Type', width=80)
        self.tree.column('Date', width=100)
        self.tree.column('Tags', width=200)

        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.tree.bind('<<TreeviewSelect>>', self.on_select)

        # Status bar
        status = tk.Frame(self.root, bg='#ecf0f1', height=28)
        status.pack(fill=tk.X, side=tk.BOTTOM)
        status.pack_propagate(False)

        self.status_label = tk.Label(status, text="Ready", bg='#ecf0f1', anchor='w', padx=10)
        self.status_label.pack(side=tk.LEFT, fill=tk.X, expand=True)

        self.topology_label = tk.Label(status, text="β₀: 0 | β₁: 0", bg='#ecf0f1', fg='#7f8c8d', padx=10)
        self.topology_label.pack(side=tk.RIGHT)

    def open_folder(self, category):
        self.current_category = category
        self.path_label.config(text=f"Home > {category}")
        self.status_label.config(text=f"Opened: {category}")

        for item in self.tree.get_children():
            self.tree.delete(item)

        docs = [d for d in self.documents if d.get('category') == category]
        for doc in docs:
            self.tree.insert('', 'end', values=(
                doc['filename'], 
                doc['file_type'].upper(), 
                doc['uploaded_at'].split(' ')[0], 
                doc['tags']
            ))

        self.update_topology_stats()

    def update_topology_stats(self):
        if self.current_category:
            docs = [d for d in self.documents if d.get('category') == self.current_category]
            betti_0 = len(docs)
            betti_1 = max(0, betti_0 - 1)
            self.topology_label.config(text=f"β₀: {betti_0} | β₁: {betti_1}")

    def on_select(self, event):
        selection = self.tree.selection()
        if selection:
            item = self.tree.item(selection[0])
            self.selected_file = item['values'][0]
            self.status_label.config(text=f"Selected: {self.selected_file}")

    def search_files(self):
        query = self.search_entry.get().strip()
        if not query:
            messagebox.showwarning("Search", "Please enter a search query.")
            return

        for item in self.tree.get_children():
            self.tree.delete(item)

        results = [d for d in self.documents if query.lower() in d.get('filename', '').lower() or
                   query.lower() in d.get('tags', '').lower()]

        for doc in results:
            self.tree.insert('', 'end', values=(
                doc['filename'], 
                doc['file_type'].upper(), 
                doc['uploaded_at'].split(' ')[0], 
                doc['tags']
            ))

        self.status_label.config(text=f"Found {len(results)} results for '{query}'")
        self.path_label.config(text=f"Search: {query}")

    def view_file(self):
        if not self.selected_file:
            messagebox.showwarning("View File", "No file selected.")
            return
        messagebox.showinfo("View File", f"Viewing: {self.selected_file}\n\n(File viewer would open here)")

    def download_file(self):
        if not self.selected_file:
            messagebox.showwarning("Download File", "No file selected.")
            return
        save_path = filedialog.asksaveasfilename(defaultextension=".*", initialfile=self.selected_file)
        if save_path:
            messagebox.showinfo("Download File", f"File saved to: {save_path}")

    def print_file(self):
        if not self.selected_file:
            messagebox.showwarning("Print File", "No file selected.")
            return
        messagebox.showinfo("Print", f"Printing: {self.selected_file}")

    def show_topology(self):
        categories = {}
        for doc in self.documents:
            category = doc.get('category', 'Unknown')
            categories[category] = categories.get(category, 0) + 1

        stats = f"=== TTK Topological Analysis ===\n\n"
        stats += f"Total Documents: {len(self.documents)}\n"
        stats += f"Total Categories: {len(categories)}\n\n"
        stats += f"Betti Numbers:\n"
        stats += f"  β₀ (Connected Components): {len(categories)}\n"
        stats += f"  β₁ (Topological Holes): {len(self.documents) - len(categories)}\n\n"
        stats += f"Documents by Category:\n"
        for cat, count in categories.items():
            stats += f"  • {cat}: {count} document(s)\n"

        messagebox.showinfo("Topology Analysis", stats)

if __name__ == "__main__":
    root = tk.Tk()
    app = TTKArchivingSystem(root)
    root.mainloop()