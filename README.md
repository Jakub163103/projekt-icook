# Recipe Finder Web Application

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [API Reference](#api-reference)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The **Recipe Finder** is a Flask-based web application that allows users to discover meal recipes based on selected ingredients. By selecting one or more common ingredients, users can find recipes that incorporate all chosen items. The application leverages [TheMealDB API](https://www.themealdb.com/api.php) to fetch and display a diverse range of meal options.

## Features

- **Ingredient Selection**: Choose from a predefined list of common ingredients to find matching recipes.
- **Dynamic Recipe Fetching**: Retrieves meals that include all selected ingredients.
- **Detailed Recipe Information**: Provides comprehensive details for each recipe, including ingredients, measurements, instructions, category, and area.
- **Error Handling**: Notifies users of any issues, such as API errors or no matching recipes found.
- **Responsive Design**: User-friendly interface optimized for various devices.

## Technologies Used

- **Backend**:
  - [Flask](https://flask.palletsprojects.com/) - A lightweight WSGI web application framework.
  - [Requests](https://requests.readthedocs.io/) - For making HTTP requests to external APIs.
  - [dotenv](https://github.com/theskumar/python-dotenv) - For managing environment variables.
- **Frontend**:
  - HTML/CSS - For structuring and styling the web pages.
- **API**:
  - [TheMealDB API](https://www.themealdb.com/api.php) - Provides a vast database of meal recipes.

## Installation

1. **Clone the Repository**
    ```bash
    git clone https://github.com/yourusername/recipe-finder.git
    cd recipe-finder
    ```

2. **Create a Virtual Environment**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

## Configuration

1. **Environment Variables**

    Create a `.env` file in the root directory of the project to store your environment variables. This file should include any sensitive information such as API keys.

    ```env
    FLASK_APP=app.py
    FLASK_ENV=development
    # Add other environment variables as needed
    ```

    > **Note**: Ensure that the `.env` file is included in `.gitignore` to prevent sensitive information from being exposed.

## Usage

1. **Run the Application**
    ```bash
    flask run
    ```

2. **Access the Application**

    Open your web browser and navigate to `http://127.0.0.1:5000/` to access the Recipe Finder.

3. **Using the Application**

    - **Select Ingredients**: Choose one or more ingredients from the provided list.
    - **Find Recipes**: Submit your selection to view recipes that include all chosen ingredients.
    - **View Details**: Click on a recipe to view detailed information, including ingredients, measurements, and cooking instructions.

## API Reference

The application interacts with [TheMealDB API](https://www.themealdb.com/api.php) to fetch meal data. Below are the primary endpoints used:

- **Filter Meals by Ingredient**
    - **Endpoint**: `/filter.php`
    - **Description**: Retrieves a list of meals that include a specific ingredient.
    - **Example**:
        ```python
        def fetch_meals_by_ingredient(ingredient):
            url = f"https://www.themealdb.com/api/json/v1/1/filter.php?i={ingredient}"
            response = requests.get(url)
            # Handle response
        ```

- **Lookup Meal Details by ID**
    - **Endpoint**: `/lookup.php`
    - **Description**: Fetches detailed information about a specific meal using its unique ID.
    - **Example**:
        ```python
        def fetch_meal_details(meal_id):
            url = f"https://www.themealdb.com/api/json/v1/1/lookup.php?i={meal_id}"
            response = requests.get(url)
            # Handle response
        ```

## Project Structure
