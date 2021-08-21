import './App.css';
import Header from './Header';
import Services from './Services';
import {useState} from 'react';

function App() {

  let [home, changeHome] = useState("Hello World");

  function fnChange()
  {
    if(home == "Hello World")
      changeHome("React: Day 2");
    else
      changeHome("Hello World");

  }

  return (
    <div className="App">
      <Header/>

      <div style={{width: "50%", margin: "auto", display: "flex", justifyContent: "space-around", alignItems: "center"}}>
        <h1 style={{textAlign: "center"}}>{home}</h1>
        <button onClick={fnChange}>Change H1</button>
      </div>
      
      <Services/>
    </div>
  );
}

export default App;
