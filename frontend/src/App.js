
import React, { Component } from 'react';


import axios from 'axios';




export default class App extends Component {
  constructor(){
        super();
        this.state = {
            data: null,
        };
    }

   

    render() {
      const{data}=this.state;
      return(        
        <div>
          <button type="button" onClick={this.handleLogin}>Button</button>
          <p>{data}</p>
        </div>      
        
      );
    }

    handleLogin() {
      axios.get('https://localhost:3001/')
  .then((response) => {
    console.log(response.data);
    console.log(response.status);
    console.log(response.statusText);
    console.log(response.headers);
    console.log(response.config);
  });
     
    }
      
 
}
