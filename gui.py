import customtkinter as ctk

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
topFrame.grid_columnconfigure(0, weight=5)
topFrame.grid_columnconfigure(1, weight=1)
topFrame.grid_columnconfigure(2, weight=1)
topFrame.grid_rowconfigure(0, weight=1)


titleLabel = ctk.CTkLabel(topFrame,text="examurai",font=("Helvetica",30))
titleLabel.grid(row=0,column=0, sticky="nw", padx=15, pady=15)

searchPageButton = ctk.CTkButton(topFrame, text="Search Questions", font=("Helvetica", 16), fg_color="#A3A3A3", text_color="#101010")
searchPageButton.grid(row=0, column=1, sticky="nsew", padx=15, pady=15)

addPageButton = ctk.CTkButton(topFrame, text="Add Questions", font=("Helvetica", 16), fg_color="#515151", hover_color="#282828")
addPageButton.grid(row=0, column=2, sticky="nsew", padx=15, pady=15)

# Left bar frame

leftFrame = ctk.CTkFrame(app,border_width=4)
leftFrame.grid(row=1, column=0, sticky="nsew",padx=5, pady=5) 
leftFrame.grid_columnconfigure(0, weight=1)

searchLabel = ctk.CTkLabel(leftFrame,text="Search Questions",font=("Helvetica",20))
searchLabel.grid(row=0,column=0, sticky="nsew", padx=30, pady=30)

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
