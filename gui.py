import customtkinter as ctk

def button_callback():
    print("button pressed")

app = ctk.CTk()
app.title("my app")
app.geometry("1000x600")

# Configure the main window grid
app.grid_columnconfigure((0, 1), weight=1)
app.grid_rowconfigure(0, weight=2)
app.grid_rowconfigure(1, weight=6)
app.grid_rowconfigure(2, weight=1)

# Top bar frame

topFrame = ctk.CTkFrame(app,border_width=4)
topFrame.grid(row=0, column=0, columnspan=2, sticky="nsew",padx=5, pady=5) 

titleLabel = ctk.CTkLabel(topFrame,text="examurai",font=("Helvetica",40))
titleLabel.grid(row=0,column=0, sticky="nsew", padx=30, pady=30)

# Left bar frame

leftFrame = ctk.CTkFrame(app,border_width=4)
leftFrame.grid(row=1, column=0, sticky="nsew",padx=5, pady=5) 



# Right bar frame

rightFrame = ctk.CTkFrame(app,border_width=4)
rightFrame.grid(row=1, column=1, sticky="nsew",padx=5, pady=5)


# Bottom bar frame

bottomFrame = ctk.CTkFrame(app,border_width=4)
bottomFrame.grid(row=2, column=0, columnspan=2, sticky="nsew",padx=5, pady=5)

topFrame.configure(fg_color="#D1D1D1")
leftFrame.configure(fg_color="white")
rightFrame.configure(fg_color="white")
bottomFrame.configure(fg_color="#D1D1D1")

app.mainloop()
