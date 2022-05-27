import sys
import csv

import helper as hlp
from food import Food
from menu import Menu, FoodMenu
from recipe import Recipe

MAIN_MENU_OPTIONS = ['Food', 'Search', 'Recipes']
FOOD_MENU_OPTIONS = ['Show All Food', 'Home', 'Add Food', 'Recipes']
RECIPE_MENU_OPTIONS = ['Add Recipe', 'Show All Recipes', 'Home']

MAIN_MENU = Menu(fieldnames=MAIN_MENU_OPTIONS)
FOOD_MENU = FoodMenu(fieldnames=FOOD_MENU_OPTIONS)
RECIPE_MENU = Menu(fieldnames=RECIPE_MENU_OPTIONS)

DATA_FILE_FOOD = 'foods.csv'
DATA_FILE_RECIPES = 'recipes.csv'


def app_controller(choice: str, food: list = [], recipes: list = []) -> bool:
    match choice:
        case 'Home':
            return False
        case 'Show All Food':
            hlp.show_enumerated_list(food)
        case 'Food':
            food_choice = FOOD_MENU.use_menu()
            app_controller(food_choice, food, recipes)
        case 'Add Food':
            while True:
                new_food = Food.create_new_food()
                print(new_food)
                if hlp.get_user_confirmation('Would you like to proceed (y/n): '):
                    hlp.add_to_csv_file(
                        new_food, DATA_FILE_FOOD, Food.fieldnames)
                    return True
                else:
                    food_choice = FOOD_MENU.use_menu()
                    app_controller(food_choice, food, recipes)
                    break
        case 'Search':
            user_search = input('Food name: ')
            user_food = hlp.search_food_collection(food, user_search)
            print(user_food)
        case 'Quit':
            sys.exit()
        case 'Recipes':
            recipe_choice = RECIPE_MENU.use_menu()
            app_controller(recipe_choice, food, recipes)
        case 'Show All Recipes':
            hlp.show_enumerated_list(recipes)
            recipe_show_choice = hlp.get_and_validate_user_choice(recipes)
            recipes[recipe_show_choice-1].show_ingredients(DATA_FILE_FOOD)
        case 'Add Recipe':
            Recipe.create_and_save_new_recipe(DATA_FILE_RECIPES)
            return True


def main(food, recipes):
    """Execute the app"""
    while True:
        initialize = True
        if initialize:
            my_food = Food.prepare_food_data(food)
            my_recipes = Recipe.prepare_recipe_data(recipes)
            initialize = False
        reset = False
        if reset == True:
            my_recipes = Recipe.prepare_recipe_data(recipes)
            my_food = Food.prepare_food_data(food)
            reset = False
        user_choice = MAIN_MENU.use_menu()
        reset = app_controller(user_choice, my_food, my_recipes)


if __name__ == '__main__':
    main(DATA_FILE_FOOD, DATA_FILE_RECIPES)
