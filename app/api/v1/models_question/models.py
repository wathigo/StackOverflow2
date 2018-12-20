import datetime

question_rec = []

class QuestionRecords():
    def __init__(self):
        self.rec = question_rec

    def save(self, category, question):
        data = {
        "id": len(question_rec) + 1,
        "postedOn":datetime.datetime.now(),
        "category": category,
        "question": question
        }
        question_rec.append(data)
        return question_rec

    def get_records(self):
        return question_rec

    def find(self, id):
        result = False
        for question in question_rec:
            if question['id'] == id:
                return question
        return result

    def empty_records(self):
        del question_rec[:]
        return question_rec

    def del_record(self, id):
        rec = self.find(id)
        if rec:
            question_rec.remove(rec)
            return question_rec
        else:
            return rec

    def replace(self, id, category, question):
        item = self.find(id)
        if item:
            i = 0
            while i < len(question_rec):
                for record in question_rec:
                    if record == item:
                        record['category'] = category
                        record['question'] = question
                        return question_rec
        return item
