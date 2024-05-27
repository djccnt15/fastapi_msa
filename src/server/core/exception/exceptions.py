class NotUniqueException(Exception):
    def __init__(self, *args: object, obj, detail) -> None:
        super().__init__(*args)
        self.obj = obj
        self.detail = detail


class QueryResultEmpty(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
