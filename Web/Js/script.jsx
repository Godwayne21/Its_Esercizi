const rootElement = document.querySelector("#root");

const root = ReactDOM.createRoot(rootElement);

const App = ()=>{
    return(
        <main className="main">
            <h1>Primo Componente</h1>
        </main>
    )
}

const List=()=>{
    return(
        <ul>
            <li>PhP</li>
            <li>JS</li>
            <li>Python</li>
        </ul>
    )
}

root.render(
    <App>
        <h2>Lista Competenze</h2>
        <List></List>
    </App>

)