# Project Name

The goal of this project is to create a recipe based on user input, generate a PDF file containing the recipe information and its nutritional value.

## Project Structure

In my main file, `project.py`, I have many functions and 2 classes. Firstly, I created a class called `Recipe` to store information about the recipe. I use setter and getter methods with decorators such as `@property` and `.setter` to store the name of the ingredients with the quantity, name, and description of the recipe. I also verify user input when using the setter method.

The main function of the project lets the user input ingredients and their quantity to make a recipe. Users can only input ingredients that are in the table that is shown to them.

I connect my project to a database using the `sqlite3` library to store the data in an efficient way. I created a separate file called `data.py` where I store the information needed, so it can be modified and changed later. In `data.py`, I have an array called `data`. The tuples in this array represent the rows of my database, and to visualize it easily, I have put a comment at the top of the file indicating the columns of the database.

To create the database containing the ingredients, I created a new file called `create.py`, which creates a database based on the list `data` in `data.py`. I put another column called `qty_gram` in the file, giving it a default value of 100, which represents the nutritional value of the ingredients for each 100 grams.

When I need to update my database, I go to `data.py`, modify the array, delete the old database, go to `create.py`, and run it to create the new database.

In `project.py`, I have a function called `get_column_db`. This function accesses the database and returns the first row in an array. This information is used to create a table containing all the ingredients, so the user can visually see what ingredients are available.

I also have a function called `get_ing_qty`. This function allows me to know how much of each ingredient the user input. This is important as the user may input the same ingredient multiple times, so this function adds up the times and the quantity of the same ingredient.

Additionally, in `project.py`, we have `get_recipe_info`, which summarizes all the information the user has input. This includes how many ingredients the recipe has, the name of the recipe, and all the nutritional information. It summarizes all the information of the recipe.

To build the tables containing the ingredients, I use the `prettytable` library. To use this library, I downloaded it using `pip install prettytable`.

My `get_recipe_info` function returns a list of dictionaries summarizing the recipe. I use the `json` library to show this list in a proper and better way.

Furthermore, I have the class `PDF`, which I use with the function `create_pdf` and the `fpdf` library. To use this library, I downloaded it using `pip install fpdf`. These three components work together to help create a PDF file that summarizes all the information of the recipe.

Finally, I have a function called `isfloat` that checks if the input (string or not) can be converted to a float number.

## Requirements

In the `requirements.txt` file, I list the libraries that I will need to install using pip before running the program.

## Testing

I also have a `test_project.py` file which tests some of the functionalities of my project.

Please note that all input is case-sensitive.
