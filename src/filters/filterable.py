class Filterable:
    """
    Abstract class for any filtering functionality.
    All the below methods should be implemented.
    """

    def filter(self, files, *args):
        """
        Filters the given list of file names and returns the file names that
        match a particular criteria.
        :param files: A list of file names.
        :param args: Further arguments to help filter the file names.
        :return: A list of filtered file names.
        """
        raise NotImplementedError('This method should be implemented.')
