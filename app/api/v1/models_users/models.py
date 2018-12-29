import datetime
user_rec = []

class UserRecords():
    def __init__(self):
        self.rec = user_rec

    def save(self, email, password):
        data = {
        "userId": len(user_rec)+1,
        "createdOn": datetime.datetime.now(),
        "userName": email.split("@")[0],
        "email": email,
        "password": password
        }
        self.rec.append(data)
        return self.rec
