import csv


def search_list_for_item(food: list):
    user_search = input('What are you looking for? ')
    for item in food:
        if user_search.title() == item.name:
            print(item)
            break
    else:
        print('Item not found')


def get_user_confirmation(message: str) -> bool:
    while True:
        user_choice = input(message).lower()
        if user_choice != 'y' and user_choice != 'n':
            print('That is not a valid entry')
        else:
            match user_choice:
                case 'y':
                    return True
                case 'n':
                    return False


def convert_csv_file_to_list(file: str) -> list:
    with open(file, newline='') as f:
        new_list = csv.DictReader(f, delimiter=',')
        new_list = list(new_list)
        return new_list


def show_enumerated_list(items: list):
    for num, item in enumerate(items, 1):
        print(num, item)


def search_food_collection(foods, choice):
    for item in foods:
        if item.name == choice.title():
            return item
    else:
        print('Item not found')
        return False


def add_to_csv_file(items: dict, csv_file: str, fieldnames: list) -> None:
    with open(csv_file, 'a', newline='') as csvfile:
        data_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        data_writer.writerow(items)


def get_and_validate_user_choice(choices: list) -> int:
    while True:
        choice = input(
            f'Press a number (1-{len(choices)})')
        try:
            choice = int(choice)
            if 0 < choice <= len(choices):
                return choice
            else:
                print('That is not a valid choice')
                continue
        except ValueError:
            print(f'"{choice}" is not a number')
        except IndexError:
            print('That is not a valid choice')
