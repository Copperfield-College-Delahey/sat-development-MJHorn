# Examurai GUI Application. Exemplar for Y12 Software Development 2025.

import customtkinter as ctk
from CTkTable import *
from pages.searchPage import SearchPage

app = ctk.CTk()
app.title("my app")
app.geometry("1000x600")

# Configure app window grid
app.grid_columnconfigure(0, weight=1)   # Left column
app.grid_columnconfigure(1, weight=4)   # Right column
app.grid_rowconfigure(0, weight=1)      # Top bar
app.grid_rowconfigure(1, weight=6)      # Main content
app.grid_rowconfigure(2, weight=1)      # Footer


# Container for all pages (middle row only changes)
pageContainer = ctk.CTkFrame(app)
pageContainer.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)
pageContainer.grid_rowconfigure(0, weight=1)
pageContainer.grid_columnconfigure(0, weight=1)

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

## — Variable pages loaded from files in pages folder

searchPage = SearchPage(pageContainer)
searchPage.grid(row=0, column=0, sticky="nsew")
searchPage.tkraise()  # show it initially

# ─── Bottom Frame ──────────────────────────────────────────
bottomFrame = ctk.CTkFrame(app, border_width=4)
bottomFrame.grid(row=2, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)
bottomFrame.grid_columnconfigure(0, weight=1)
bottomFrame.grid_rowconfigure(0, weight=1)

footerLabel = ctk.CTkLabel(bottomFrame, text="MHR 2025", font=("Helvetica", 12))
footerLabel.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

# ─── Frame Colouring ──────────────────────────────────────
topFrame.configure(fg_color="#D1D1D1")
bottomFrame.configure(fg_color="#D1D1D1")

app.mainloop()
