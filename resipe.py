from abc import ABC, abstractmethod

class Recipe(ABC):
    def __init__(self, title, ingredients, instructions):
        self.title = title
        self.ingredients = ingredients
        self.instructions = instructions
        self.rating = None
        self.comments = []

    @abstractmethod
    def get_type(self):
        pass

    def rate(self, user, score):
        self.rating = score

    @abstractmethod
    def comment(self, user, text):
        pass

class VegetarianRecipe(Recipe):
    def __init__(self, title, ingredients, instructions):
        super().__init__(title, ingredients, instructions)

    def get_type(self):
        return 'vegetarian'
        
    def comment(self, user, text):
        print("Comment for Vegetarian recipe...")
        self.comments.append((user, text))

class DessertRecipe(Recipe):
    def __init__(self, title, ingredients, instructions):
        super().__init__(title, ingredients, instructions)

    def get_type(self):
        return 'dessert'
    
    def comment(self, user, text):
        print("Comment for Dessert...")
        self.comments.append((user, text))