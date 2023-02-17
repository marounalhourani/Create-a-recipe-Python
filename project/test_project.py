from project import isfloat, get_recipe_info, Recipe, get_column_db
import pytest
import data


def test_isfloat():
    assert isfloat("5") == True
    assert isfloat(2) == True
    assert isfloat("2.5") == True
    assert isfloat(2.5) == True
    assert isfloat("hello world") == False

def test_get_recipe_info():
    recipe = Recipe(name="Pasta", description="A delicious pasta recipe")
    result = get_recipe_info(recipe)
    assert result[0]["recipe_name"] == "Pasta"
    assert result[0]["recipe_description"] == "A delicious pasta recipe"
    assert len(result) > 0
    assert result[0]['recipe_name'] == recipe.name
    assert result[0]['recipe_description'] == recipe.description

def test_get_column_db():
    Ingredients = [item[0] for item in data.data]
    assert get_column_db() == Ingredients




