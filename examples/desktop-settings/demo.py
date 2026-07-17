"""Anonymous Tkinter settings-panel example."""

from __future__ import annotations

import tkinter as tk
from tkinter import ttk


def main() -> None:
    root = tk.Tk()
    root.title("Quiet Settings — Synthetic Example")
    root.geometry("1024x720")
    root.minsize(760, 560)

    style = ttk.Style(root)
    style.configure("Title.TLabel", font=("Segoe UI", 22, "bold"))
    style.configure("Section.TLabel", font=("Segoe UI", 12, "bold"))

    shell = ttk.Frame(root, padding=28)
    shell.pack(fill="both", expand=True)
    shell.columnconfigure(1, weight=1)
    shell.rowconfigure(0, weight=1)

    navigation = ttk.Frame(shell, padding=(0, 6, 28, 0))
    navigation.grid(row=0, column=0, sticky="ns")
    ttk.Label(navigation, text="SETTINGS", style="Section.TLabel").pack(anchor="w", pady=(0, 18))
    for label in ("General", "Appearance", "Notifications", "Privacy"):
        ttk.Button(navigation, text=label, width=18).pack(anchor="w", pady=4)

    form = ttk.Frame(shell, padding=28)
    form.grid(row=0, column=1, sticky="nsew")
    form.columnconfigure(0, weight=1)

    ttk.Label(form, text="General preferences", style="Title.TLabel").grid(row=0, column=0, sticky="w")
    ttk.Label(form, text="Synthetic example — no account or device data is collected.").grid(
        row=1, column=0, sticky="w", pady=(6, 28)
    )

    ttk.Label(form, text="Workspace name", style="Section.TLabel").grid(row=2, column=0, sticky="w")
    workspace = ttk.Entry(form)
    workspace.insert(0, "Example workspace")
    workspace.grid(row=3, column=0, sticky="ew", pady=(8, 22))

    compact = tk.BooleanVar(value=True)
    sounds = tk.BooleanVar(value=False)
    ttk.Checkbutton(form, text="Use compact navigation", variable=compact).grid(row=4, column=0, sticky="w", pady=6)
    ttk.Checkbutton(form, text="Play completion sounds", variable=sounds).grid(row=5, column=0, sticky="w", pady=6)

    status_var = tk.StringVar(value="No unsaved changes")

    def save() -> None:
        status_var.set("Saved locally for this demo session")

    footer = ttk.Frame(form)
    footer.grid(row=6, column=0, sticky="ew", pady=(34, 0))
    footer.columnconfigure(0, weight=1)
    ttk.Label(footer, textvariable=status_var).grid(row=0, column=0, sticky="w")
    save_button = ttk.Button(footer, text="Save changes", command=save)
    save_button.grid(row=0, column=1, sticky="e")

    root.mainloop()


if __name__ == "__main__":
    main()
