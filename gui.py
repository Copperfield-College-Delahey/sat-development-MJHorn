import customtkinter as ctk
from CTkTable import *

app = ctk.CTk()
app.title("my app")
app.geometry("1000x600")

# Configure the main window grid
app.grid_columnconfigure((0, 1), weight=1)
app.grid_rowconfigure(0, weight=2)
app.grid_rowconfigure(1, weight=16)
app.grid_rowconfigure(2, weight=1)

# Top bar frame

topFrame = ctk.CTkFrame(app,border_width=4)
topFrame.grid(row=0, column=0, columnspan=2, sticky="nsew",padx=5, pady=5) 

# Set up the grid for the topFrame
topFrame.grid_columnconfigure(0, weight=1)
topFrame.grid_columnconfigure(1, weight=1)
topFrame.grid_rowconfigure(0, weight=1)


titleLabel = ctk.CTkLabel(topFrame,text="examurai",font=("Helvetica",30))
titleLabel.grid(row=0,column=0, sticky="nw", padx=15, pady=15)

menuButtonFrame = ctk.CTkFrame(topFrame)
menuButtonFrame.grid(row=0, column=1, sticky="e", padx=15, pady=15)

searchPageButton = ctk.CTkButton(menuButtonFrame, text="Search Questions", font=("Helvetica", 16), height=50, width=120,fg_color="#515151", hover_color="#282828")
searchPageButton.grid(row=0, column=0, sticky="e", padx=10, pady=0)

addPageButton = ctk.CTkButton(menuButtonFrame, text="Add Questions", font=("Helvetica", 16), height=50, width=120,fg_color="#515151", hover_color="#282828")
addPageButton.grid(row=0, column=1, sticky="e", padx=10, pady=0)

# Left bar frame
leftFrame = ctk.CTkFrame(app,border_width=4)
leftFrame.grid(row=1, column=0, sticky="nsew",padx=5, pady=5) 
leftFrame.grid_columnconfigure(0, weight=1)
leftFrame.grid_rowconfigure(0, weight=1) # row 1 in leftFrame for search entry fields
leftFrame.grid_rowconfigure(0, weight=1) # row 2 in leftFrame for search results table

searchEntryFrame = ctk.CTkFrame(leftFrame)
searchEntryFrame.grid(row=0, column=0, sticky="nsew")

searchEntryFrame.grid_columnconfigure(0, weight=1)
searchEntryFrame.grid_rowconfigure(0, weight=1)
searchEntryFrame.grid_rowconfigure(1, weight=1)
searchEntryFrame.grid_rowconfigure(2, weight=1)

searchLabel = ctk.CTkLabel(searchEntryFrame,text="Search Questions",font=("Helvetica",20))
searchLabel.grid(row=0,column=0, sticky="nsew", padx=30, pady=30)

searchEntry = ctk.CTkEntry(searchEntryFrame, placeholder_text="Search by question or tag", font=("Helvetica", 16), width=300)
searchEntry.grid(row=1, column=0, sticky="nsew", padx=30, pady=10)  

# Search results table
searchResultsFrame = ctk.CTkFrame(leftFrame)
searchResultsFrame.grid(row=1, column=0, sticky="nsew")
searchResultsFrame.grid_columnconfigure(0, weight=1)
searchResultsFrame.grid_rowconfigure(0, weight=1)
searchResultsLabel = ctk.CTkLabel(searchResultsFrame, text="Search Results", font=("Helvetica", 16))
searchResultsLabel.grid(row=0, column=0, sticky="nsew", padx=30, pady=10)

value = [[1,2,3,4,5],
         [1,2,3,4,5],
         [1,2,3,4,5],
         [1,2,3,4,5],
         [1,2,3,4,5]]

table = CTkTable(searchResultsFrame, row=5, column=5, values=value, header_color="#515151")
table.grid(row=1, column=0, sticky="nsew", padx=30, pady=10)




# Right bar frame

rightFrame = ctk.CTkFrame(app,border_width=4)
rightFrame.grid(row=1, column=1, sticky="nsew",padx=5, pady=5)
rightFrame.grid_columnconfigure(0, weight=1)

questionLabel = ctk.CTkLabel(rightFrame,text="[Question will display here.]",font=("Helvetica",20))
questionLabel.grid(row=0,column=0, sticky="nsew", padx=30, pady=30)

# Bottom bar frame

bottomFrame = ctk.CTkFrame(app,border_width=4)
bottomFrame.grid(row=2, column=0, columnspan=2, sticky="nsew",padx=5, pady=5)

bottomFrame.grid_columnconfigure(0, weight=1)
bottomFrame.grid_rowconfigure(0, weight=1)

footerLabel = ctk.CTkLabel(bottomFrame, text="MHR 2025", font=("Helvetica", 12))
footerLabel.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")



topFrame.configure(fg_color="#D1D1D1")
leftFrame.configure(fg_color="white")
rightFrame.configure(fg_color="white")
bottomFrame.configure(fg_color="#D1D1D1")

app.mainloop()
