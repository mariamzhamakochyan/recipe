class Rating:
    def __init__(self, recipe, user, score):
        self.recipe = recipe
        self.user = user
        self.score = score

    def save(self):
        self.recipe.rate(self.user, self.score)