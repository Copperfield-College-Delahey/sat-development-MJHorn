import customtkinter as ctk
from CTkTable import CTkTable
from CTkTableRowSelector import *
from PIL import Image, ImageOps

class SearchPage(ctk.CTkFrame):

    def update_table(self):
        print("Updating table")
        questions = self.question_manager.get_all()
        questions.sort(key=lambda q: q.questionId)  # Sort by questionId
        new_values = [["Question ID", "Question Text", "Tags", "Source"]]  # header
        for q in questions:
            formatted_tags = ", ".join(q.tags)
            new_values.append([q.questionId, q.question_text,formatted_tags, q.source])
        self.table.update_values(new_values)
                
    def poll_selected_row(self):
        self.current = list(self.row_selector.selected_rows)
        if len(self.current) > 0:
            self.current = self.current[0]

            if self.current != self.last_selected_row:
                self.last_selected_row = self.current
                self.row_clicked(self.current)
        self.after(20, self.poll_selected_row)

    def row_clicked(self, index):
        print("Row clicked!")
        questionId = self.table.values[self.current][0]
        questions = self.question_manager.get_all()
        selectedQuestion = None
        for question in questions:
            if question.questionId == questionId:
                selectedQuestion = question
                break
        if selectedQuestion is not None:
            
            image = Image.open(f"./questionFiles/{selectedQuestion.questionId}.png")
            aspect_ratio = image.width / image.height

            desiredWidth, desiredHeight = 500, 350

            # AI assistance with padding image to maintain constant size regardless of aspect ratio    
            # Resize and pad to fit the fixed area
            image = ImageOps.contain(image, (desiredWidth, desiredHeight))
            padded = Image.new("RGB", (desiredWidth, desiredHeight), (255, 255, 255))
            offset = ((desiredWidth - image.width) // 2, (desiredHeight - image.height) // 2)
            padded.paste(image, offset)

            self.questionImage = ctk.CTkImage(light_image=padded, size=(desiredWidth, desiredHeight))
            self.imageLabel.configure(image=self.questionImage)

    def search(self):
        print("Searching")
        tagsString = self.searchEntry.get()
        tagList = tagsString.split(",")

        searchType = self.searchType.get()

        questions = self.question_manager.search(tagList,searchType)
        questions.sort(key=lambda q: q.questionId)  # Sort by questionId

        new_values = [["Question ID", "Question Text", "Tags", "Source"]]  # header
        for q in questions:
            formatted_tags = ", ".join(q.tags)
            new_values.append([q.questionId, q.question_text,formatted_tags, q.source])
        self.table.update_values(new_values)
        self.last_selected_row = None

    def delete(self):
        selectedQ = self.table.values[self.current]
        print("Deleting",selectedQ[0])
        
        questions = self.question_manager.get_all()
        for question in questions:
            print("Comparing: ", question.question_text, selectedQ[0])
            if question.questionId == selectedQ[0]:
                self.question_manager.delete_question(question)
                self.question_manager.save_to_xml("questions.xml")
                self.update_table()
                self.last_selected_row = None
                break

    def edit(self):
        selectedQ = self.table.values[self.current]
        print("Editing", selectedQ[0])
        questions = self.question_manager.get_all()
        for question in questions:
            if question.questionId == selectedQ[0]:
                # Pass the question to AddPage for editing
                add_page = self.frames["AddPage"]  # Get AddPage instance
                add_page.prefill_fields(question)
                add_page.editing_question_id = question.questionId
                self.controller("AddPage")
                break


    def __init__(self, parent, question_manager, controller=None, frames=None):
        super().__init__(parent)
        self.question_manager = question_manager  # shared instance
        self.controller = controller 
        self.frames = frames

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=4)
        self.grid_rowconfigure(0, weight=1)

        # Left Frame
        leftFrame = ctk.CTkFrame(self, border_width=4)
        leftFrame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        leftFrame.grid_rowconfigure(0, weight=0)
        leftFrame.grid_rowconfigure(1, weight=1)
        leftFrame.grid_rowconfigure(2, weight=3)
        leftFrame.grid_columnconfigure(0, weight=1)
        leftFrame.grid_columnconfigure(1, weight=1)

        searchLabel = ctk.CTkLabel(leftFrame, text="Search Questions", font=("Helvetica", 20))
        searchLabel.grid(row=0, column=0, sticky="nw", padx=15, pady=(10, 5))

        searchControlsFrame = ctk.CTkFrame(leftFrame, fg_color="white")
        searchControlsFrame.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=10, pady=(0, 10))

        searchControlsFrame.grid_columnconfigure(0, weight=3)
        searchControlsFrame.grid_columnconfigure(1, weight=1)
        searchControlsFrame.grid_columnconfigure(3, weight=0, minsize=130)

        self.searchEntry = ctk.CTkEntry(searchControlsFrame, placeholder_text="Search by question or tag", font=("Helvetica", 16), height=40)
        self.searchEntry.grid(row=0, column=0, rowspan=2, sticky="nsew", padx=(5, 0), pady=(5, 0))

        # Radio buttons for search type (AND or OR for multiple tags entered)
        self.searchType = ctk.StringVar(value="AND")
        radioAnd = ctk.CTkRadioButton(searchControlsFrame, text="AND", variable=self.searchType, value="AND")
        radioAnd.grid(row=0, column=1, sticky="w", padx=5, pady=(5, 0))
        radioOr = ctk.CTkRadioButton(searchControlsFrame, text="OR", variable=self.searchType, value="OR")
        radioOr.grid(row=1, column=1, sticky="w", padx=5, pady=(0, 5))

        excludeEntry = ctk.CTkEntry(searchControlsFrame, placeholder_text="Exclude tags", font=("Helvetica", 16), height=40)
        excludeEntry.grid(row=2, column=0, sticky="nsew", padx=(5, 0), pady=(5, 5))

        searchButton = ctk.CTkButton(searchControlsFrame, text="Search", command=self.search, font=("Helvetica", 16), fg_color="#515151", hover_color="#282828", cursor="hand2", width=120)
        searchButton.grid(row=0, column=3, rowspan=3, sticky="nsew", padx=10, pady=10)

        # Get all questions and arrange into arrays
        questions = self.question_manager.get_all()
        print("Got questions")
        # Scrollable area for the table
        scrollFrame = ctk.CTkScrollableFrame(leftFrame)
        scrollFrame.grid(row=2, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)

        self.table_values = [["Question ID", "Question Text", "Tags", "Source"]]
        self.table = CTkTable(scrollFrame, row=25, column=4,values=self.table_values, header_color="#515151")
        self.table.pack()
        self.update_table()  # Populate initially

        # Add the row selector to the table
        self.row_selector = CTkTableRowSelector(self.table)
        self.last_selected_row = None
        self.poll_selected_row()

        # Delete question button
        deleteButton = ctk.CTkButton(leftFrame, text="Delete question",command=self.delete, font=("Helvetica", 16), fg_color="#515151", hover_color="#282828", cursor="hand2", width=100)
        deleteButton.grid(row=3, column=0, sticky="nsew", padx=10, pady=10)

        # Edit question button
        editButton = ctk.CTkButton(leftFrame, text="Edit question",command=self.edit, font=("Helvetica", 16), fg_color="#515151", hover_color="#282828", cursor="hand2", width=100)
        editButton.grid(row=3, column=1, sticky="nsew", padx=10, pady=10)

        # Right Frame
        rightFrame = ctk.CTkFrame(self, border_width=4)
        rightFrame.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
        rightFrame.grid_columnconfigure(0, weight=1)
        rightFrame.grid_rowconfigure(0, weight=1)

        self.imageLabel = ctk.CTkLabel(rightFrame, text="", width=500, height=350)  # text="" hides text
        self.imageLabel.grid(row=0, column=0)