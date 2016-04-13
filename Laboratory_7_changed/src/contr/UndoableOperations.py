class AddOperation:
    """
    Class that models an add operation
    """
    def __init__(self, item):
        self._item = item

    def get_item(self):
        return self._item


class RemoveOperation:
    """
    Class that models a remove operation
    """
    def __init__(self, item):
        self._item = item

    def get_item(self):
        return self._item


class UpdateOperation:
    """
    Class that models an update operation
    """
    def __init__(self, old, updated):
        self._old = old
        self._updated = updated

    def get_old(self):
        return self._old

    def get_updated(self):
        return self._updated
