from tkinter import ttk


def _setup_style(self):
    style = ttk.Style()
    style.theme_use("clam")

    style.configure("App.TFrame", background="#edf1f5")
    style.configure("Sidebar.TFrame", background="#0f172a")
    style.configure("Card.TFrame", background="#ffffff", relief="flat")
    style.configure("Panel.TFrame", background="#ffffff")

    style.configure("SidebarTitle.TLabel", background="#0f172a", foreground="#ffffff", font=("Segoe UI", 18, "bold"))
    style.configure("SidebarSmall.TLabel", background="#0f172a", foreground="#94a3b8", font=("Segoe UI", 9))
    style.configure("SidebarUser.TLabel", background="#0f172a", foreground="#e2e8f0", font=("Segoe UI", 10))
    style.configure("Heading.TLabel", background="#edf1f5", foreground="#0f172a", font=("Segoe UI", 22, "bold"))
    style.configure("SubHeading.TLabel", background="#edf1f5", foreground="#64748b", font=("Segoe UI", 10))
    style.configure("CardTitle.TLabel", background="#ffffff", foreground="#64748b", font=("Segoe UI", 10))
    style.configure("CardValue.TLabel", background="#ffffff", foreground="#0f172a", font=("Segoe UI", 18, "bold"))
    style.configure("SectionTitle.TLabel", background="#ffffff", foreground="#0f172a", font=("Segoe UI", 13, "bold"))
    style.configure("SectionSub.TLabel", background="#ffffff", foreground="#64748b", font=("Segoe UI", 9))

    style.configure("Nav.TButton", font=("Segoe UI", 10), padding=(14, 12), background="#1e293b", foreground="#e2e8f0", borderwidth=0, anchor="w")
    style.map("Nav.TButton", background=[("active", "#334155")], foreground=[("active", "#ffffff")])

    style.configure("NavActive.TButton", font=("Segoe UI", 10, "bold"), padding=(14, 12), background="#2563eb", foreground="#ffffff", borderwidth=0, anchor="w")
    style.map("NavActive.TButton", background=[("active", "#1d4ed8")])

    style.configure("Primary.TButton", font=("Segoe UI", 10, "bold"), padding=(16, 10), background="#0f172a", foreground="#ffffff", borderwidth=0)
    style.map("Primary.TButton", background=[("active", "#1e293b")], foreground=[("active", "#ffffff")])

    style.configure("Blue.TButton", font=("Segoe UI", 10, "bold"), padding=(16, 10), background="#2563eb", foreground="#ffffff", borderwidth=0)
    style.map("Blue.TButton", background=[("active", "#1d4ed8")])

    style.configure("Light.TButton", font=("Segoe UI", 10), padding=(14, 10), background="#f8fafc", foreground="#0f172a", borderwidth=1, relief="solid")
    style.map("Light.TButton", background=[("active", "#e2e8f0")])

    style.configure("Danger.TButton", font=("Segoe UI", 9, "bold"), padding=(8, 5), background="#fee2e2", foreground="#b91c1c", borderwidth=0)
    style.map("Danger.TButton", background=[("active", "#fecaca")])

    style.configure("MiniDark.TButton", font=("Segoe UI", 9, "bold"), padding=(8, 5), background="#0f172a", foreground="#ffffff", borderwidth=0)
    style.map("MiniDark.TButton", background=[("active", "#1e293b")])

    style.configure("TEntry", padding=8, fieldbackground="#f8fafc", bordercolor="#cbd5e1", relief="solid")
    style.configure("TCombobox", padding=6, fieldbackground="#f8fafc", bordercolor="#cbd5e1")

    style.configure("Treeview", rowheight=34, font=("Segoe UI", 9), background="#ffffff", fieldbackground="#ffffff", foreground="#0f172a", borderwidth=0)
    style.configure("Treeview.Heading", font=("Segoe UI", 9, "bold"), background="#f8fafc", foreground="#475569", relief="flat")
    style.map("Treeview", background=[("selected", "#dbeafe")], foreground=[("selected", "#0f172a")])
