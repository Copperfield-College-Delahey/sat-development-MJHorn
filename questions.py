class Question:
    def __init__(self, questionId, question_text, tags, source):
        self.questionId = questionId
        self.questionImage = "questionFiles/"+questionId+".png"
        self.question_text = question_text
        self.tags = tags
        self.source = source

class QuestionManager:
    def __init__(self):
        self.questions = []

    def qetNewID(self):
        existing_ids = [q.questionId for q in self.questions]
        max_num = 0
        for qid in existing_ids:
            if qid.startswith("q") and qid[1:].isdigit():
                max_num = max(max_num, int(qid[1:]))
        return f"q{max_num + 1:05d}"

    def add_question(self, question):
        self.questions.append(question)
        print("Added question: ", question.question_text)

    def get_all(self):
        return self.questions
    
    def search(self, keyword):
        return [q for q in self.questions if keyword.lower() in q.question_text.lower()]