import customtkinter as ctk
from CTkTable import CTkTable

# === Monkey Patch Begins ===

_original_init = CTkTable.__init__

def patched_init(self, *args, column_widths=None, **kwargs):
    _original_init(self, *args, **kwargs)
    if column_widths:
        for i, width in enumerate(column_widths):
            self.grid_columnconfigure(i, minsize=width)

CTkTable.__init__ = patched_init

# === GUI App ===

def main():
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")

    root = ctk.CTk()
    root.title("CTkTable Column Width Test")
    root.geometry("700x300")

    sample_data = [
        ["ID", "Name", "Role", "Notes"],
        ["1", "Alice", "Engineer", "Works on frontend"],
        ["2", "Bob", "Designer", "Focuses on UX"],
        ["3", "Charlie", "Product", "Coordinates releases"]
    ]

    table = CTkTable(
        master=root,
        row=len(sample_data),
        column=len(sample_data[0]),
        values=sample_data,
        header_color="#3e3e3e",
        column_widths=[50, 150, 100, 300]
    )
    table.pack(padx=20, pady=20, expand=True, fill="both")

    root.mainloop()

if __name__ == "__main__":
    main()
