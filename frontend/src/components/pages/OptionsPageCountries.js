import React from 'react';
import {Button} from 'reactstrap';

export default class OptionsPageCountries extends React.Component {
    constructor(props) {
        super(props);

        this.state = {

        };
    }

    render() {
        return (
            <header className="App-header">
                Options Page Countries
                <Button href="/map">Enter</Button>
            </header>
        )
    }
}