# Examurai GUI Application. Responsive and clean.

import customtkinter as ctk
from CTkTable import *

app = ctk.CTk()
app.title("my app")
app.geometry("1000x600")

# Configure app window grid
app.grid_columnconfigure(0, weight=1)   # Left column
app.grid_columnconfigure(1, weight=4)   # Right column
app.grid_rowconfigure(0, weight=1)      # Top bar
app.grid_rowconfigure(1, weight=6)      # Main content
app.grid_rowconfigure(2, weight=1)      # Footer

# ─── Top Frame ─────────────────────────────────────────────
topFrame = ctk.CTkFrame(app, border_width=4)
topFrame.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)
topFrame.grid_columnconfigure(0, weight=1)
topFrame.grid_columnconfigure(1, weight=0)
topFrame.grid_rowconfigure(0, weight=1)

titleLabel = ctk.CTkLabel(topFrame, text="examurai", font=("Helvetica", 30))
titleLabel.grid(row=0, column=0, sticky="nw", padx=15, pady=15)

menuButtonFrame = ctk.CTkFrame(topFrame)
menuButtonFrame.grid(row=0, column=1, sticky="e", padx=15, pady=15)

searchPageButton = ctk.CTkButton(menuButtonFrame, text="Filter Questions", font=("Helvetica", 16), height=50, width=120, fg_color="#515151", hover_color="#282828", cursor="hand2")
searchPageButton.grid(row=0, column=0, padx=10)

addPageButton = ctk.CTkButton(menuButtonFrame, text="Add Questions", font=("Helvetica", 16), height=50, width=120, fg_color="#515151", hover_color="#282828", cursor="hand2")
addPageButton.grid(row=0, column=1, padx=10)

# ─── Left Frame ────────────────────────────────────────────
leftFrame = ctk.CTkFrame(app, border_width=4)
leftFrame.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
leftFrame.grid_rowconfigure(0, weight=0)
leftFrame.grid_rowconfigure(1, weight=1)
leftFrame.grid_rowconfigure(2, weight=3)
leftFrame.grid_columnconfigure(0, weight=1)

searchLabel = ctk.CTkLabel(leftFrame, text="Search Questions", font=("Helvetica", 20))
searchLabel.grid(row=0, column=0, sticky="nw", padx=15, pady=(10, 5))

searchControlsFrame = ctk.CTkFrame(leftFrame)
searchControlsFrame.grid(row=1, column=0, sticky="nsew", padx=10, pady=(0, 10))

searchControlsFrame.grid_columnconfigure(0, weight=3)  # entry + exclude
searchControlsFrame.grid_columnconfigure(1, weight=1)  # radio buttons
searchControlsFrame.grid_columnconfigure(2, weight=0)
searchControlsFrame.grid_columnconfigure(3, weight=0, minsize=130)
searchControlsFrame.grid_rowconfigure(0, weight=1)
searchControlsFrame.grid_rowconfigure(1, weight=1)
searchControlsFrame.grid_rowconfigure(2, weight=1)

searchEntry = ctk.CTkEntry(searchControlsFrame, placeholder_text="Search by question or tag", font=("Helvetica", 16), height=40)
searchEntry.grid(row=0, column=0, rowspan=2, sticky="nsew", padx=(5, 0), pady=(5, 0))

radioAnd = ctk.CTkRadioButton(searchControlsFrame, text="AND")
radioAnd.grid(row=0, column=1, sticky="w", padx=5, pady=(5, 0))

radioOr = ctk.CTkRadioButton(searchControlsFrame, text="OR")
radioOr.grid(row=1, column=1, sticky="w", padx=5, pady=(0, 5))

excludeEntry = ctk.CTkEntry(searchControlsFrame, placeholder_text="Exclude tags", font=("Helvetica", 16), height=40)
excludeEntry.grid(row=2, column=0, sticky="nsew", padx=(5, 0), pady=(5, 5))

searchButton = ctk.CTkButton(searchControlsFrame, text="Search", font=("Helvetica", 16), fg_color="#515151", hover_color="#282828", cursor="hand2", width=120)
searchButton.grid(row=0, column=3, rowspan=3, sticky="nsew", padx=10, pady=10)

table = CTkTable(leftFrame, row=8, column=3, header_color="#515151")
table.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)

# ─── Right Frame ───────────────────────────────────────────
rightFrame = ctk.CTkFrame(app, border_width=4)
rightFrame.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)
rightFrame.grid_columnconfigure(0, weight=1)
rightFrame.grid_rowconfigure(0, weight=1)

questionLabel = ctk.CTkLabel(rightFrame, text="[Question will display here.]", font=("Helvetica", 20), anchor="center")
questionLabel.grid(row=0, column=0, sticky="nsew", padx=30, pady=30)

# ─── Bottom Frame ──────────────────────────────────────────
bottomFrame = ctk.CTkFrame(app, border_width=4)
bottomFrame.grid(row=2, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)
bottomFrame.grid_columnconfigure(0, weight=1)
bottomFrame.grid_rowconfigure(0, weight=1)

footerLabel = ctk.CTkLabel(bottomFrame, text="MHR 2025", font=("Helvetica", 12))
footerLabel.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

# ─── Frame Colouring ──────────────────────────────────────
topFrame.configure(fg_color="#D1D1D1")
leftFrame.configure(fg_color="white")
rightFrame.configure(fg_color="white")
bottomFrame.configure(fg_color="#D1D1D1")
searchControlsFrame.configure(fg_color="white")

app.mainloop()
