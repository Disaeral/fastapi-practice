class Post:
    def __init__(self, title, body, user_id) -> None:
        self.title: str = title
        self.body: str = body
        self.user_id: int = user_id