class Spy:

    def __init__(self, name, salutation, age, rating):
        # Initializing the values
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None
        # Count the number of words
        self.count = 0