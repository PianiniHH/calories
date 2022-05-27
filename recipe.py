from food import Food
import helper as hlp
import csv

DATA_FILE_FOOD = 'foods.csv'
DATA_FILE_RECIPES = 'recipes.csv'


class Recipe:
    fieldnames = ['name', 'ingredient_1', 'ingredient_1_qt', 'ingredient_2', 'ingredient_2_qt',
                  'ingredient_3', 'ingredient_3_qt', 'ingredient_4', 'ingredient_4_qt', 'ingredient_5', 'ingredient_5_qt']

    def __init__(self, name: str, ingredients: dict = {}) -> None:
        self.name = name
        self.ingredients = ingredients
        self.calories = None

    def __repr__(self):
        return self.name

    @classmethod
    def create_and_save_new_recipe(cls, location=None) -> None:
        recipe_name = input('Recipe Name: ')
        saveable_recipe = Recipe(name=recipe_name)
        saveable_recipe = saveable_recipe.gather_ingredients()
        recipe = Recipe.build_recipe_object_from_dict(
            saveable_recipe)
        recipe.show_recipe()
        if hlp.get_user_confirmation('Would you like to save the recipe? (y/n): '):
            hlp.add_to_csv_file(saveable_recipe, location, Recipe.fieldnames)

    @classmethod
    def build_recipe_object_from_dict(cls, ingredients: dict):
        recipe_name = ingredients.pop('name')
        recipe = Recipe(name=recipe_name, ingredients=ingredients)
        recipe.ingredients = recipe.convert_ingredients_from_csv(ingredients)
        return recipe

    @classmethod
    def prepare_recipe_data(cls, location: str) -> list:
        data = hlp.convert_csv_file_to_list(location)
        return list(map(Recipe.build_recipe_object_from_dict, data))

    def gather_ingredients(self):
        ingredients = {'name': self.name.title()}
        foods = Food.prepare_food_data(DATA_FILE_FOOD)
        count = 1
        while True:
            search_item = input('Add ingredient: ')
            ingredient = hlp.search_food_collection(
                foods, search_item)
            if ingredient:
                print(ingredient)
            else:
                if hlp.get_user_confirmation('Would you like to add this food to the database? (y/n): '):
                    add_food = Food.create_new_food(name=search_item)
                    Food.add_to_csv_file(add_food, DATA_FILE_FOOD)
                    foods = Food.prepare_food_data('foods.csv')
                    ingredient = hlp.search_food_collection(
                        foods, search_item)
                    print(ingredient)
                else:
                    continue
            if hlp.get_user_confirmation('Add ingredient to recipe? (y/n): '):
                ingredients[f'ingredient_{count}'] = ingredient.name
                quantity = input('Quantity: ')
                hlp.show_enumerated_list(Food.available_measurements)
                measure = int(input('Choose measurement: '))
                quantity += Food.available_measurements[measure-1]
                ingredients[f'ingredient_{count}_qt'] = quantity
            if hlp.get_user_confirmation('Add another ingredient? (y/n): '):
                count += 1
                continue
            return ingredients

    def convert_ingredients_from_csv(self, ingredients: dict) -> dict:
        ingredient = []
        quantity = []
        for key, value in ingredients.items():
            if 'qt' in key:
                quantity.append(value)
            else:
                ingredient.append(value)
        return dict(zip(ingredient, quantity))

    def show_ingredients(self, food_file: str) -> None:
        ingredients = []
        food_list = Food.prepare_food_data(food_file)
        for food in food_list:
            for key, _ in self.ingredients.items():
                if 'qt' not in key:
                    if key == food.name:
                        ingredients.append(food)
        hlp.show_enumerated_list(ingredients)

    def show_recipe(self):
        print(self.name)
        for key, value in self.ingredients.items():
            print(key, value)


if __name__ == '__main__':
    new_recipe = Recipe.create_and_save_new_recipe()

    # with open('recipes.csv', 'a') as f:
    #     fieldnames =
    #     writer = csv.DictWriter(f, fieldnames=fieldnames)

    #     writer.writerow(new_recipe)

    # with open('recipes.csv', newline='') as f:
    #     reader = csv.DictReader(f, delimiter=',')
    #     recipes = list(reader)

    # my_recipes = Recipe.prepare_recipe_data(DATA_FILE_RECIPES)

    # print(my_recipes[0].name)
    # my_recipes[0].show_ingredients(DATA_FILE_FOOD)
