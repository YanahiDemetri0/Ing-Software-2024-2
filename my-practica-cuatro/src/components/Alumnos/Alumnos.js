import React from "react";

import Card from '../UI/Card';
import Alumno from "./Alumno/Alumno";
import './Alumnos.css';

const Alumnos = (props) => {  
    return (
        <div>
            <Card className='alumnos'>
                <Alumno
                    nombre={props.alumnos[0].nombre}
                    apellido={props.alumnos[0].apellido}
                    id={props.alumnos[0].id}
                    email={props.alumnos[0].email}
                    password={props.alumnos[0].password}

                />
                <Alumno
                    nombre={props.alumnos[1].nombre}
                    apellido={props.alumnos[1].apellido}
                    id={props.alumnos[1].id}
                    email={props.alumnos[1].email}
                    password={props.alumnos[1].password}
                />
                <Alumno
                    nombre={props.alumnos[2].nombre}
                    apellido={props.alumnos[2].apellido}
                    id={props.alumnos[2].id}
                    email={props.alumnos[2].email}
                    password={props.alumnos[2].password}
                />
            </Card>
        </div>
    )
};

export default Alumnos;