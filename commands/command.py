from abc import ABCMeta, abstractmethod


class Command:

    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def execute(self, channel, parameters):
        pass
