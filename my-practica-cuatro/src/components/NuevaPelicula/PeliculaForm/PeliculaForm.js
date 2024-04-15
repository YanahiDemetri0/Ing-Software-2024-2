import React, { useState } from "react";

import "./PeliculaForm.css";

const PeliculaForm = (props) => {
  const [nombreIngresado, setNombreIngresado] = useState("");
  const [duracionIngresado, setDuracionIngresado] = useState("");
  const [idPeliculaIngresado, setIdPeliculaIngresado] = useState("");
  const [generoIngresado, setGeneroIngresado] = useState("");
  const [inventarioIngresado, setInventarioIngresado] = useState("");

  const cambioNombreHandler = (event) => {
    setNombreIngresado(event.target.value);
  };

  const cambioDuracionHandler = (event) => {
    setDuracionIngresado(event.target.value);
  };

  const cambioIdPeliculaHandler = (event) => {
    setIdPeliculaIngresado(event.target.value);
  };

  const cambioGeneroHandler = (event) => {
    setGeneroIngresado(event.target.value);
  };

  const cambioInventarioHandler = (event) => {
    setInventarioIngresado(event.target.value);
  };

  const submitHandler = (event) => {
    event.preventDefault();

    const pelicula = {
      nombre: nombreIngresado,
      duracion: duracionIngresado,
      idPelicula: idPeliculaIngresado,
      genero: generoIngresado,
      inventario: inventarioIngresado
    };
    if (
      nombreIngresado === "" ||
      duracionIngresado === "" ||
      idPeliculaIngresado === "" ||
      generoIngresado === "" ||
      inventarioIngresado === ""
    ) {
      alert("Campos vacíos!!");
      return;
    }
    props.onGuardarPelicula(pelicula);
    setNombreIngresado("");
    setDuracionIngresado("");
    setIdPeliculaIngresado("");
    setGeneroIngresado("");
    setInventarioIngresado("");

  };

  return (

    <form onSubmit={submitHandler}>
      <h2> Agregar Pelicula a la lista</h2>
      <div className="nueva-pelicula__controls">
        <div className="nueva-pelicula__control">
          <label>Nombre: </label>
          <input
            type="text"
            value={nombreIngresado}
            onChange={cambioNombreHandler}
          />
        </div>
        <div className="nueva-pelicula__control">
          <label>Duracion: </label>
          <input
            type="text"
            value={duracionIngresado}
            onChange={cambioDuracionHandler}
          />
        </div>
        <div className="nueva-pelicula__control">
          <label>idPelicula.: </label>
          <input
            type="text"
            value={idPeliculaIngresado}
            onChange={cambioIdPeliculaHandler}
          />
        </div>
        <div className="nueva-pelicula__control">
          <label>Genero: </label>
          <input
            type="text"
            value={generoIngresado}
            onChange={cambioGeneroHandler}
          />
        </div>
        <div className="nueva-pelicula__control">
          <label>inventario: </label>
          <input
            type="text"
            value={inventarioIngresado}
            onChange={cambioInventarioHandler}
          />
        </div>
        <div className="nueva-pelicula__actions">
          <button type="submit">Agregar Pelicula</button>
        </div>
        <div className="nueva-pelicula__actions">
          <button type="submit">Buscar Pelicula</button>
        </div>
      </div>
    </form>
  );
};

export default PeliculaForm;
