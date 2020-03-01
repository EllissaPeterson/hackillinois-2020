import React from 'react';
import {Button} from 'reactstrap';

export default class OptionsPage extends React.Component {
    constructor(props) {
        super(props);

        this.state = {

        };
    }

    render() {
        return (
            <header className="App-header">
                Options Page
                <Button href="/options/countries">Enter</Button>
            </header>
        );
    }
}