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

    def find(self, answer_id):
        items = []
        for item in self.rec:
            if item['answer_id'] == answer_id:
                items.append(item)
        return items

    def get_item(self, answer_id):
        res = self.find(answer_id)
        if res is not None:
            return res
        else:
            return False
