import re

from .filterable import Filterable


class FilenameMatches(Filterable):

    def filter(self, files, *args):
        """
        Filters the given list of file names and returns the file names that
        match the given regex pattern.
        :param files: A list of file names.
        :param args: A regex pattern.
        :return: A list of filtered file names.
        """
        pattern = re.compile(args[0])
        filtered_files = []
        for f in files:
            if pattern.match(f):
                filtered_files.append(f)
        return filtered_files
