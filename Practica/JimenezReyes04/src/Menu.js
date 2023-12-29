import React from 'react';
import { useNavigate } from 'react-router-dom';
import "./Menu.css"; 


const Menu = () => {
  const navigate = useNavigate();

  const handleClickClientes = () => {
    navigate('/clientes');
  };

  const handleClickPeliculas = () => {
    navigate('/peliculas');
  };

  const handleClickRentas = () => {
    navigate('/rentas');
  };

  return (
    <div className = "Menu">
    <h1> Crunchyroll </h1>  
      <nav>
        <ul>            
          <li>
            <button onClick={handleClickClientes}>Clientes</button>
          </li>
          <li>
            <button onClick={handleClickPeliculas}>Peliculas</button>
          </li>
          <li>
            <button onClick={handleClickRentas}>Rentas</button>
          </li>
        </ul>
      </nav>   
    </div>
  );
};

export default Menu;

