const API_URL = "http://localhost:4000/tasks"

export const fetchTasks = async () => {
        const response = await fetch(API_URL);
        if (!response.ok) throw new Error("Errore fetch :(")
        const data = await response.json();
        return data;
};


export const createTask=async (text) =>{
    await fetch(API_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body:JSON.stringify({text,completed:false})
    });}

export const deleteTaskS = async (id) => {
        await fetch(API_URL + "/" + id, { method: "DELETE" });}

export    const toggleTaskS = async (id, completed) => {
        await fetch(API_URL + "/" + id, {
            method: "PATCH",
            headers: { "Content-Type": "application/json" }, body: JSON.stringify({ completed: !completed })
        });}
