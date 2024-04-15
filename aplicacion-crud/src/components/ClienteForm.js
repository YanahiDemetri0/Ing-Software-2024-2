import React, { useState } from 'react'

const ClienteForm = () => {
    const initialForm = {
        nombre:"",
        Apellido: "",
        Id: "",
        Email: "",
        Password: ""
    }

    const[form, setForm]= useState(initialForm);

    const handleChange = (e) => {}

    const handleSubmit = (e) => {}
    
    const handleReset = (e) => {}

    
    return (
        <div>
            <h3>Agregar cliente</h3>
            <form onSubmit={handleSubmit}>
                <input type='text'name = "Nombre" placeholder='Nombre'onChange={handleChange} value={form.Nombre}/>
                <input type='text'name = "Apellido" placeholder='Apellido'onChange={handleChange} value={form.Apellido}/>
                <input type='text'name = "Id" placeholder='Id'onChange={handleChange} value={form.Id}/>
                <input type='text'name = "Email" placeholder='Email'onChange={handleChange} value={form.Email}/>
                <input type='text'name = "Password" placeholder='Password'onChange={handleChange} value={form.Password}/>
                <input type='submit' value = "Agregar Cliente" />
                <input type='reset' value = "Limpiar" onClick={handleReset}/>
            </form>
        </div>
    );
}

export default ClienteForm;