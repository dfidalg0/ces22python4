class Ingredient:
    @classmethod
    def getDescription(cls):
        return cls.__name__

    @classmethod
    def getTotalCost(cls):
        return cls.cost

class Pizza(Ingredient):
    cost = 10.00

class Decorator(Ingredient):
    def __init__(self, ingredient):
        self.component = ingredient

    def getTotalCost(self):
        return self.component.getTotalCost() + super().getTotalCost()

    def getDescription(self):
        return f'{super().getDescription()} {self.component.getDescription()}'

class Bacon(Decorator):
    cost = 2.00

    def __init__(self, ingredient):
        super().__init__(ingredient)

class Mozzarella(Decorator):
    cost = 1.00

    def __init__(self, ingredient):
        super().__init__(ingredient)

class Parmesan(Decorator):
    cost = 1.00

    def __init__(self, ingredient):
        super().__init__(ingredient)

class Gorgonzola(Decorator):
    cost = 1.00

    def __init__(self, ingredient):
        super().__init__(ingredient)

class Provolone(Decorator):
    cost = 1.00

    def __init__(self, ingredient):
        super().__init__(ingredient)

class Tomato(Decorator):
    cost = 0.50

    def __init__(self, ingredient):
        super().__init__(ingredient)

class Ham(Decorator):
    cost = 0.50

    def __init__(self, ingredient):
        super().__init__(ingredient)

class Chicken(Decorator):
    cost = 2.00

    def __init__(self, ingredient):
        super().__init__(ingredient)

four_cheese = Gorgonzola(Parmesan(Provolone(Mozzarella(Pizza()))))

print(four_cheese.getDescription())
print(f'Cost: $ {four_cheese.getTotalCost():.2f}')
