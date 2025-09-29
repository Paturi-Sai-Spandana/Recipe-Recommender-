function RecipeList({ recipes }) {
  return (
    <ul>
      {recipes.map((r, i) => (
        <li key={i}>
          <h3>{r.name}</h3>
          <p><strong>Missing:</strong> {r.missing.join(', ') || 'None'}</p>
          <p><strong>Substitutes:</strong> {r.substitutes.join(', ') || 'None'}</p>
        </li>
      ))}
    </ul>
  );
}

export default RecipeList;
