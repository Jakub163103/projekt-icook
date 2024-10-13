from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

COMMON_INGREDIENTS = [
    "Chicken",
    "Beef",
    "Garlic",
    "Onion",
    "Tomato",
    "Rice",
    "Pasta",
    "Salt",
    "Pepper",
    "Olive Oil",
    "Butter",
    "Eggs",
    "Milk",
    "Cheese",
    "Carrot",
    "Potato",
    "Bell Pepper",
    "Mushroom",
    "Basil",
    "Oregano"
]

def fetch_meals_by_ingredient(ingredient):
    url = f"https://www.themealdb.com/api/json/v1/1/filter.php?i={ingredient}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get('meals')
    else:
        return {"error": f"Error: {response.status_code} - {response.text}"}

def fetch_meal_details(meal_id):
    url = f"https://www.themealdb.com/api/json/v1/1/lookup.php?i={meal_id}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get('meals')[0] if data.get('meals') else None
    else:
        return {"error": f"Error: {response.status_code} - {response.text}"}

@app.route('/', methods=['GET', 'POST'])
def home():
    recipes = []
    selected_ingredients = []
    error = ""
    all_ingredients = COMMON_INGREDIENTS 

    if request.method == 'POST':
        selected_ingredients = request.form.getlist('ingredients')
        selected_ingredients = [ing.strip().lower() for ing in selected_ingredients if ing.strip()]

        if selected_ingredients:
            meal_ids = None

            for ingredient in selected_ingredients:
                meals = fetch_meals_by_ingredient(ingredient)
                if isinstance(meals, dict) and 'error' in meals:
                    error = meals['error']
                    recipes = []
                    break
                elif meals:
                    current_ids = set(meal['idMeal'] for meal in meals)
                    if meal_ids is None:
                        meal_ids = current_ids
                    else:
                        meal_ids &= current_ids  
                else:
                    error = f"No meals found with the ingredient '{ingredient}'."
                    recipes = []
                    break

            if not error and meal_ids:
                for meal_id in meal_ids:
                    meal_details = fetch_meal_details(meal_id)
                    if isinstance(meal_details, dict) and 'error' in meal_details:
                        error = meal_details['error']
                        recipes = []
                        break
                    elif meal_details:
                        ingredients_list = []
                        for i in range(1, 21):
                            ingredient = meal_details.get(f'strIngredient{i}')
                            measure = meal_details.get(f'strMeasure{i}')
                            if ingredient and ingredient.strip():
                                ingredients_list.append({
                                    'ingredient': ingredient.strip(),
                                    'measure': measure.strip() if measure else ""
                                })

                        recipes.append({
                            'id': meal_details.get('idMeal'),
                            'title': meal_details.get('strMeal'),
                            'category': meal_details.get('strCategory'),
                            'area': meal_details.get('strArea'),
                            'instructions': meal_details.get('strInstructions'),
                            'thumbnail': meal_details.get('strMealThumb'),
                            'ingredients': ingredients_list
                        })
        else:
            error = "Please select at least one ingredient."

    return render_template('index.html', recipes=recipes, selected_ingredients=selected_ingredients, all_ingredients=all_ingredients, error=error)

if __name__ == '__main__':
    app.run(debug=True)