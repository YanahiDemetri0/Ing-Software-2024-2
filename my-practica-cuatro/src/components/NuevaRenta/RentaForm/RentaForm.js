import React, { useState } from "react";

import "./RentaForm.css";

const RentaForm = (props) => {
  const [idClienteIngresado, setIdClienteIngresado] = useState("");
  const [idPeliculaIngresado, setIdPeliculaIngresado] = useState("");
  const [idRentaIngresado, setIdRentaIngresado] = useState("");
  const [diasIngresado, setDiasIngresado] = useState("");
  const [fechaIngresado, setFechaIngresado] = useState("");

  const cambioIdClienteHandler = (event) => {
    setIdClienteIngresado(event.target.value);
  };

  const cambioidPeliculaHandler = (event) => {
    setIdPeliculaIngresado(event.target.value);
  };

  const cambioIdRentaHandler = (event) => {
    setIdRentaIngresado(event.target.value);
  };

  const cambioDiasHandler = (event) => {
    setDiasIngresado(event.target.value);
  };

  const cambioFechaHandler = (event) => {
    setFechaIngresado(event.target.value);
  };

  const submitHandler = (event) => {
    event.preventDefault();

    const alumno = {
      idCliente: idClienteIngresado,
      idPelicula: idPeliculaIngresado,
      idRenta: idRentaIngresado,
      dias: diasIngresado,
      fecha: fechaIngresado
    };
    if (
      idClienteIngresado === "" ||
      idPeliculaIngresado === "" ||
      idRentaIngresado === "" ||
      diasIngresado === "" ||
      fechaIngresado === ""
    ) {
      alert("Campos vacíos!!");
      return;
    }
    props.onGuardarAlumno(alumno);
    setIdClienteIngresado("");
    setIdPeliculaIngresado("");
    setIdRentaIngresado("");
    setDiasIngresado("");
    setFechaIngresado("");

  };

  return (

    <form onSubmit={submitHandler}>
      <h2>Lista de Rentas</h2>
      <div className="nueva-renta__controls">
        <div className="nueva-renta__control">
          <label>ID Clientes: </label>
          <input
            type="text"
            value={idClienteIngresado}
            onChange={cambioIdClienteHandler}
          />
        </div>
        <div className="nueva-renta__control">
          <label>ID Peliculas: </label>
          <input
            type="text"
            value={idPeliculaIngresado}
            onChange={cambioidPeliculaHandler}
          />
        </div>
        <div className="nueva-renta__control">
          <label>ID Renta.: </label>
          <input
            type="text"
            value={idRentaIngresado}
            onChange={cambioIdRentaHandler}
          />
        </div>
        <div className="nueva-renta__control">
          <label>Fecha de renta: </label>
          <input
            type="text"
            value={fechaIngresado}
            onChange={cambioFechaHandler}
          />
        </div>
        <div className="nueva-renta__control">
          <label>Dias de renta: </label>
          <input
            type="text"
            value={diasIngresado}
            onChange={cambioDiasHandler}
          />
        </div>
        <div className="nueva-renta__actions">
          <button type="submit">Agregar Renta</button>
        </div>
      </div>
    </form>
  );
};

export default RentaForm;
