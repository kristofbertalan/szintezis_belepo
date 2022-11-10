class Car:

    def __init__(self, make, model, owner):
        self.make = make
        self.model = model
        self.owner = owner

    def get_make(self):
        return self.make

    def set_make(self, make):
        self.make = make

    def get_model(self):
        return self.model

    def set_model(self, model):
        self.model = model

    def get_owner(self):
        return self.owner

    def set_owner(self, owner):
        self.owner = owner


    def __str__(self):
        return f"Car(make={self.make}, model={self.model}, owner={self.owner})"

    def __repr__(self):
        return f"Car(make={self.make}, model={self.model}, owner={self.owner})"









