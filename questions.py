import xml.etree.ElementTree as ET

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

    def delete_question(self, question):
        self.questions.remove(question)
        print("Deleted question: ", question.question_text)

    def get_all(self):
        return self.questions
    
    def search(self, keywords, mode):
        keywords_lower = [kw.lower() for kw in keywords]

        def matches(q):
            text = q.question_text.lower()
            tags = [tag.lower() for tag in q.tags]
            if mode == "AND":
                return all(
                    any(kw in text or any(kw in tag for tag in tags) for kw in [keyword])
                    for keyword in keywords_lower
                )
            else:  # "OR"
                return any(
                    kw in text or any(kw in tag for tag in tags)
                    for kw in keywords_lower
                )

        return [q for q in self.questions if matches(q)]
    
    def save_to_xml(self, filepath):
        root = ET.Element("questions")
        for q in self.questions:
            q_elem = ET.SubElement(root, "question")

            ET.SubElement(q_elem, "id").text = q.questionId
            ET.SubElement(q_elem, "question_text").text = q.question_text
            ET.SubElement(q_elem, "tags").text = ",".join(q.tags)
            ET.SubElement(q_elem, "source").text = q.source

        tree = ET.ElementTree(root)
        tree.write(filepath, encoding="utf-8", xml_declaration=True)

    def load_from_xml(self, filepath):
        try:
            tree = ET.parse(filepath)
            root = tree.getroot()
            for q_elem in root.findall("question"):
                id = q_elem.find("id").text or ""
                question_text = q_elem.find("question_text").text or ""
                tags = (q_elem.find("tags").text or "").split(",")
                source = q_elem.find("source").text or None
                self.add_question(Question(id, question_text, tags, source))
        except FileNotFoundError:
            pass  # OK on first run
        except ET.ParseError as e:
            print("Error loading XML:", e)
