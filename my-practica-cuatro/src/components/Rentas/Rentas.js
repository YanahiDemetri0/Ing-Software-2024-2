import React from "react";

import Card from '../UI/Card';
import Renta from "./Renta/Renta";
import './Rentas.css';

const Rentas = (props) => {  
    return (
        <div>
            <Card className='rentas'>
                <Renta
                    idCliente={props.rentas[0].idCliente}
                    idPelicula={props.rentas[0].idPelicula}
                    idRenta={props.rentas[0].idRenta}
                    dias={props.rentas[0].dias}
                    fecha={props.rentas[0].fecha}

                />
                <Renta
                    idCliente={props.rentas[1].idCliente}
                    idPelicula={props.rentas[1].idPelicula}
                    idRenta={props.rentas[1].idRenta}
                    dias={props.rentas[1].dias}
                    fecha={props.rentas[1].fecha}
                />
                <Renta
                   idCliente={props.rentas[2].idCliente}
                   idPelicula={props.rentas[2].idPelicula}
                   idRenta={props.rentas[2].idRenta}
                   dias={props.rentas[2].dias}
                   fecha={props.rentas[2].fecha}
                />
            </Card>
        </div>
    )
};

export default Rentas;