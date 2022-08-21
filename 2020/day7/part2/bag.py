class Bag:

    def __init__(self, name: str):
        assert name
        self.name = name
        self.children = {}


    def add_child(self, child_bag, count: int):
        assert child_bag
        assert count > 0
        self.children[child_bag] = count
        

    def children_count(self) -> int:
        children_count = 0
        for child in self.children:
            cc = self.children[child]
            children_count += cc
            children_count += cc * child.children_count()
        return children_count


    def __str__(self):
        children_info = []
        for child in self.children:
            children_info.append(f'{self.children[child]} {child.name}')
        return f'{self.name} -> {children_info}'
