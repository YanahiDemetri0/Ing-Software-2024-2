import React from 'react'
import ClienteTableRow from './ClienteTableRow';

const ClienteTable = ({data}) => {
    return (
        <div>
            <h3>Tabla de Clientes</h3>
            <table>
                <thead>
                    <tr>
                        <th>Nombre</th>
                        <th>Apellido</th>
                        <th>Id</th>
                        <th>Email</th>
                        <th>Password</th>
                    </tr>
                </thead>
                <tbody>
                    {data.length === 0? (
                        <tr>
                            <td colSpan="3">Sin datos</td>
                        </tr>
                    ):(
                    data.map((el)=> <ClienteTableRow key={el.id} el={el}/>))}
                </tbody>
            </table>
        </div>
    )
}

export default ClienteTable;