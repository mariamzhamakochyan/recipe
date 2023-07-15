class Comment:
    def __init__(self, recipe, user, text):
        self.recipe = recipe
        self.user = user
        self.text = text

    def save(self):
        self.recipe.comment(self.user, self.text)
        print(self.text)