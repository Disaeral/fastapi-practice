class User:
    def __init__(self, username, fullname, password):
        self.username: str = username
        self.password: str = password
        self.fullname: str = fullname

    # def _hash_pass(self, secret: str):
    #     return f"cached_{secret}"

    # def validate(self):
    #     if len(self.username) < 5:
    #         raise ValueError("Username is too short")
    #     elif "cached_" not in self.password:
    #         raise ValueError("invalid password hashing")
