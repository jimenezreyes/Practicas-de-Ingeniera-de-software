import React, { useState } from 'react';
import "./Clientes.css";

function Clientes() {
  const [clientes, setClientes] = useState([]);
  const [form, setForm] = useState({ nombre: '', email: '' });
  const [editIndex, setEditIndex] = useState(-1);

  const agregarCliente = () => {
    if (!form.nombre.trim() || !form.email.trim()) {
      alert("Por favor, ingresa nombre y email.");
      return;
    }

    if (clientes.some((cliente) => cliente.nombre === form.nombre && cliente.id !== form.id)) {
      alert("El cliente con este nombre ya existe.");
      return;
    }

    if (clientes.some((cliente) => cliente.email === form.email && cliente.id !== form.id)) {
      alert("El cliente con este email ya existe.");
      return;
    }

    if (editIndex === -1) {
      const nuevoCliente = { ...form, id: new Date().getTime() };
      setClientes([...clientes, nuevoCliente]);
      setForm({ nombre: '', email: '' });
    } else {
      const nuevosClientes = [...clientes];
      nuevosClientes[editIndex] = { ...form, id: nuevosClientes[editIndex].id };
      setClientes(nuevosClientes);
      setForm({ nombre: '', email: '' });
      setEditIndex(-1);
    }
  };

  const editarCliente = (index) => {
    const clienteAEditar = clientes[index];
    setForm({ nombre: clienteAEditar.nombre, email: clienteAEditar.email, id: clienteAEditar.id });
    setEditIndex(index);
  };

  const cancelarEdicion = () => {
    setForm({ nombre: '', email: '' });
    setEditIndex(-1);
  };

  const eliminarCliente = (id) => {
    const nuevosClientes = clientes.filter((cliente) => cliente.id !== id);
    setClientes(nuevosClientes);
    setEditIndex(-1);
  };

  return (
    <div>
      <h2>Clientes</h2>
      <div>
        <input
          type="text"
          value={form.nombre}
          onChange={(e) => setForm({ ...form, nombre: e.target.value })}
          placeholder="Nombre del cliente"
        />
        <input
          type="text"
          value={form.email}
          onChange={(e) => setForm({ ...form, email: e.target.value })}
          placeholder="Email del cliente"
        />
        {editIndex === -1 ? (
          <button onClick={agregarCliente}>Agregar Cliente</button>
        ) : (
          <div>
            <button onClick={agregarCliente}>Guardar</button>
            <button onClick={cancelarEdicion}>Cancelar</button>
          </div>
        )}
      </div>
      <ul>
        {clientes.map((cliente, index) => (
          <li key={cliente.id}>
            {editIndex === index ? (
              <div>
                <input
                  type="text"
                  value={form.nombre}
                  onChange={(e) => setForm({ ...form, nombre: e.target.value })}
                />
                <input
                  type="text"
                  value={form.email}
                  onChange={(e) => setForm({ ...form, email: e.target.value })}
                />
              </div>
            ) : (
              `${cliente.nombre} (${cliente.email})`
            )}
            {editIndex === -1 ? (
              <button onClick={() => editarCliente(index)}>Editar</button>
            ) : (
              <button disabled>Editar</button>
            )}
            <button onClick={() => eliminarCliente(cliente.id)}>Eliminar</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Clientes;