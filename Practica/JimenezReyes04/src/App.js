import React from 'react';
import { BrowserRouter as Router, Route, Routes, Switch } from 'react-router-dom';
import Rentas from './Rentas';
import Clientes from './Clientes';
import Peliculas from './Peliculas';
import Menu from './Menu';
import './App.css';

function App() {
  return (
    <div className="App">
      <Router>
        <Routes>
          <Route path="/" element={<Menu />} />
          <Route path="clientes" element={<Clientes />} />
          <Route path="peliculas" element={<Peliculas />} />
          <Route path="rentas" element={<Rentas />} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;