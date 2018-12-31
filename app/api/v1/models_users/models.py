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

    def find(self, email):
        for item in user_rec:
            if item['email'] == email:
                return item['password']
        return False

    def authenticate(self, email, password):
        response = self.find(email)
        if response:
            if response == password:
                return True
            else:
                return False
        return Response
