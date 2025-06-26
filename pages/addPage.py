import customtkinter as ctk
from questions import *

class AddPage(ctk.CTkFrame):
    def __init__(self, parent, question_manager,controller=None):
        super().__init__(parent)

        self.question_manager = question_manager  # shared instance

        def save_question():
            text = textInput.get()
            tags = tagInput.get().split(",")
            source = sourceInput.get()
            new_question = Question(text, tags, source)
            self.question_manager.add_question(new_question)
        
        addQuestionFrame = ctk.CTkFrame(self)
        addQuestionFrame.pack(padx=20, pady=50)  

        # Heading label
        heading = ctk.CTkLabel(addQuestionFrame, text="Add Question", font=("Helvetica", 24))
        heading.pack(pady=10, padx=10)

        textInput = ctk.CTkEntry(addQuestionFrame, placeholder_text="Enter question text. ", width=500)
        textInput.pack(anchor="w",pady=10, padx=10)

        tagInput = ctk.CTkEntry(addQuestionFrame, placeholder_text="Enter question tags, separated by commas. ", width=500)
        tagInput.pack( anchor="w",pady=10, padx=10)

        sourceInput = ctk.CTkEntry(addQuestionFrame, placeholder_text="Enter question source", width=500)
        sourceInput.pack( anchor="w",pady=10, padx=10)

        saveButton = ctk.CTkButton(addQuestionFrame,text="Save Question",command=save_question, fg_color="#515151", hover_color="#282828", cursor="hand2")
        saveButton.pack(padx=10, pady=10)

        
