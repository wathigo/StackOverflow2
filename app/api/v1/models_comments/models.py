import datetime
comment_rec = []

class CommentRecord():
    def __init__(self):
        self.rec = comment_rec

    def save(self, answer_id, comment):
        data = {
        "comment_id": len(comment_rec)+1,
        "answer_id": answer_id,
        "commentedOn": datetime.datetime.now(),
        "comment": comment
        }
        self.rec.append(data)
        return self.rec
