from request import Request


class BaseController:
    """
    Base class for the bot controllers
    """
    def __init__(self, request: Request):
        """
        Initializes the controller with the +request+
        """
        self.request = request

    def process(self):
        """
        Write how do you want to process a request in nested controllers
        :return:
        """
        raise NotImplementedError
