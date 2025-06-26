class Question:
    def __init__(self, question_text, tags, source):
        self.question_text = question_text
        self.tags = tags
        self.source = source

class QuestionManager:
    def __init__(self):
        self.questions = []

    def add_question(self, question):
        self.questions.append(question)
        print("Added question: ", question.question_text)

    def get_all(self):
        return self.questions
    
    def search(self, keyword):
        return [q for q in self.questions if keyword.lower() in q.question_text.lower()]