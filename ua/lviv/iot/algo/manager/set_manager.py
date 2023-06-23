class SetManager:
    """
     Set manager class that operates on a set of objects.
    """

    def __init__(self, regular_manager):
        self.regular_manager = regular_manager

    def __iter__(self):
        """
        :return: An iterator yielding items from the regular_manager attribute.
        """
        for obj in self.regular_manager:
            for item in obj:
                yield item

    def __len__(self):
        """

        :return: The total length of the octane_number attribute.
        """
        return sum(len(obj.octane_number) for obj in self.regular_manager)

    def __getitem__(self, index):
        """

        :param index:
        :return:
        """
        for obj in self.regular_manager:
            for item in obj:
                if index == 0:
                    return item
                index -= 1
        raise IndexError("Index out of range"),

    def __next__(self):
        for obj in self.regular_manager:
            for item in obj:
                return item
        raise StopIteration
