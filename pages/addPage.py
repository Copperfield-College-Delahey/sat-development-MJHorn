import customtkinter as ctk

class AddPage(ctk.CTkFrame):
    def __init__(self, parent, controller=None):
        super().__init__(parent)
        
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)
        self.grid_columnconfigure(0, weight=1)

        heading = ctk.CTkLabel(self, text="Add Question Page", font=("Helvetica", 24))
        heading.grid(row=0, column=0, padx=20, pady=10, sticky="n")

        # Question text entry
        self.question_entry = ctk.CTkEntry(self, placeholder_text="Enter question text", height=100, font=("Helvetica", 16))
        self.question_entry.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

        # Tags entry
        self.tags_entry = ctk.CTkEntry(self, placeholder_text="Enter tags (comma-separated)", font=("Helvetica", 16))
        self.tags_entry.grid(row=2, column=0, padx=20, pady=10, sticky="ew")

        # Source entry
        self.source_entry = ctk.CTkEntry(self, placeholder_text="Enter source", font=("Helvetica", 16))
        self.source_entry.grid(row=3, column=0, padx=20, pady=10, sticky="ew")

        # Submit button
        submit_button = ctk.CTkButton(self, text="Submit Question", font=("Helvetica", 16), command=self.submit_question, fg_color="#515151", hover_color="#282828",)
        submit_button.grid(row=4, column=0, padx=20, pady=20, sticky="ew")

        # Feedback label
        self.feedback_label = ctk.CTkLabel(self, text="", font=("Helvetica", 14), text_color="green")
        self.feedback_label.grid(row=5, column=0, padx=20, pady=5, sticky="n")

    def submit_question(self):
        question_text = self.question_entry.get("1.0", "end").strip()
        tags = [tag.strip() for tag in self.tags_entry.get().split(",") if tag.strip()]
        source = self.source_entry.get().strip()

        if question_text and tags and source:
            # Temporary print — replace with saving to file/db/list
            print("New Question:")
            print("Text:", question_text)
            print("Tags:", tags)
            print("Source:", source)

            self.feedback_label.configure(text="Question submitted!", text_color="green")
            self.question_entry.delete("1.0", "end")
            self.tags_entry.delete(0, "end")
            self.source_entry.delete(0, "end")
        else:
            self.feedback_label.configure(text="Please fill in all fields.", text_color="red")
