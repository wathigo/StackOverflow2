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
        "answer": answer
        }
        answer_rec.append(data)
        return answer_rec
