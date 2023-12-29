import React, { useState } from 'react';
import './Peliculas.css';

function Peliculas() {
  const [peliculas, setPeliculas] = useState([]); 
  const [form, setForm] = useState({ id: '', nombre: '', año: '', genero: '' });
  const [editIndex, setEditIndex] = useState(-1);

  const agregarPelicula = () => {
    if (!form.nombre.trim() || !form.año.trim() || !form.genero.trim()) {
      alert("Por favor, ingresa nombre, año y género de la película.");
      return;
    }

    if (!/^\d{4}-\d{2}-\d{2}$/.test(form.año)) {
      alert("El campo 'Año' debe tener el formato 'aaaa-mm-dd'.");
      return;
    }

    if (editIndex === -1) {
      // Agregar una nueva película
      const nuevaPelicula = { ...form, id: new Date().getTime() };
      setPeliculas([...peliculas, nuevaPelicula]);
    } else {
      // Guardar la edición de una película existente
      const nuevasPeliculas = [...peliculas];
      nuevasPeliculas[editIndex] = form;
      setPeliculas(nuevasPeliculas);
      setEditIndex(-1); // Salir del modo de edición
    }

    // Limpiar el formulario
    setForm({ id: '', nombre: '', año: '', genero: '' });
  };

  const editarPelicula = (index) => {
    const peliculaAEditar = peliculas[index];
    setForm({ ...peliculaAEditar });
    setEditIndex(index);
  };

  const cancelarEdicion = () => {
    setEditIndex(-1); // Salir del modo de edición
    setForm({ id: '', nombre: '', año: '', genero: '' }); // Limpiar el formulario
  };

  const eliminarPelicula = (index) => {
    const nuevasPeliculas = [...peliculas];
    nuevasPeliculas.splice(index, 1);
    setPeliculas(nuevasPeliculas);
  };

  return (
    <div>
      <h2>Películas</h2>
      <div>
        <input
          type="text"
          value={form.nombre}
          onChange={(e) => setForm({ ...form, nombre: e.target.value })}
          placeholder="Título de la película"
        />
        <input
          type="text"
          value={form.año}
          onChange={(e) => setForm({ ...form, año: e.target.value })}
          placeholder="Año de la película (aaaa-mm-dd)"
        />
        <input
          type="text"
          value={form.genero}
          onChange={(e) => setForm({ ...form, genero: e.target.value })}
          placeholder="Género de la película"
        />
        {editIndex === -1 ? (
          <button onClick={agregarPelicula}>Agregar Película</button>
        ) : (
          <div>
            <button onClick={agregarPelicula}>Guardar</button>
            <button onClick={cancelarEdicion}>Cancelar</button>
          </div>
        )}
      </div>
      <ul>
        {peliculas.map((pelicula, index) => (
          <li key={pelicula.id}>
            {editIndex === index ? (
              <div>
                <input
                  type="text"
                  value={form.nombre}
                  onChange={(e) => setForm({ ...form, nombre: e.target.value })}
                />
                <input
                  type="text"
                  value={form.año}
                  onChange={(e) => setForm({ ...form, año: e.target.value })}
                />
                <input
                  type="text"
                  value={form.genero}
                  onChange={(e) => setForm({ ...form, genero: e.target.value })}
                />
              </div>
            ) : (
              `${pelicula.nombre} (${pelicula.año}) - ${pelicula.genero}`
            )}
            {editIndex === -1 ? (
              <button onClick={() => editarPelicula(index)}>Editar</button>
            ) : (
              <button disabled>Editar</button>
            )}
            <button onClick={() => eliminarPelicula(index)}>Eliminar</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Peliculas;