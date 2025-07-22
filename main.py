# Examurai GUI Application. Exemplar for Y12 Software Development 2025.

import customtkinter as ctk
from CTkTable import *
from pages.searchPage import SearchPage
from pages.addPage import AddPage
from questions import *

from tkinter import font as tkFont

question_manager = QuestionManager()

question_manager.load_from_xml("questions.xml")

app = ctk.CTk()
app.title("my app")
app.geometry("1000x600")

ctk.FontManager.load_font("fontFiles/Aptos-Bold.ttf")


# Configure app window grid
app.grid_columnconfigure(0, weight=1)   # Left column
app.grid_rowconfigure(0, weight=1)      # Top bar
app.grid_rowconfigure(1, weight=6)      # Main content
app.grid_rowconfigure(2, weight=1)      # Footer


# ─── Top Frame ─────────────────────────────────────────────
topFrame = ctk.CTkFrame(app, border_width=4)
topFrame.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)
topFrame.grid_columnconfigure(0, weight=1)
topFrame.grid_columnconfigure(1, weight=0)
topFrame.grid_rowconfigure(0, weight=1)

titleLabel = ctk.CTkLabel(topFrame, text="examurai", font=("Aptos", 30))
titleLabel.grid(row=0, column=0, sticky="nw", padx=15, pady=15)

menuButtonFrame = ctk.CTkFrame(topFrame)
menuButtonFrame.grid(row=0, column=1, sticky="e", padx=15, pady=15)

searchPageButton = ctk.CTkButton(menuButtonFrame, text="Filter \nQuestions", font=("Helvetica", 16), height=50, width=120, fg_color="#515151", hover_color="#282828", cursor="hand2")
searchPageButton.grid(row=0, column=0, padx=10)

addPageButton = ctk.CTkButton(menuButtonFrame, text="Add \nQuestions", font=("Helvetica", 16), height=50, width=120, fg_color="#515151", hover_color="#282828", cursor="hand2")
addPageButton.grid(row=0, column=1, padx=10)

# Container for all pages (middle row only changes; page is loaded from separate files)
pageContainer = ctk.CTkFrame(app)
pageContainer.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
pageContainer.grid_rowconfigure(0, weight=1)
pageContainer.grid_columnconfigure(0, weight=1)


# Load add question page
addPage = AddPage(pageContainer,question_manager)
addPage.grid(row=0, column=0, sticky="nsew")

# Load search page
searchPage = SearchPage(pageContainer,question_manager)
searchPage.grid(row=0, column=0, sticky="nsew")

frames = {
    "AddPage": addPage,
    "SearchPage": searchPage
}

# Page-switching function
def show_frame(page_name):
    frame = frames[page_name]
    frame.tkraise()
    frame.focus_set()
    if page_name == "SearchPage":
        frame.update_table()

# Initially show the SearchPage
show_frame("SearchPage")

#Configure buttons in header to raise the relevant pages
addPageButton.configure(command=lambda: show_frame("AddPage"))
searchPageButton.configure(command=lambda: show_frame("SearchPage"))

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
