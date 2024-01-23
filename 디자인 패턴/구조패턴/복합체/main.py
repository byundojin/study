import component

class Box(component.Composite):
    def __init__(self, number) -> None:
        super().__init__()
        self.number = number

    def operation(self):
        print("call box :", self.number)
        super().operation()

class Product(component.Component):
    def __init__(self, name) -> None:
        super().__init__()
        self.name = name

    def operation(self):
        print("call product :",self.name)
        super().operation()

pack1 = Box(1)
pack1.add(Product("a1"))
pack1.add(Product("a2"))
pack2 = Box(2)
pack2.add(Product("b1"))
pack2.add(Product("b2"))
pack1.add(pack2)

pack1.operation()
print("-------------")
pack2.operation()