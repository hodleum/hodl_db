class Column:
    def __init__(self, instance, primary_key=False):
        self.instance = instance
        self.primary_key = primary_key

    def __get__(self, instance, owner):
        pass

    def __set__(self, instance, value):
        pass


class String:
    type = str


class Integer:
    type = int
