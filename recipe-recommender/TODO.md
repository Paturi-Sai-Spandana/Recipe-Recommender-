# TODO: Add Dietary Restrictions Flags

- [x] Update db_setup.py: Add 'dietary_restrictions' column to recipes table, update INSERT with sample flags (e.g., VEGETARIAN, VEGAN) for all 20 recipes.
- [x] Update logic.py: Modify SELECT to include dietary_restrictions, add it to results dict.
- [x] Update App.js: Add display for dietary_restrictions in recipe cards (after nutrition, before steps toggle).
- [x] Run db_setup.py to update database.
- [x] Restart backend server to apply logic changes.
- [x] Test: API returns dietary flags; UI shows them; 20 recipes load with all info; steps toggle works.
