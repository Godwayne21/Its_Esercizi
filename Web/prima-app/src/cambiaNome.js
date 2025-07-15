import { Button } from "bootstrap";
import { useState } from "react";

const CambiaNome = () => {
    const [nome,setNome] = useState("James");
    const cambia =()=>{
        if(nome === "James"){
            setNome("Steph");
        }
        else setNome("James");
    };
return (
    <div>
        <h3>{nome}</h3>
        <button className = "btn btn-dark" onClick = {cambia}>
            CambiaNome
        </button>
    </div>
);

}

export default CambiaNome;