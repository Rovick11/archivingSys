def show_view(self, view_name):
    if view_name not in self.views:
        return

    self.current_view = view_name
    title, subtitle = self.view_meta.get(view_name, self.view_meta["dashboard"])
    self.header_title_var.set(title)
    self.header_subtitle_var.set(subtitle)

    for name, frame in self.views.items():
        if name == view_name:
            frame.tkraise()

    for name, button in self.nav_buttons.items():
        button.configure(style="NavActive.TButton" if name == view_name else "Nav.TButton")

    if view_name == "dashboard":
        self.summary_cards.grid()
    else:
        self.summary_cards.grid_remove()
