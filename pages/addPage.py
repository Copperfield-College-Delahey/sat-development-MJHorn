import customtkinter as ctk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageGrab
import os
import shutil
from questions import *

class AddPage(ctk.CTkFrame):
    def __init__(self, parent, question_manager, controller=None):
        super().__init__(parent)
        self.question_manager = question_manager
        self.image_path = None  # Store image file path

        def save_question():
            id = self.question_manager.qetNewID()
            text = textInput.get()
            tags = tagInput.get().split(",")
            source = sourceInput.get()
            new_question = Question(id, text, tags, source)
            self.question_manager.add_question(new_question)
            # Save the image using the question ID
            if self.pasted_or_uploaded_image:  # Assume this is a PIL Image object
                os.makedirs("questionFiles", exist_ok=True)
                image_path = f"questionFiles/{id}.png"
                self.pasted_or_uploaded_image.save(image_path)
            messagebox.showinfo("Saved", "Question saved successfully!")
            self.clear_form()

        def paste_image():
            image = ImageGrab.grabclipboard()
            if isinstance(image, Image.Image):
                self.pasted_or_uploaded_image = image
                show_image_preview(image)
            else:
                messagebox.showwarning("No image", "No image in clipboard.")

        def choose_image():
            file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
            if file_path:
                image = Image.open(file_path)
                self.pasted_or_uploaded_image = image
                show_image_preview(image)

        def show_image_preview(img):
            img.thumbnail((200, 200))
            tk_img = ImageTk.PhotoImage(img)
            imageLabel.configure(image=tk_img)
            imageLabel.image = tk_img
            imageLabel.pack(pady=(10, 0))

        def clear_form():
            textInput.delete(0, 'end')
            tagInput.delete(0, 'end')
            sourceInput.delete(0, 'end')
            imageLabel.configure(image=None)
            imageLabel.image = None
            self.image_path = None

        # Main form frame
        addQuestionFrame = ctk.CTkFrame(self)
        addQuestionFrame.pack(padx=20, pady=50)  

        heading = ctk.CTkLabel(addQuestionFrame, text="Add Question", font=("Helvetica", 24))
        heading.pack(pady=10, padx=10)

        textInput = ctk.CTkEntry(addQuestionFrame, placeholder_text="Enter question text. ", width=500)
        textInput.pack(anchor="w", pady=10, padx=10)

        tagInput = ctk.CTkEntry(addQuestionFrame, placeholder_text="Enter question tags, separated by commas. ", width=500)
        tagInput.pack(anchor="w", pady=10, padx=10)

        sourceInput = ctk.CTkEntry(addQuestionFrame, placeholder_text="Enter question source", width=500)
        sourceInput.pack(anchor="w", pady=10, padx=10)

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
        imageLabel = ctk.CTkLabel(addQuestionFrame, text="")  # Will hold image
        imageLabel.pack(pady=(5, 0))
