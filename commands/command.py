from abc import ABCMeta, abstractclassmethod


class Command:

    __metaclass__ = ABCMeta

    @abstractclassmethod
    def execute(self, channel, parameters):
        pass
