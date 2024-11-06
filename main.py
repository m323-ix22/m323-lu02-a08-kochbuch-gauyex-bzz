"""
author: Xavier Gauye
date: 06.11.2024
"""


import json


def sum_of_numbers(numbers):
    return sum(numbers)


def parse_recipe(json_string):
    recipe_ = json.loads(json_string)
    return recipe_


def adjust_recipe(recipe_, num_people):
    factor = num_people / recipe_['servings']
    adjusted_ingredients = {ingredient: int(quantity * factor) for ingredient, quantity in
                            recipe_['ingredients'].items()}
    return {
        'title': recipe_['title'],
        'ingredients': adjusted_ingredients,
        'servings': num_people
    }


def load_recipe(json_string):
    return json.loads(json_string)


if __name__ == '__main__':
    recipe_json = ('{"title": "Spaghetti Bolognese", "ingredients": {"Spaghetti": 400, "Tomato Sauce": 300, '
                   '"Minced Meat": 500}, "servings": 4}')

    recipe = parse_recipe(recipe_json)
    print(recipe)
