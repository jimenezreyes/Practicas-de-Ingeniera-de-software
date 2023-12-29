import React from 'react';
import {Link} from 'react-router-dom';

const Menu = () => {
  return (
    <div>
      <nav>
        <ul>            
          <li>
            <Link to="/clientes">Clientes</Link>
          </li>
          <li>
            <Link to="/peliculas">Peliculas</Link>
          </li>
          <li>
            <Link to="/rentas">Rentas</Link>
          </li>
        </ul>
      </nav>   
    </div>
  );
}