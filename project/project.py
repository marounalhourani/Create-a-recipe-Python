import sqlite3
import json
from data import data
from prettytable import PrettyTable
from fpdf import FPDF


class Recipe:

    def __init__(self, name="name not Found", description="description not Found"):
        self._ingredients = []
        self._name = name
        self._description = description

    def __str__(self):
        return f"this recipe is called: {self._name}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @property
    def ingredients(self):
        list_ing = ""

        for i in self._ingredients:
            list_ing +=  ', '.join(i.keys()) + "\n"

        return set(list_ing)

    @ingredients.setter
    def ingredients(self, args):
        ingredient, qty = args
        if ingredient not in get_column_db():
            print("ingredient not Found ")
        elif float(qty) <= 0:
            print("Invalid qty ")
        else:
            self._ingredients.append({ingredient: qty})


class PDF(FPDF):
    def __init__(self):
        super().__init__()

    def table(self, header, data):
        # Colors, line width and font bold
        self.set_fill_color(255, 255, 255)
        self.set_text_color(0, 0, 0)
        self.set_line_width(0.3)
        self.set_font('Arial', 'B', 12)

        # Calculate total width of table
        table_width = self.w - 2 * self.l_margin
        col_width = table_width / len(header)

        # Header
        for col in header:
            self.cell(40, 7, col, 1)
        self.ln()



        # Data
        self.set_fill_color(255, 255, 255)
        self.set_text_color(0, 0, 0)
        self.set_line_width(0.3)
        self.set_font('Arial', '', 12)

        for row in data:
            for col in row:
                self.cell(40, 7, str(col), 1)
            self.ln()


def get_column_db():
    conn = sqlite3.connect("project_database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM ingredients")
    rows = cursor.fetchall()
    first_column = [row[0] for row in rows]
    cursor.close()
    conn.close()
    return first_column

def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def create_pdf(a):
    recipe_name = a.name + " recipe.pdf"
    pdf = PDF()
    pdf.set_title(a.name)
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    title = a.name
    pdf.cell(0, 10, title, 0, 1, 'C')


    header = ['Ingredients', 'Quantity(g)', 'Calories', 'Fat', 'Proteins']

    data_1 = get_recipe_info(a)
    data_1 = data_1[1:-1]
    data_2 = []
    for y in data_1:
        list_info = [y["ingredient"], y["qty(gram)"], y["calories"], y["fat"], y["proteins"]]
        data_2.append(list_info)

    pdf.table(header, data_2)

    pdf.ln()

    header_final = ['Total Mass (g)', 'Total Calories', 'Total Fat', 'Total Proteins']
    data_2 = get_recipe_info(a)[-1]
    data_final = [[data_2["Weight(gram)"], data_2["Total Calories"], data_2["Total Fat"], data_2["Total Proteins"]]]

    # Add the second table to the PDF document
    pdf.table(header_final, data_final)

    pdf.ln()

    pdf.set_font('Arial', 'I', 12)
    description = a.description
    pdf.cell(0, 10, description, 0, 1, 'C')

    pdf.output(recipe_name, 'F')


#argument should be the name of the object
def get_ing_qty(a):
    list_ing = a._ingredients
    ingredients = {}

    for item in list_ing:
        ingredient, qty = list(item.items())[0]
        if ingredient in ingredients:
            ingredients[ingredient] += qty
        else:
            ingredients[ingredient] = qty

    result = [{ingredient: qty} for ingredient, qty in ingredients.items()]

    return result

# the argument should be the name of the object
#retrive all info from recipe, total qty, fat, etc, for each ingredient
def get_recipe_info(a):
    conn = sqlite3.connect('project_database.db')
    cursor = conn.cursor()
    info = []

    for i in get_ing_qty(a):
        ingredient = str(list(i.keys())[0])
        ing_qty = i[ingredient]
        query = f"SELECT * FROM ingredients WHERE name = '{ingredient}'"
        cursor.execute(query)
        result = cursor.fetchall()
        result = list(result[0])
        arr = [item * ing_qty if isinstance(item, int) else item for item in result]
        info.append({"ingredient": arr[0], "fat":round(arr[1],1), "calories":round(arr[2],1), "proteins": round(arr[3],1), "qty(gram)": round(arr[4],1)})

    cursor.close()
    conn.close()

    total_fat = 0
    total_calories = 0
    total_proteins = 0
    total_qty = 0
    total_ingredients = ""
    for y in info:
        total_fat = total_fat + y["fat"]
        total_calories = total_calories + y["calories"]
        total_proteins = total_proteins + y["proteins"]
        total_qty = total_qty + y["qty(gram)"]
        total_ingredients = total_ingredients + y["ingredient"] + " "

    info.append({"All Ingredients": total_ingredients, "Total Fat": round(total_fat,1), \
                 "Total Calories": round(total_calories,1), "Total Proteins": round(total_proteins,1), "Weight(gram)": round(total_qty,1)})
    info.insert(0,{"recipe_name": a.name, "recipe_description": a.description})

    return info

def main():

    #Display Table
    while True:
        try:
            inp = input("Make your recipe here!, to view the ingredients alone, please click 'v' and enter, to view the ingredients with there \
                        nutrious value plesae click 'x' and enter, otherwise, press ENTER: ")
            if inp == "v":
                my_table = PrettyTable(['Strings'])
                my_table.max_width['Strings'] = 50
                for string in get_column_db():
                    my_table.add_row([string])
                print(my_table)
                break
            elif inp == "x":
                table = PrettyTable()
                table.field_names = ['Ingredient', 'Fat', 'Calories', 'Proteins']
                for row in data:
                    table.add_row(row)

                print(table)
                break
            elif inp == "":
                break
            else:
                raise ValueError
        except ValueError:
            print("Invalid input, please try again")

    recipe = Recipe()
    recipe_name = input("Please Enter your recipe name here: ")
    recipe.name = recipe_name

    while True:
        try:
            ingredient = input("Please Enter the Ingredient name available: ")
            if ingredient == "":
                break

            qty = input("please Enter a valid qty (1 for 100g): ")
            if qty == "":
                break

            if qty.isdigit() or isfloat(qty):
                recipe.ingredients = (ingredient, float(qty))
            else:
                print("you did not enter a valid number, please try again ")

        except EOFError:
            break

    recipe_description = input("Please write the description of your recipe: ")
    recipe.description = recipe_description

    print(json.dumps(get_recipe_info(recipe), indent=4))

    create_pdf(recipe)

if __name__ == "__main__":
    main()
