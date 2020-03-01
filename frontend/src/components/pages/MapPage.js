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
                Map Page
                <Button color="danger" href="/options">Back</Button>
            </header>
        )
    }
}