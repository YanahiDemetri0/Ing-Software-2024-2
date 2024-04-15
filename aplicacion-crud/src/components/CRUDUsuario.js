import React from "react"
import ClienteForm from "./ClienteForm";
import ClienteTable from "./ClienteTable";
import { useState } from "react";

const initialDb = [
{
    nombre: "Yanahi",
    apellido: "Demetrio",
    id: 1,
    email: "demetrioyanahi@gmail.com",
    password: 3764572
},
{
    nombre: "Cesar",
    apellido: "Demetrio",
    id: 2,
    email: "demetriocesar@gmail.com",
    password: 30192572
},
{
    nombre: "Edgar",
    apellido: "Demetrio",
    id: 3,
    email: "demetrioedgar@gmail.com",
    password: 497730302
}
];


const CrudCliente = () => {

    const[dataToEdit, setDataToEdit] = useState(initialDb)
    const[cliente, setCliente] = useState(initialDb)

    const creatData = (data) => {};
    const updateData = (data) => {};
    const delteData = (id) => {};

    

    return (
        <div>
        <h2>CRUD Clientes</h2>
        <ClienteForm/>
        <ClienteTable data={cliente}/>
        <table></table>
        </div>
    )
}
export default CrudCliente