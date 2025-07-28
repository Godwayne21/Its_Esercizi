import React, { useEffect } from "react";

const FetchComponents = () => {
    const url = "https://jsonplaceholder.typicode.com/users";
    const [users,setUsers]=useState([]);
    useEffect(()=>{
        fetch(url)
    },[])
    return(
        <>
        <h1>Fetch User from jsonplaceholder</h1>
    <div>
        {
            users.map((u) => {
                return <p key ={u.id}>{u.name}</p>
            })
        }
    </div>
    </>
    );
}

export default FetchComponents;