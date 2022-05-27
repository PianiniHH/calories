import sys
from food import Food


class Menu:
    def __init__(self, fieldnames: list, **kwargs) -> None:
        self.fieldnames = fieldnames

        for key, value in kwargs.items():
            setattr(self, key, value)

    def show_menu(self) -> None:
        """Show the menu as a numbered list."""
        for num, item in enumerate(self.fieldnames, 1):
            print(num, item)

    def get_and_validate_user_choice(self, exit: bool = True) -> str:
        if exit:
            exit_choice = ' or "q" to exit'
        else:
            exit_choice = ''
        loops = 0
        while True:
            if loops >= 3:
                print('This is getting ridiculous')
            choice = input(
                f'Press a number (1-{len(self.fieldnames)}){exit_choice}: ')
            if exit:
                if choice.lower() == 'q':
                    return 'Quit'
            try:
                choice = int(choice)
                if choice > 0:
                    choice = self.fieldnames[choice-1]
                else:
                    print('That is not a valid choice')
                    loops += 1
                    continue
            except ValueError:
                print(f'"{choice}" is not a number')
                loops += 1
            except IndexError:
                print('That is not a valid choice')
                loops += 1
            else:
                return choice

    def use_menu(self, exit: bool = True):
        self.show_menu()
        return self.get_and_validate_user_choice(exit=exit)


class MainMenu(Menu):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class FoodMenu(Menu):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


if __name__ == '__main__':

    MAIN_MENU_OPTIONS = ['Home', 'Back', 'Search', 'Food']
    FOOD_MENU_OPTIONS = ['Show All', 'Search', 'Add Food', 'Recipes']

    try:
        main_menu = MainMenu(fieldnames=MAIN_MENU_OPTIONS)
        food_menu = FoodMenu(fieldnames=FOOD_MENU_OPTIONS)
    except TypeError:
        print('specify fieldnames=[list of menu options]')
        sys.exit()

    choice = main_menu.use_menu()

    banana = food_menu.build_food('Banana')
    print(banana, type(banana))
