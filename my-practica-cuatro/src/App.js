import React, { useState } from "react";

import "./App.css";

import Alumnos from "./components/Alumnos/Alumnos";
import NuevoAlumno from "./components/NuevoAlumno/NuevoAlumno";
import Peliculas from "./components/Peliculas/Peiculas";
import NuevaPelicula from "./components/NuevaPelicula/NuevaPelicula";
import NuevaRenta from "./components/NuevaRenta/NuevaRenta";
import Rentas from "./components/Rentas/Rentas"


function App() {

  const [alumnos, setAlumnos] = useState([
    {
      nombre: "Fernando",
      apellido: "Fong",
      id: 142,
      email: "fong@gmail.com",
      password: 7263664,
    },
    {
      nombre: "Valeria",
      apellido: "Garcia",
      id: 231,
      email: "vale@gmail.com",
      password: 7263664,
    },
    {
      nombre: "Erick",
      apellido: "Martinez",
      id: 651,
      email: "erick@gmail.com",
      password: 7263664,
    },]);

    const [peliculas, setPelicula] = useState([
      {
        nombre: "Tierra de osos",
        duracion: "1:42:00",
        idPelicula: 352,
        Genero: "Animada",
        Inventario: 3,
      },
      {
        nombre: "It",
        duracion: "1:18:00",
        idPelicula: 824,
        Genero: "Terror",
        Inventario: 2,
      },
      {
        nombre: "Mundo de Terabithia",
        duracion: "1:23:50",
        idPelicula: 679,
        Genero: "Drama",
        Inventario: 1
      },]);

      const [rentas, setRenta] = useState([
        {
          idClient: 1,
          idPelicula: 21,
          idRenta: 313320679,
          fecha: "23-01-23",
          dias: 3
        },
        {
          idClient: 2,
          idPelicula: 11,
          idRenta: 313373949,
          fecha: "24-01-23",
          dias: 4
        },
        {
          idClient: 3,
          idPelicula: 18,
          idRenta: 937320679,
          fecha: "25-01-23",
          dias: 5
        },]);

  const agregarAlumno = (alumno) => {
    const nuevoAlumno = [alumno, ...alumnos];
    setAlumnos(nuevoAlumno);
    console.log(nuevoAlumno);
  };

  const agregarPelicula = (pelicula) => {
    const nuevaPelicula = [pelicula, ...peliculas];
    setPelicula(nuevaPelicula);
    console.log(nuevaPelicula);
  };

  const agregarRenta = (renta) => {
    const nuevaRenta = [renta, ...rentas];
    setRenta(nuevaRenta);
    console.log(nuevaRenta);
  };

  return (
    <div className="App">
      <NuevoAlumno onAgregarAlumno={agregarAlumno} />
      <Alumnos alumnos={alumnos} />
      <NuevaPelicula onAgregarPelicula={agregarPelicula} />
      <Peliculas peliculas={peliculas} />
      <NuevaRenta onAgregarRenta={agregarRenta} />
      <Rentas rentas={rentas}/>
    </div>
  );
}

export default App;
