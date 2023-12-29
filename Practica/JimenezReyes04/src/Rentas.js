import React, { useState } from 'react';
import './Rentas.css';

function Rentas() {
  const [rentas, setRentas] = useState([]); // Estado para almacenar la lista de rentas
  const [nuevaRenta, setNuevaRenta] = useState({
    id: '',
    cliente: '',
    pelicula: '',
    fechaDevolucion: '',
  }); // Estado para la nueva renta a agregar
  const [editIndex, setEditIndex] = useState(-1); // Estado para rastrear la renta en edición

  const agregarRenta = () => {
    // Función para agregar una nueva renta a la lista
    if (nuevaRenta.cliente.trim() === '' || nuevaRenta.pelicula.trim() === '') return; // No agregar rentas sin cliente o película
    setRentas([...rentas, nuevaRenta]);
    setNuevaRenta({
      id: '',
      cliente: '',
      pelicula: '',
      fechaDevolucion: '',
    }); // Limpiar el campo de nueva renta
  };

  const editarRenta = (index) => {
    // Función para poner una renta en modo de edición
    setEditIndex(index);
    setNuevaRenta(rentas[index]);
  };

  const guardarEdicion = () => {
    // Función para guardar la edición de la renta
    if (editIndex === -1) return; // Salir si no se está editando
    const nuevasRentas = [...rentas];
    nuevasRentas[editIndex] = nuevaRenta;
    setRentas(nuevasRentas);
    setNuevaRenta({
      id: '',
      cliente: '',
      pelicula: '',
      fechaDevolucion: '',
    }); // Limpiar el campo de nueva renta
    setEditIndex(-1); // Salir del modo de edición
  };

  const cancelarEdicion = () => {
    // Función para cancelar la edición de la renta
    setNuevaRenta({
      id: '',
      cliente: '',
      pelicula: '',
      fechaDevolucion: '',
    });
    setEditIndex(-1);
  };

  return (
    <div>
      <h2>Rentas</h2>

      {/* Formulario para agregar una nueva renta */}
      <div>
        <input
          type="text"
          value={nuevaRenta.cliente}
          onChange={(e) => setNuevaRenta({ ...nuevaRenta, cliente: e.target.value })}
          placeholder="Cliente"
        />
        <input
          type="text"
          value={nuevaRenta.pelicula}
          onChange={(e) => setNuevaRenta({ ...nuevaRenta, pelicula: e.target.value })}
          placeholder="Película"
        />
        <input
          type="text"
          value={nuevaRenta.fechaDevolucion}
          onChange={(e) => setNuevaRenta({ ...nuevaRenta, fechaDevolucion: e.target.value })}
          placeholder="Fecha de Devolución"
        />
        {editIndex === -1 ? (
          <button onClick={agregarRenta}>Agregar Renta</button>
        ) : (
          <div>
            <button onClick={guardarEdicion}>Guardar</button>
            <button onClick={cancelarEdicion}>Cancelar</button>
          </div>
        )}
      </div>

      {/* Lista de rentas */}
      <ul>
        {rentas.map((renta, index) => (
          <li key={index}>
            {editIndex === index ? (
              <div>
                <input
                  type="text"
                  value={nuevaRenta.cliente}
                  onChange={(e) => setNuevaRenta({ ...nuevaRenta, cliente: e.target.value })}
                />
                <input
                  type="text"
                  value={nuevaRenta.pelicula}
                  onChange={(e) => setNuevaRenta({ ...nuevaRenta, pelicula: e.target.value })}
                />
                <input
                  type="text"
                  value={nuevaRenta.fechaDevolucion}
                  onChange={(e) =>
                    setNuevaRenta({ ...nuevaRenta, fechaDevolucion: e.target.value })
                  }
                />
              </div>
            ) : (
              <>
                <strong>ID:</strong> {renta.id}
                <br />
                <strong>Cliente:</strong> {renta.cliente}
                <br />
                <strong>Película:</strong> {renta.pelicula}
                <br />
                <strong>Fecha de Devolución:</strong> {renta.fechaDevolucion}
              </>
            )}
            <button onClick={() => editarRenta(index)}>Editar</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Rentas;