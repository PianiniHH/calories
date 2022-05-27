import csv
import helper as hlp


class Food:
    available_measurements = ['g', 'kg', 'ltr', 'pcs']
    fieldnames = ['name', 'category', 'calories',
                  'carbohydrates', 'protein', 'fat', 'measurement']

    def __init__(self, name, category, calories, carbohydrates, protein, fat, measurement):
        self.name = name
        self.category = category
        self.calories = calories
        self.carbohydrates = carbohydrates
        self.protein = protein
        self.fat = fat
        self.measurement = measurement

    def __repr__(self):
        return self.name

    def __str__(self):
        return f'{self.name} ({self.category}) | Calories: {self.calories} kcal | Carbs: {self.carbohydrates}g | Protein: {self.protein}g | Fat: {self.fat}g'

    @classmethod
    def build_food_from_dict(cls, raw_data: dict):
        """Takes information from a dictionary and converts them into a Food object."""
        return Food(
            raw_data['name'],
            raw_data['category'],
            int(raw_data['calories']),
            float(raw_data['carbohydrates']),
            float(raw_data['protein']),
            float(raw_data['fat']),
            raw_data['measurement']
        )

    @classmethod
    def create_new_food(cls, name: str = '') -> dict:
        """Ask user for input and return a dictionary that can be saved to the csv file."""
        new_food = {}
        if name == '':
            new_food['name'] = input('Name: ').title()
        else:
            new_food['name'] = name.title()
            print(f'Name: {name}')
        new_food['category'] = input('Category: ').title()
        new_food['calories'] = input('Calories: ')
        new_food['carbohydrates'] = input('Carbs: ')
        new_food['protein'] = input('Protein: ')
        new_food['fat'] = input('Fat: ')
        hlp.show_enumerated_list(Food.available_measurements)
        measure = input('Choose measure: ')
        new_food['measurement'] = Food.available_measurements[int(
            measure) - 1]
        return new_food

    @classmethod
    def prepare_food_data(cls, location: str) -> list:
        data = hlp.convert_csv_file_to_list(location)
        return list(map(Food.build_food_from_dict, data))

    def calculate_calories_per_gramm(self):
        return self.calories / 100


if __name__ == '__main__':
    # print(Food.available_measurements)
    # my_food = Food.create_new_food()
    # my_food = Food.build_food_from_dict(my_food)
    # print(my_food)
    # print(my_food.__dict__)
    test_food = Food('Essen', 'Fressen', 300, 20, 1, 4, 'g')
    # fieldnames = [attr for attr in dir(test_food) if not callable(
    #     getattr(test_food, attr)) and not attr.startswith("__")]
