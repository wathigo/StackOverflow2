import datetime

question_rec = []

class QuestionRecords():
    def __init__(self):
        self.rec = question_rec

    def save(self, question, category):
        data = {
        "id": len(question_rec) + 1,
        "postedOn":datetime.datetime.now(),
        "category": category,
        "question": question
        }
        question_rec.append(data)
        return question_rec
