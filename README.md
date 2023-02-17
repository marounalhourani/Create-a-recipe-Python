# Recipe Creator

The Recipe Creator is a Python project designed to create recipes based on user input, generate a PDF file containing the recipe information and its nutritional value, and store the data in an efficient way using SQLite3.

## Table of Contents

- [Introduction](#introduction)
- [How It Works](#how-it-works)
- [Usage](#usage)
- [Installation](#installation)
- [Contributing](#contributing)
- [License](#license)

## Introduction

In the main file `project.py`, the project contains many functions and 2 classes. Firstly, a class called Recipe is created to store information about the recipe. Setter and getter methods with decorators such as `@property` and `.setter` are used to store the name of the ingredients with the quantity, name, and description of the recipe. User input is verified when using the setter method.

The main function of the project lets the user input ingredients and their quantity to make a recipe. Users can only input ingredients that are in the table that is shown to them. The project is connected to a database using the SQLite3 library to store the data in an efficient way.

## How It Works

In `data.py`, an array called `data` is created to store the information needed, so it can be modified and changed later. To create the database containing the ingredients, a new file called `create.py` is created, which creates a database based on the list `data` in `data.py`. A column called `qty_gram` is put in the file, giving it a default value of 100, which represents the nutritional value of the ingredients for each 100 grams. When needing to update the database, go to `data.py`, modify the array, delete the old database, go to `create.py`, and run it to create the new database.

In `project.py`, a function called `get_column_db` accesses the database and returns the first row in an array. This information is used to create a table containing all the ingredients, so the user can visually see what ingredients are available. A function called `get_ing_qty` allows to know how much of each ingredient the user input. A function called `get_recipe_info` summarizes all the information the user has input, including how many ingredients the recipe has, the name of the recipe, and all the nutritional information.

To build the tables containing the ingredients, the prettytable library is used. A class called PDF is used with the function `create_pdf` and the fpdf library to create a PDF file that summarizes all the information of the recipe.

## Usage

Please note that all input is case-sensitive.

To use the project, you can follow the steps below:

1. Install the required libraries listed in `requirements.txt` using pip.
2. Run the `project.py` file.
3. Input the ingredients and their quantities to create a recipe.
4. Check the PDF file generated containing the recipe information and its nutritional value.

## Installation

To install the required libraries, run the following command:

pip install -r requirements.txt


## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.
