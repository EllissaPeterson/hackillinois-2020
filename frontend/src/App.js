
import React, { Component } from 'react';
import axios from 'axios';
import MapChart from "./MapChart.jsx";  

export default class App extends Component {
  constructor(){
    super();
    this.state = {
        data: null,
        value:""
    };
    this.handleSubmit = this.handleSubmit.bind(this);
    this.handleChange = this.handleChange.bind(this);

  }

   

  render() {
    const{data}=this.state;
    return(        
      <div>
        <form onSubmit={this.handleSubmit}>
          <label>
            Time:
            <input type="text" value={this.state.value} onChange={this.handleChange} name="time" />
          </label>
          <input type="submit" value="Submit" />  
        </form> 
        <p>{data}</p>
        <MapChart />
      </div>      
      
    );
  }
  handleChange(event) {
    this.setState({value: event.target.value});
  }
  
  handleSubmit() {

    axios.get('http://localhost:3001/getmessage',{
      time: this.state.value,
    })
      .then((response) => {
       console.log(response);
       this.setState({data: response.data})
     })
    .catch((error)=>{
       console.log(error);
    });
      
  }
      
 
}
