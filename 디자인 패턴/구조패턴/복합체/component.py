class Component():
    def operation(self):
        pass

class Composite(Component):
    def __init__(self) -> None:
        self.components:list[Component] = []

    def add(self, c:Component):
        self.components.append(c)

    def remove(self, c:Component):
        self.components.remove(c)

    def get_child(self):
        return self.components

    def operation(self):
        for component in self.components:
            component.operation()

