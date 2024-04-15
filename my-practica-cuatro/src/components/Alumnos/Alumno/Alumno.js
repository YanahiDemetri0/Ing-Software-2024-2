import React from "react";

import Card from '../../UI/Card';
import './Alumno.css';

const Alumno = (props) => {
    return (
        <Card className='alumno'>
            <div className="alumno__description">
                <h2>{props.nombre}</h2>
                <h2>{props.apellido}</h2>
                <h2>{props.id}</h2>
                <h2>{props.email}</h2>
                <h2>{props.password}</h2>
            </div>
        </Card>
    );
}

export default Alumno