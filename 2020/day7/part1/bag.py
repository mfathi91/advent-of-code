class Bag:

    def __init__(self, name: str):
        assert name
        self.name = name
        self.children = set()


    def add_child(self, child):
        self.children.add(child)


    def contains(self, bag):
        for child in self.children:
            if child.name == bag.name:
                return True

        for child in self.children:
            if child.contains(bag):
                return True

        return False

    def __str__(self):
        result = self.name
        children_name = []
        for child in self.children:
            children_name.append(child.name)
        return f'{self.name} -> {children_name}'
