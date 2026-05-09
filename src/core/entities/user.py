class User:
    def __init__(self, username, fullname, password, is_banned, id):
        self.id: int = id
        self.is_banned: bool = is_banned
        self.username: str = username
        self.password: str = password
        self.fullname: str = fullname
    
    def ban(self):
        self.is_banned = True
    
    def unban(self):
        self.is_banned = False