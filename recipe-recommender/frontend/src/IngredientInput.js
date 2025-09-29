import React, { useState } from 'react';

function IngredientInput({ onSubmit }) {
  const [ingredients, setIngredients] = useState('');

  return (
    <form onSubmit={(e) => { e.preventDefault(); onSubmit(ingredients.split(',').map(i => i.trim())); }}>
      <input
        type="text"
        placeholder="Enter ingredients (comma-separated)"
        onChange={(e) => setIngredients(e.target.value)}
      />
      <button type="submit">Find Recipes</button>
    </form>
  );
}

export default IngredientInput;
