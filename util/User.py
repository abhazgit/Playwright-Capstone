class User:
    def __init__(self, id, name, email, username):
        self.id = id
        self.name = name
        self.email = email
        self.username = username

    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, email={self.email}, username={self.username})"