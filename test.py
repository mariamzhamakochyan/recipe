from user import User
from comment import Comment
from rating import Rating
from resipe import Recipe, VegetarianRecipe, DessertRecipe


chocolate_cake = DessertRecipe('Chocolate Cake', ['Flour', 'Sugar', 'Cocoa'], 'Mix, bake')

bob = User('Bob', 'bob@gmail.com')

bob.save_recipe(chocolate_cake)

bob_rating = Rating(chocolate_cake, bob, 4)
bob_rating.save()

bob_comment = Comment(chocolate_cake, bob, 'This cake is amazing')
bob_comment.save()
bob.show_saved_recipes() 