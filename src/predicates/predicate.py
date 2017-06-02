import re

from abc import ABC, abstractmethod


class Predicate(ABC):
    @abstractmethod
    def match(self):
        """ Returns true if file satisfies predicate. False otherwise. """
        pass


class RegexPredicate(Predicate):
    def __init__(self, regex_str):
        self.regex = re.compile(regex_str)

    def match(self, path):
        return bool(self.regex.match(path))
