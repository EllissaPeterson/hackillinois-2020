
import React, { Component } from 'react';
import axios from 'axios';
import MapChart from "./MapChart";  

export default class App extends Component {
  constructor(){
    super();
    this.state = {
        data: null,
    };
    this.handleLogin = this.handleLogin.bind(this);
  }

   

  render() {
    const{data}=this.state;
    return(        
      <div>
        <button type="button" onClick={this.handleLogin}>Button</button>
        <p>{data}</p>
        <MapChart />
      </div>      
      
    );
  }

  handleLogin() {

    axios.get('http://localhost:3001/getmessage')
      .then((response) => {
       console.log(response);
       this.setState({data: response.data})
     })
    .catch((error)=>{
       console.log(error);
    });
      
  }
      
 
}
