class Data:

    def __init__(self, id, email, first_name, last_name, avatar):
        self.data = Details(id, email, first_name, last_name, avatar)


class Details:

    def __init__(self, id, email, first_name, last_name, avatar):
        self.id = id
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.avatar = avatar
