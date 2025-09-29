import sqlite3
import os

def suggests_recipes(user_ingredients):
    try:
        db_path = os.path.join(os.path.dirname(__file__), 'recipes.db')
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute("SELECT name, ingredients, steps, prep_time, nutrition, dietary_restrictions FROM recipes")
        recipes = cursor.fetchall()

        cursor.execute("SELECT ingredient, alternatives FROM substitutions")
        subs_raw = cursor.fetchall()
        substitutions = {i: a.split(',') for i, a in subs_raw}

        results = []
        for name, ing_str, steps, prep_time, nutrition, dietary_restrictions in recipes:
            req_ingredients = [i.strip() for i in ing_str.split(',')]
            missing = [i for i in req_ingredients if i not in user_ingredients]
            substitutes = [substitutions.get(i, []) for i in missing]
            results.append({
                'name': name,
                'missing': missing,
                'substitutes': [item for sublist in substitutes for item in sublist],
                'steps': steps,
                'prep_time': prep_time,
                'nutrition': nutrition,
                'dietary_restrictions': dietary_restrictions
            })

        conn.close()
        return sorted(results, key=lambda x: len(x['missing']))
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    except Exception as e:
        print(f"Unexpected error: {e}")
        return []
