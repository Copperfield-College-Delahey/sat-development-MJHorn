import customtkinter as ctk

class App:
    def __init__(self):
        # Create main window
        self.window = ctk.CTk()
        self.window.title("Screen Switching Example")
        self.window.geometry("400x300")
        
        # Create frames for different screens
        self.screen1 = ctk.CTkFrame(self.window)
        self.screen2 = ctk.CTkFrame(self.window)
        
        # Setup Screen 1
        self.setup_screen1()
        
        # Setup Screen 2
        self.setup_screen2()
        
        # Show first screen initially
        self.show_screen1()
    
    def setup_screen1(self):
        """Setup the first screen with its widgets"""
        # Title
        title = ctk.CTkLabel(self.screen1, text="Welcome to Screen 1", 
                           font=ctk.CTkFont(size=20, weight="bold"))
        title.pack(pady=30)
        
        # Some content
        content = ctk.CTkLabel(self.screen1, text="This is the first screen.\nClick the button below to go to Screen 2.")
        content.pack(pady=20)
        
        # Button to switch to screen 2
        switch_btn = ctk.CTkButton(self.screen1, text="Go to Screen 2", 
                                 command=self.show_screen2)
        switch_btn.pack(pady=20)
    
    def setup_screen2(self):
        """Setup the second screen with its widgets"""
        # Title
        title = ctk.CTkLabel(self.screen2, text="You're on Screen 2!", 
                           font=ctk.CTkFont(size=20, weight="bold"))
        title.pack(pady=30)
        
        # Some content
        content = ctk.CTkLabel(self.screen2, text="This is the second screen.\nYou can go back to Screen 1.")
        content.pack(pady=20)
        
        # Button to switch back to screen 1
        back_btn = ctk.CTkButton(self.screen2, text="Back to Screen 1", 
                               command=self.show_screen1)
        back_btn.pack(pady=20)
    
    def show_screen1(self):
        """Hide all screens and show screen 1"""
        self.screen2.pack_forget()  # Hide screen 2
        self.screen1.pack(fill="both", expand=True, padx=20, pady=20)  # Show screen 1
    
    def show_screen2(self):
        """Hide all screens and show screen 2"""
        self.screen1.pack_forget()  # Hide screen 1
        self.screen2.pack(fill="both", expand=True, padx=20, pady=20)  # Show screen 2
    
    def run(self):
        """Start the application"""
        self.window.mainloop()

# Create and run the app
if __name__ == "__main__":
    app = App()
    app.run()