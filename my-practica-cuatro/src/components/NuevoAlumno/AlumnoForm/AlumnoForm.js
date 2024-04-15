import React, { useState } from "react";

import "./AlumnoForm.css";

const AlumnoForm = (props) => {
  const [nombreIngresado, setNombreIngresado] = useState("");
  const [apellidoIngresado, setApellidoIngresado] = useState("");
  const [idIngresado, setIdIngresado] = useState("");
  const [emailIngresado, setEmailIngresado] = useState("");
  const [passwordIngresado, setPasswordIngresado] = useState("");

  const cambioNombreHandler = (event) => {
    setNombreIngresado(event.target.value);
  };

  const cambioApellidoHandler = (event) => {
    setApellidoIngresado(event.target.value);
  };

  const cambioIdHandler = (event) => {
    setIdIngresado(event.target.value);
  };

  const cambioEmailHandler = (event) => {
    setEmailIngresado(event.target.value);
  };

  const cambioPasswordHandler = (event) => {
    setPasswordIngresado(event.target.value);
  };

  const submitHandler = (event) => {
    event.preventDefault();

    const alumno = {
      nombre: nombreIngresado,
      apellido: apellidoIngresado,
      id: idIngresado,
      email: emailIngresado,
      password: passwordIngresado
    };
    if (
      nombreIngresado === "" ||
      apellidoIngresado === "" ||
      idIngresado === "" ||
      emailIngresado === "" ||
      passwordIngresado === ""
    ) {
      alert("Campos vacíos!!");
      return;
    }
    props.onGuardarAlumno(alumno);
    setNombreIngresado("");
    setApellidoIngresado("");
    setIdIngresado("");
    setEmailIngresado("");
    setPasswordIngresado("");

  };

  return (

    <form onSubmit={submitHandler}>
      <h2>Lista de Clientes</h2>
      <div className="nuevo-alumno__controls">
        <div className="nuevo-alumno__control">
          <label>Nombre: </label>
          <input
            type="text"
            value={nombreIngresado}
            onChange={cambioNombreHandler}
          />
        </div>
        <div className="nuevo-alumno__control">
          <label>Apellido: </label>
          <input
            type="text"
            value={apellidoIngresado}
            onChange={cambioApellidoHandler}
          />
        </div>
        <div className="nuevo-alumno__control">
          <label>id.: </label>
          <input
            type="text"
            value={idIngresado}
            onChange={cambioIdHandler}
          />
        </div>
        <div className="nuevo-alumno__control">
          <label>Email: </label>
          <input
            type="text"
            value={emailIngresado}
            onChange={cambioEmailHandler}
          />
        </div>
        <div className="nuevo-alumno__control">
          <label>password: </label>
          <input
            type="text"
            value={passwordIngresado}
            onChange={cambioPasswordHandler}
          />
        </div>
        <div className="nuevo-alumno__actions">
          <button type="submit">Agregar Cliente</button>
        </div>
        <div className="nuevo-alumno__actions">
          <button type="submit">Ver Cliente</button>
        </div>
      </div>
    </form>
  );
};

export default AlumnoForm;
