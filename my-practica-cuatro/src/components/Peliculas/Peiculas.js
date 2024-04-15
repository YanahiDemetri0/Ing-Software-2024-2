import React from "react";

import Card from '../UI/Card';
import Pelicula from "./Pelicula/Pelicula";
import './Peliculas.css';

const Peliculas = (props) => {  
    return (
        <div>
            <Card className='alumnos'>
                <Pelicula
                    nombre={props.peliculas[0].nombre}
                    duracion={props.peliculas[0].duracion}
                    idPelicula={props.peliculas[0].idPelicula}
                    genero={props.peliculas[0].genero}
                    inventario={props.peliculas[0].inventario}

                />
                <Pelicula
                    nombre={props.peliculas[1].nombre}
                    duracion={props.peliculas[1].duracion}
                    idPelicula={props.peliculas[1].idPelicula}
                    genero={props.peliculas[1].genero}
                    inventario={props.peliculas[1].inventario}
                />
                <Pelicula
                    nombre={props.peliculas[2].nombre}
                    duracion={props.peliculas[2].duracion}
                    idPelicula={props.peliculas[2].idPelicula}
                    genero={props.peliculas[2].genero}
                    inventario={props.peliculas[2].inventario}
                />
            </Card>
        </div>
    )
};

export default Peliculas;