import customtkinter as ctk
from CTkTable import CTkTable

class SearchPage(ctk.CTkFrame):

    def update_table(self):
        print("Updating table")
        questions = self.question_manager.get_all()
        new_values = [["Question Text", "Tags", "Source"]]  # header
        for q in questions:
            new_values.append([q.question_text,q.tags, q.source])
        self.table.update_values(new_values)
        
    def __init__(self, parent, question_manager, controller=None):
        super().__init__(parent)

        self.question_manager = question_manager  # shared instance

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

        searchLabel = ctk.CTkLabel(leftFrame, text="Search Questions", font=("Helvetica", 20))
        searchLabel.grid(row=0, column=0, sticky="nw", padx=15, pady=(10, 5))

        searchControlsFrame = ctk.CTkFrame(leftFrame, fg_color="white")
        searchControlsFrame.grid(row=1, column=0, sticky="nsew", padx=10, pady=(0, 10))

        searchControlsFrame.grid_columnconfigure(0, weight=3)
        searchControlsFrame.grid_columnconfigure(1, weight=1)
        searchControlsFrame.grid_columnconfigure(3, weight=0, minsize=130)

        searchEntry = ctk.CTkEntry(searchControlsFrame, placeholder_text="Search by question or tag", font=("Helvetica", 16), height=40)
        searchEntry.grid(row=0, column=0, rowspan=2, sticky="nsew", padx=(5, 0), pady=(5, 0))

        radioAnd = ctk.CTkRadioButton(searchControlsFrame, text="AND")
        radioAnd.grid(row=0, column=1, sticky="w", padx=5, pady=(5, 0))

        radioOr = ctk.CTkRadioButton(searchControlsFrame, text="OR")
        radioOr.grid(row=1, column=1, sticky="w", padx=5, pady=(0, 5))

        excludeEntry = ctk.CTkEntry(searchControlsFrame, placeholder_text="Exclude tags", font=("Helvetica", 16), height=40)
        excludeEntry.grid(row=2, column=0, sticky="nsew", padx=(5, 0), pady=(5, 5))

        searchButton = ctk.CTkButton(searchControlsFrame, text="Search", font=("Helvetica", 16), fg_color="#515151", hover_color="#282828", cursor="hand2", width=120)
        searchButton.grid(row=0, column=3, rowspan=3, sticky="nsew", padx=10, pady=10)

        # Get all questions and arrange into arrays
        questions = self.question_manager.get_all()
        print("Got questions")
        qTable = [["Question Text", "Tags", "Source"]]
        for q in questions:
            qTable.append([q.question_text, ", ".join(q.tags), q.source])

        # Scrollable area for the table
        scrollFrame = ctk.CTkScrollableFrame(leftFrame)
        scrollFrame.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)

        self.table_values = [["Question Text", "Tags", "Source"]]
        self.table = CTkTable(scrollFrame, row=25, column=3,values=self.table_values, header_color="#515151")
        self.table.pack()
        self.update_table()  # Populate initially


        # Right Frame
        rightFrame = ctk.CTkFrame(self, border_width=4)
        rightFrame.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
        rightFrame.grid_columnconfigure(0, weight=1)
        rightFrame.grid_rowconfigure(0, weight=1)

        self.questionLabel = ctk.CTkLabel(rightFrame, text="[Question will display here.]", font=("Helvetica", 20), anchor="center")
        self.questionLabel.grid(row=0, column=0, padx=30, pady=30)
