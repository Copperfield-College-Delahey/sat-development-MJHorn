import customtkinter as ctk

class AddPage(ctk.CTkFrame):
    def __init__(self, parent, controller=None):
        super().__init__(parent)
        
        # Configure grid if you want to expand later
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Placeholder label
        heading = ctk.CTkLabel(self, text="Add Questions Page", font=("Helvetica", 24))
        heading.grid(row=0, column=0, padx=20, pady=20, sticky="n")