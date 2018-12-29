import datetime
answer_rec = []

class AnswerRecord():
    def __init__(self):
        self.rec  = answer_rec

    def save(self, question_id, answer):
        data = {
        "answer_id": len(answer_rec) + 1,
        "question_id": question_id,
        "answeredOn": datetime.datetime.now(),
        "accepted" : False,
        "answer": answer
        }
        answer_rec.append(data)
        return answer_rec

    def find(self, answer_id):
        for item in answer_rec:
            if item['answer_id'] == answer_id:
                return item
    def get_answer(self, id):
        item = self.find(id)
        if item is not None:
            return item
        return False
