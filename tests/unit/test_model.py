from cook_api.models import Recipe
import pytest

def test_create_recipe():
    """
    GIVEN a Recipe model
    WHEN a new Recipe is created
    THEN check the name, ingredients, steps, rating and favorite fields are defined correctly
    """
    recipe = Recipe('Pizza', 'Flour, Water, Salt, Yeast, Tomato Sauce, Cheese', 'Mix the ingredients, let it rest, bake it', 5, True)
    assert recipe.name == 'Pizza'
    assert recipe.ingredients == 'Flour, Water, Salt, Yeast, Tomato Sauce, Cheese'
    assert recipe.steps == 'Mix the ingredients, let it rest, bake it'
    assert recipe.rating == 5
    assert recipe.favorite == True

