class SomeException(Exception):
    """
    Completely inherited exception
    """
    pass

class SomeError(Exception):
    def __init__(self, arg, message):
        self.arg = arg
        self.message = message
        super().__init__(message)
    
    def __str__(self):
        return f"{self.arg} -> {self.message}"

raise SomeError("myArg", "myMsg")
# __main__.SomeError: myArg -> myMsg
