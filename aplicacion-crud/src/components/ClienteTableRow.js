import React from 'react'

const ClienteTableRow = ({el}) => {
    return (
        <tr>
            <td>{el.Nombre}</td>
            <td>{el.Apellido}</td>
            <th>{el.Id}</th>
            <th>{el.Email}</th>
            <th>{el.Password}</th>
        </tr>
            
    )
}

export default ClienteTableRow;