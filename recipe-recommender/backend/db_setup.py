import sqlite3
import os

db_path = os.path.join(os.path.dirname(__file__), 'recipes.db')
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS recipes")
cursor.execute("DROP TABLE IF EXISTS substitutions")

cursor.execute('''
CREATE TABLE recipes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    ingredients TEXT NOT NULL,
    steps TEXT NOT NULL,
    prep_time TEXT NOT NULL,
    nutrition TEXT NOT NULL,
    dietary_restrictions TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE substitutions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ingredient TEXT NOT NULL,
    alternatives TEXT NOT NULL
)
''')

cursor.executemany('''
INSERT INTO recipes (name, ingredients, steps, prep_time, nutrition, dietary_restrictions) VALUES (?, ?, ?, ?, ?, ?)
''', [
    ("Pasta", "tomato,garlic,basil", "1. Boil water and cook pasta according to package. 2. In a pan, sauté garlic, add tomatoes and basil. 3. Drain pasta, mix with sauce.", "20 min", "Calories: 400, Protein: 12g, Carbs: 70g, Fat: 5g", "VEGETARIAN"),
    ("Omelette", "egg,milk,cheese", "1. Whisk eggs with milk. 2. Heat pan, pour mixture. 3. Add cheese, fold when set.", "10 min", "Calories: 250, Protein: 18g, Carbs: 2g, Fat: 20g", "VEGETARIAN"),
    ("Salad", "lettuce,tomato,cucumber", "1. Wash and chop lettuce, tomato, cucumber. 2. Toss together. 3. Add dressing if desired.", "5 min", "Calories: 100, Protein: 4g, Carbs: 15g, Fat: 2g", "VEGAN,VEGETARIAN,GLUTEN-FREE"),
    ("Pizza", "dough,tomato sauce,cheese,pepperoni", "1. Roll out dough. 2. Spread sauce, add cheese and toppings. 3. Bake at 450°F for 12-15 min.", "30 min", "Calories: 800, Protein: 30g, Carbs: 100g, Fat: 35g", "VEGETARIAN"),
    ("Burger", "bun,beef,lettuce,tomato", "1. Grill beef patty. 2. Toast bun. 3. Assemble with lettuce and tomato.", "15 min", "Calories: 500, Protein: 25g, Carbs: 40g, Fat: 25g", "KETO,PALEO"),
    ("Chicken Soup", "chicken broth,carrots,celery,noodles", "1. Simmer broth with chopped carrots and celery. 2. Add noodles, cook until tender. 3. Season to taste.", "25 min", "Calories: 200, Protein: 15g, Carbs: 25g, Fat: 5g", "KETO,PALEO"),
    ("Chocolate Cake", "flour,sugar,eggs,butter,cocoa", "1. Mix dry ingredients. 2. Cream butter and sugar, add eggs. 3. Combine, bake at 350°F for 30 min.", "45 min", "Calories: 350, Protein: 5g, Carbs: 50g, Fat: 15g", "VEGETARIAN"),
    ("Grilled Cheese Sandwich", "bread,cheese,butter", "1. Butter bread, place cheese between slices. 2. Grill in pan until golden and melted.", "5 min", "Calories: 300, Protein: 12g, Carbs: 30g, Fat: 18g", "VEGETARIAN"),
    ("Vegetable Stir Fry", "broccoli,carrots,bell peppers,soy sauce", "1. Chop vegetables. 2. Stir fry in oil. 3. Add soy sauce, cook until tender.", "15 min", "Calories: 150, Protein: 5g, Carbs: 20g, Fat: 8g", "VEGAN,VEGETARIAN,GLUTEN-FREE"),
    ("Banana Smoothie", "banana,milk,yogurt,honey", "1. Blend banana, milk, yogurt, honey. 2. Serve chilled.", "5 min", "Calories: 250, Protein: 10g, Carbs: 40g, Fat: 5g", "VEGETARIAN"),
    ("Fried Rice", "rice,egg,carrot,pea,onion", "1. Cook rice and cool. 2. Sauté vegetables and egg. 3. Add rice and soy sauce, stir fry.", "20 min", "Calories: 350, Protein: 10g, Carbs: 60g, Fat: 8g", "VEGETARIAN"),
    ("Taco", "tortilla,ground beef,lettuce,cheese,tomato", "1. Cook ground beef with spices. 2. Warm tortillas. 3. Assemble with toppings.", "15 min", "Calories: 400, Protein: 20g, Carbs: 35g, Fat: 20g", "KETO,PALEO"),
    ("Apple Pie", "apple,flour,sugar,cinnamon,butter", "1. Make pie crust. 2. Fill with sliced apples, sugar, cinnamon. 3. Bake at 375°F for 45 min.", "60 min", "Calories: 450, Protein: 4g, Carbs: 65g, Fat: 20g", "VEGETARIAN"),
    ("Sushi Roll", "rice,nori,salmon,avocado,cucumber", "1. Prepare sushi rice. 2. Lay nori, add fillings. 3. Roll and slice.", "30 min", "Calories: 300, Protein: 15g, Carbs: 40g, Fat: 10g", "GLUTEN-FREE"),
    ("Falafel", "chickpeas,parsley,onion,garlic,cumin", "1. Blend chickpeas with herbs and spices. 2. Form balls. 3. Fry until golden.", "25 min", "Calories: 350, Protein: 15g, Carbs: 50g, Fat: 12g", "VEGAN,VEGETARIAN,GLUTEN-FREE"),
    ("Guacamole", "avocado,tomato,onion,lime,cilantro", "1. Mash avocado. 2. Mix with diced tomato, onion, cilantro. 3. Add lime juice.", "10 min", "Calories: 200, Protein: 3g, Carbs: 12g, Fat: 18g", "VEGAN,VEGETARIAN,KETO,PALEO,GLUTEN-FREE"),
    ("Pancakes", "flour,milk,egg,sugar,baking powder", "1. Mix batter. 2. Heat pan, pour batter. 3. Cook until bubbles form, flip.", "15 min", "Calories: 300, Protein: 8g, Carbs: 45g, Fat: 10g", "VEGETARIAN"),
    ("Lasagna", "pasta,ground beef,tomato sauce,cheese,ricotta", "1. Layer pasta, sauce, meat, cheeses. 2. Bake at 375°F for 30 min.", "45 min", "Calories: 600, Protein: 30g, Carbs: 50g, Fat: 30g", "KETO"),
    ("Cereal", "cereal,milk", "1. Pour cereal into bowl. 2. Add milk. 3. Eat immediately.", "2 min", "Calories: 200, Protein: 8g, Carbs: 35g, Fat: 3g", "VEGETARIAN"),
    ("Ice Cream Sundae", "ice cream,chocolate syrup,whipped cream,cherry", "1. Scoop ice cream into bowl. 2. Drizzle syrup, add whipped cream and cherry.", "5 min", "Calories: 500, Protein: 5g, Carbs: 60g, Fat: 25g", "VEGETARIAN")
])

cursor.executemany('''
INSERT INTO substitutions (ingredient, alternatives) VALUES (?, ?)
''', [
    ("milk", "almond milk,soy milk"),
    ("cheese", "tofu,nutritional yeast"),
    ("beef", "turkey,plant-based meat"),
    ("eggs", "flaxseed,applesauce"),
    ("butter", "margarine,coconut oil")
])

conn.commit()
conn.close()
print("Database setup complete with additional recipes.")

