import tkinter as tk


def _clear_placeholder(self, event):
    widget = event.widget
    if widget.get() == "Search document name or ID":
        widget.delete(0, tk.END)
