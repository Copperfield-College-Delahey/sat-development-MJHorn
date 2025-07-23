import customtkinter as ctk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageGrab
import os
import shutil
from questions import *

class AddPage(ctk.CTkFrame):
    def show_image_preview(self, img):
        preview_img = img.copy()
        preview_img.thumbnail((200, 200))
        tk_img = ImageTk.PhotoImage(preview_img)
        self.imageLabel.configure(image=tk_img)
        self.imageLabel.image = tk_img
        self.imageLabel.pack(pady=(10, 0))

    
    def clear_form(self):
        self.textInput.delete(0, 'end')
        self.tagInput.delete(0, 'end')
        self.sourceInput.delete(0, 'end')
        self.imageLabel.configure(image=None)
        self.imageLabel.image = None
        self.image_path = None

    def __init__(self, parent, question_manager, controller=None, frames=None):
        super().__init__(parent)
        self.question_manager = question_manager
        self.image_path = None  # Store image file path
        self.frames = frames

        def save_question():
            if hasattr(self, "editing_question_id") and self.editing_question_id:
                # Edit mode
                id = self.editing_question_id
                text = self.textInput.get()
                tags = self.tagInput.get().split(",")
                source = self.sourceInput.get()
                updated_question = Question(id, text, tags, source)
                self.question_manager.update_question(updated_question)
                # Save image
                if self.pasted_or_uploaded_image:
                    os.makedirs("questionFiles", exist_ok=True)
                    image_path = f"questionFiles/{id}.png"
                    self.pasted_or_uploaded_image.save(image_path)
                messagebox.showinfo("Saved", "Question updated successfully!")
                self.question_manager.save_to_xml("questions.xml")
                self.clear_form()
                self.editing_question_id = None
            else:
                # Add mode
                id = self.question_manager.qetNewID()
                text = self.textInput.get()
                tags = self.tagInput.get().split(",")
                source = self.sourceInput.get()
                new_question = Question(id, text, tags, source)
                self.question_manager.add_question(new_question)
                # Save the image using the question ID
                if self.pasted_or_uploaded_image:  # Assume this is a PIL Image object
                    os.makedirs("questionFiles", exist_ok=True)
                    image_path = f"questionFiles/{id}.png"
                    self.pasted_or_uploaded_image.save(image_path)
                messagebox.showinfo("Saved", "Question saved successfully!")
                self.question_manager.save_to_xml("questions.xml")
                self.clear_form()

        def paste_image():
            image = ImageGrab.grabclipboard()
            if isinstance(image, Image.Image):
                self.pasted_or_uploaded_image = image
                show_image_preview(image)
            else:
                messagebox.showwarning("No image", "No image in clipboard.")

        def choose_image():
            file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif")])
            if file_path:
                image = Image.open(file_path)
                self.pasted_or_uploaded_image = image
                show_image_preview(image)


        # Main form frame
        addQuestionFrame = ctk.CTkFrame(self)
        addQuestionFrame.pack(padx=20, pady=50)  

        heading = ctk.CTkLabel(addQuestionFrame, text="Add Question", font=("Helvetica", 24))
        heading.pack(pady=10, padx=10)

        self.textInput = ctk.CTkEntry(addQuestionFrame, placeholder_text="Enter question text. ", width=500)
        self.textInput.pack(anchor="w", pady=10, padx=10)

        self.tagInput = ctk.CTkEntry(addQuestionFrame, placeholder_text="Enter question tags, separated by commas. ", width=500)
        self.tagInput.pack(anchor="w", pady=10, padx=10)

        self.sourceInput = ctk.CTkEntry(addQuestionFrame, placeholder_text="Enter question source", width=500)
        self.sourceInput.pack(anchor="w", pady=10, padx=10)

        # Image Buttons
        imageButtonFrame = ctk.CTkFrame(addQuestionFrame)
        imageButtonFrame.pack(pady=10, padx=10)

        chooseImageBtn = ctk.CTkButton(imageButtonFrame, text="Choose Image", command=choose_image)
        chooseImageBtn.pack(side="left", padx=5)

        pasteImageBtn = ctk.CTkButton(imageButtonFrame, text="Paste Image", command=paste_image)
        pasteImageBtn.pack(side="left", padx=5)

        saveButton = ctk.CTkButton(addQuestionFrame, text="Save Question", command=save_question, fg_color="#515151", hover_color="#282828", cursor="hand2")
        saveButton.pack(padx=10, pady=10)

        # Image preview
        self.imageLabel = ctk.CTkLabel(addQuestionFrame, text="")  # Will hold image
        self.imageLabel.pack(pady=(5, 0))

    def prefill_fields(self, question):
        self.textInput.delete(0, 'end')
        self.textInput.insert(0, question.question_text)
        self.tagInput.delete(0, 'end')
        self.tagInput.insert(0, ", ".join(question.tags))
        self.sourceInput.delete(0, 'end')
        self.sourceInput.insert(0, question.source)
        # Optionally load image if exists
        image_path = f"questionFiles/{question.questionId}.png"
        if os.path.exists(image_path):
            image = Image.open(image_path)
            self.pasted_or_uploaded_image = image
            self.show_image_preview(image)
        self.editing_question_id = question.questionId  # Track editing mode
