import logo from './logo.svg';
import './App.css';
import Componente1 from './Componente1';
import Clock from './Clock';
import CambiaNome from './cambiaNome';
import LoginForm from './LoginForm';

//function getDate(date){
//  return date.toLocaleDateString()+" "+ date.toLocaleTimeString() 
//}

function App() {

  let nome = "Godwayne";


  return (
    <>
    <div className="App">

    <CambiaNome></CambiaNome>
  <FetchComponents></FetchComponents>

      <h1>Primo Elemento {nome}</h1>
      <Componente1>Godwayne</Componente1>
      <Componente1/>
      <h2>
        {
          new Date().toLocaleDateString()+" "+new Date().toLocaleTimeString()
        }
      </h2>
      <Clock timezone = "0" country  ="Italy"></Clock>
      <Clock timezone = "-6" country  ="Usa"></Clock>
      <Clock timezone = "87" country  ="Japan"></Clock>
        </div>  
     
      <footer>
        
      </footer>
  </>
  );


  
};

export default App;
