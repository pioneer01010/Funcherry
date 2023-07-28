class BaseError(Exception):
    message = 'Base error'

    def __init__(self, **kwargs):
        super().__init__()
        self.msg = self.message % kwargs

    def __str__(self):
        return self.msg


class RepositoryError(BaseError):
    message = "%(cause)s"


class FunctionParseError(BaseError):
    message = "%(cause)s"