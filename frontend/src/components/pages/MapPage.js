import React from 'react';
import {Button} from 'reactstrap';
import MapChart from "../../MapChart";  
import axios from 'axios';

export default class OptionsPageCountries extends React.Component {
    constructor(){
        super();
        this.state = {
            data: [],
            value:""
        };
        this.handleSubmit = this.handleSubmit.bind(this);
        this.handleChange = this.handleChange.bind(this);
    
      }

    render() {
        return (
            <header className="App-header">
                <form onSubmit={this.handleSubmit}>
                <label>
                    Time:
                    <input type="text" value={this.state.value} onChange={this.handleChange} name="time" />
                </label>
                <input type="submit" value="Submit" />  
                </form> 
                <MapChart mapdata={this.state.data}/>
                <Button color="danger" href="/options">Back</Button>
            </header>
        )
    }
    handleChange(event) {
        this.setState({value: event.target.value});
      }
      
      handleSubmit(e) {
        e.preventDefault();
        axios.post('http://localhost:3002/getmessage',{
          time: this.state.value
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