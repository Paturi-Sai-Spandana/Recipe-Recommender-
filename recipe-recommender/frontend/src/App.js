import React, { useState } from 'react';

function App() {
  const [ingredients, setIngredients] = useState('');
  const [recipes, setRecipes] = useState([]);
  const [expanded, setExpanded] = useState(new Set());

  const handleSubmit = async () => {
    const response = await fetch('http://localhost:5000/recommend', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ ingredients: ingredients.split(',').map(i => i.trim()) })
    });
    const data = await response.json();
    setRecipes(data);
  };

  return (
    <div style={{
      background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
      minHeight: '100vh',
      padding: '2rem',
      fontFamily: 'Arial, sans-serif',
      color: '#fff'
    }}>
      <div style={{ textAlign: 'center', marginBottom: '2rem' }}>
        <h1 style={{ fontSize: '3rem', marginBottom: '1rem', textShadow: '2px 2px 4px rgba(0,0,0,0.5)' }}>
          🍳 Recipe Recommender
        </h1>
        <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', gap: '1rem' }}>
          <input
            type="text"
            value={ingredients}
            onChange={e => setIngredients(e.target.value)}
            placeholder="Enter ingredients (e.g., egg, milk, tomato)"
            style={{
              width: '400px',
              padding: '0.75rem',
              borderRadius: '25px',
              border: 'none',
              fontSize: '1rem',
              boxShadow: '0 4px 8px rgba(0,0,0,0.2)'
            }}
          />
          <button
            onClick={handleSubmit}
            style={{
              padding: '0.75rem 1.5rem',
              backgroundColor: '#ff6b6b',
              color: '#fff',
              border: 'none',
              borderRadius: '25px',
              fontSize: '1rem',
              cursor: 'pointer',
              boxShadow: '0 4px 8px rgba(0,0,0,0.2)',
              transition: 'background-color 0.3s'
            }}
            onMouseOver={e => e.target.style.backgroundColor = '#ff5252'}
            onMouseOut={e => e.target.style.backgroundColor = '#ff6b6b'}
          >
            🔍 Get Recipes
          </button>
        </div>
      </div>

      <div style={{ display: 'flex', flexWrap: 'wrap', justifyContent: 'center', gap: '2rem' }}>
        {recipes.map((r, idx) => (
          <div 
            key={idx} 
            style={{
              backgroundColor: '#fff',
              color: '#333',
              borderRadius: '15px',
              padding: '1.5rem',
              width: '300px',
              boxShadow: '0 8px 16px rgba(0,0,0,0.2)',
              transition: 'transform 0.3s',
              textAlign: 'center'
            }}
            onMouseOver={e => e.currentTarget.style.transform = 'translateY(-5px)'}
            onMouseOut={e => e.currentTarget.style.transform = 'translateY(0)'}
          >
            <h3 style={{ color: '#333', marginBottom: '0.5rem' }}>{r.name}</h3>
            <p style={{ color: '#666', marginBottom: '0.5rem' }}>
              <strong>❌ Missing:</strong> {r.missing.join(', ') || 'None'}
            </p>
            <p style={{ color: '#666', marginBottom: '0.5rem' }}>
              <strong>✅ Substitutes:</strong> {r.substitutes.join(', ') || 'None'}
            </p>
            <p style={{ color: '#666', marginBottom: '0.5rem' }}>
              <strong>⏱️ Prep Time:</strong> {r.prep_time}
            </p>
            <p style={{ color: '#666', marginBottom: '0.5rem' }}>
              <strong>🍎 Nutrition:</strong> {r.nutrition}
            </p>
            <p style={{ color: '#666', marginBottom: '0.5rem' }}>
              <strong>🥗 Dietary:</strong> {r.dietary_restrictions || 'None'}
            </p>
            <button
              onClick={() => {
                const newExpanded = new Set(expanded);
                if (newExpanded.has(idx)) {
                  newExpanded.delete(idx);
                } else {
                  newExpanded.add(idx);
                }
                setExpanded(newExpanded);
              }}
              style={{
                padding: '0.5rem 1rem',
                backgroundColor: '#ff6b6b',
                color: '#fff',
                border: 'none',
                borderRadius: '5px',
                cursor: 'pointer',
                marginBottom: '0.5rem'
              }}
            >
              {expanded.has(idx) ? 'Hide Steps' : 'Show Steps'}
            </button>
            {expanded.has(idx) && (
              <p style={{ color: '#666' }}>
                <strong>📋 Steps:</strong> {r.steps}
              </p>
            )}
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;
