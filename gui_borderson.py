# Examurai GUI Application. This is my exemplar for students in Software Development 2025. 

import customtkinter as ctk
from CTkTable import *

app = ctk.CTk()
app.title("my app")
app.geometry("1000x600")

# Configure the main window grid
app.grid_columnconfigure(0, weight=1) # left column
app.grid_columnconfigure(1, weight=2) # right column
app.grid_rowconfigure(0, weight=2) # title row
app.grid_rowconfigure(1, weight=16) # content row
app.grid_rowconfigure(2, weight=1) # footer row

# Top bar frame
topFrame = ctk.CTkFrame(app,border_width=4)
topFrame.grid(row=0, column=0, columnspan=2, sticky="nsew",padx=5, pady=5) 

# Set up the grid for the topFrame
topFrame.grid_columnconfigure(0, weight=1) # column for title
topFrame.grid_columnconfigure(1, weight=1) # column for menu buttons
topFrame.grid_rowconfigure(0, weight=1) # single row to centre elements vertically

#examurai title
titleLabel = ctk.CTkLabel(topFrame,text="examurai",font=("Helvetica",30))
titleLabel.grid(row=0,column=0, sticky="nw", padx=15, pady=15) # sticky nw aligns to the top right (north-west)

# Frame for two top menu buttons
menuButtonFrame = ctk.CTkFrame(topFrame, border_width=2)
menuButtonFrame.grid(row=0, column=1, sticky="e", padx=15, pady=15)

searchPageButton = ctk.CTkButton(menuButtonFrame, text="Search Questions", font=("Helvetica", 16), height=50, width=120,fg_color="#515151", hover_color="#282828")
searchPageButton.grid(row=0, column=0, sticky="e", padx=10, pady=0)

addPageButton = ctk.CTkButton(menuButtonFrame, text="Add Questions", font=("Helvetica", 16), height=50, width=120,fg_color="#515151", hover_color="#282828")
addPageButton.grid(row=0, column=1, sticky="e", padx=10, pady=0)

# Left main section (search) frame
leftFrame = ctk.CTkFrame(app,border_width=4)
leftFrame.grid(row=1, column=0, sticky="nsew",padx=5, pady=5) 
leftFrame.grid_columnconfigure(0, weight=1) # single column to centre elements
leftFrame.grid_rowconfigure(0, weight=1) # row 1 in leftFrame for search entry fields
leftFrame.grid_rowconfigure(0, weight=1) # row 2 in leftFrame for search results table

searchEntryFrame = ctk.CTkFrame(leftFrame, border_width=2) # Search entry frame in top half of left box for search fields
searchEntryFrame.grid(row=0, column=0, sticky="nsew")

searchEntryFrame.grid_columnconfigure(0, weight=1)
searchEntryFrame.grid_rowconfigure(0, weight=1)
searchEntryFrame.grid_rowconfigure(1, weight=1)
searchEntryFrame.grid_rowconfigure(2, weight=1)

searchLabel = ctk.CTkLabel(searchEntryFrame,text="Search Questions",font=("Helvetica",20))
searchLabel.grid(row=0,column=0, sticky="nsew", padx=10, pady=10)

searchOptionFrame = ctk.CTkFrame(searchEntryFrame, border_width=2) # Frame to combine search box and radio buttons
searchOptionFrame.grid(row=1,column=0, sticky="nsew")

searchOptionFrame.grid_columnconfigure(0, weight=2)
searchOptionFrame.grid_columnconfigure(1, weight=1)
searchOptionFrame.grid_rowconfigure(0, weight=1)
searchOptionFrame.grid_rowconfigure(1, weight=1)
searchOptionFrame.grid_rowconfigure(2, weight=1)

searchEntry = ctk.CTkEntry(searchOptionFrame, placeholder_text="Search by question or tag", font=("Helvetica", 16), width=300)
searchEntry.grid(row=0, column=0, rowspan=2,sticky="nsew", padx=30, pady=10)  

radioAnd = ctk.CTkRadioButton(searchOptionFrame, text="AND")
radioAnd.grid(row=0,column=1)

radioOr = ctk.CTkRadioButton(searchOptionFrame, text="OR")
radioOr.grid(row=1,column=1)

excludeEntry = ctk.CTkEntry(searchEntryFrame, placeholder_text="Exclude tags", font=("Helvetica", 16), width=300)
excludeEntry.grid(row=2, column=0, sticky="nsew", padx=30, pady=10)  

# Search results table
searchResultsFrame = ctk.CTkFrame(leftFrame, border_width=2)
searchResultsFrame.grid(row=1, column=0, sticky="nsew")
searchResultsFrame.grid_columnconfigure(0, weight=1)
searchResultsFrame.grid_rowconfigure(0, weight=1)
searchResultsLabel = ctk.CTkLabel(searchResultsFrame, text="Search Results", font=("Helvetica", 16))
searchResultsLabel.grid(row=0, column=0, sticky="nsew", padx=30, pady=10)

value = [[1,2,3,4],
         [1,2,3,4],
         [1,2,3,4],
         [1,2,3,4],
         [1,2,3,4]]

table = CTkTable(searchResultsFrame, row=5, column=4, values=value, header_color="#515151")
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
