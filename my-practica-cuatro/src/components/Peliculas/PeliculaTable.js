import React from 'react';

function UserTable({ users }) {
    return (
        <table>
            <thead>
                <tr>
                    <th>Nombre</th>
                    <th>Duracion</th>
                    <th>Id</th>
                    <th>Genero</th>
                    <th>Inventario</th>
                </tr>
            </thead>
            <tbody>
                {users.map((user) => (
                    <tr key={user.id}>
                        <td>{user.id}</td>
                        <td>{user.nombre}</td>
                        <td>{user.email}</td>
                    </tr>
                ))}
            </tbody>
        </table>
    );
}

export default UserTable;
