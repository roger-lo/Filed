from abc import ABC, abstractmethod


class Action(ABC):
    """Abstract class for all actioner to implement"""

    @abstractmethod
    def process(self):
        """Process the file. Should return the file back for chaining."""
        pass


class MoveAction(Action):
    def __init__(self, destination):
        self.destination = destination

    def process(self, file):
        # TODO: Implement
        print("Pretending to move '{}' to '{}'".format(file, self.destination))
        return file


class RenameAction(Action):
    def __init__(self, regex):
        self.regex = regex

    def process(self, file):
        # TODO: Implement
        print("Pretending to rename '{}' to '{}'".format(file, self.regex))
        return file
