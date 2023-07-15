class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.saved_recipes = []

    def save_recipe(self, recipe):
        self.saved_recipes.append(recipe)

    def show_saved_recipes(self):
        print(f"Saved recipes for {self.name}:")
        for recipe in self.saved_recipes:
            print(recipe.title)