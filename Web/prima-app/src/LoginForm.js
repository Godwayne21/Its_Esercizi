import React from 'react'
import { useState} from 'react'

const LoginForm = () => {
    //const [nome, setNome]=useState("")
    //const [cognome, setCognome]=useState("")
    const [persone, setPersone]=useState({
        nome: "",
        cognome: ""
    })
    const gestioneDati=(e)=>{
        e.preventDefault();
        if(nome && cognome){
            setPersone([
                ...persone,
            {nome,
                cognome
            }
            ])
            setNome("")
            setCognome("")
        }else{
            alert("Inserisci tutti i dati")
        }
console.log(e)
        }
        const handlerChange=(e)=>{
            //const {name,value}=e.target
            setPersone({...persone,[e.target.name]:e.targetvalue})
        }
    
  return (
    <div className="container">
      <form className="row g-3" onSubmit={gestioneDati}>
        <div className="col-md-6">
          <label htmlFor="nome">Nome</label>
          <input
            type="text"
            id="nome"
            className="form-control"
            required
            name ="nome"
            value={persone.nome}
            onChange={handlerChange}
          ></input>
        </div>
    <div className="col-md-6">
          <label htmlFor="cognome">Cognome</label>
          <input
            type="text"
            id="cognome"
            className="form-control"
            required
            name="cognome"
            value={persone.cognome}
            onChange={handlerChange}
          ></input>
        </div>

        <button className="btn btn-success">Login</button>
      </form><br></br>
      <div>
        {
            persone.map((p,index)=>{
                return (<p key={index}>{p.nome} {p.cognome}</p>)
            })
        }
      </div>
    </div>

  )
}

export default LoginForm;

/*
            <div>
                
                <label htmlFor= "email">Email</label>
                <input type = "email" id ="email" required value = {email} onChange={(e)=>setEmail(e.target.value)}></input>
            </div>
            <div>
                <label>Password</label>
                <input type = "password" id ="password" required value ={password} onChange={(e)=>setPassword(e.target.value)}></input>
            </div>
*/
