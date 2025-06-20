class CreateNewAccount:

    def __init__(self, first_name, last_name, user_name, password, take_home):
        self.first_name = first_name
        self.last_name  = last_name
        self.user_name  = user_name
        self.password  = password
        self.take_home = take_home

    def __repr__(self):
        return ("('{}', '{}', '{}', {}, {})".format
                (self.first_name, self.last_name, self.user_name, self.password, self.take_home))










